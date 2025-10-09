#to run this use -- streamlit run C:/Users/aryan/OneDrive/Desktop/areeeeeee/carrer-decider/app.py
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import io

# Page configuration
st.set_page_config(
    page_title="Career Decider - Find Your Path",
    page_icon="🎓",
    layout="wide"
)

# Initialize session state
if 'responses' not in st.session_state:
    st.session_state.responses = {}
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'result' not in st.session_state:
    st.session_state.result = None

# Career domains data
CAREER_DOMAINS = {
    "Software Development": {
        "subdomains": "Backend, Frontend, Full-Stack, DevOps",
        "skills": "Python, C++, React, APIs, Git, Docker",
        "salary": "₹6–40 LPA",
        "companies": "Google, Microsoft, Atlassian, Amazon",
        "description": "Build scalable applications and systems that power the digital world.",
        "learning_resources": "LeetCode, FreeCodeCamp, The Odin Project"
    },
    "Data Science": {
        "subdomains": "Data Analysis, Data Engineering, Business Intelligence",
        "skills": "Python, Pandas, SQL, Power BI, Machine Learning",
        "salary": "₹8–35 LPA",
        "companies": "Amazon, Flipkart, Walmart, Nielsen",
        "description": "Extract insights from data to drive business decisions.",
        "learning_resources": "Kaggle, DataCamp, Google Data Analytics Certificate"
    },
    "Artificial Intelligence & Machine Learning": {
        "subdomains": "Deep Learning, NLP, Computer Vision",
        "skills": "Python, TensorFlow, PyTorch, Scikit-learn",
        "salary": "₹10–50 LPA",
        "companies": "Google, Microsoft, OpenAI, NVIDIA",
        "description": "Create intelligent systems that learn and adapt.",
        "learning_resources": "Coursera ML, Fast.ai, Hugging Face, Papers with Code"
    },
    "Cybersecurity": {
        "subdomains": "Ethical Hacking, Network Security, Cloud Security",
        "skills": "Linux, Networking, OWASP, Kali Linux",
        "salary": "₹7–35 LPA",
        "companies": "Cisco, Palo Alto Networks, CrowdStrike",
        "description": "Protect systems and data from cyber threats.",
        "learning_resources": "TryHackMe, HackTheBox, Cybrary"
    },
    "Cloud Computing & DevOps": {
        "subdomains": "AWS, Azure, GCP, CI/CD",
        "skills": "Docker, Kubernetes, Jenkins, Terraform",
        "salary": "₹8–40 LPA",
        "companies": "Amazon, Microsoft, Google, HashiCorp",
        "description": "Build and manage scalable cloud infrastructure.",
        "learning_resources": "AWS Free Tier, Azure Learn, Google Cloud Skills"
    },
    "Web Development": {
        "subdomains": "Frontend, Backend, Full Stack",
        "skills": "HTML, CSS, JavaScript, Django, React",
        "salary": "₹5–25 LPA",
        "companies": "Vercel, Netlify, Shopify, WordPress",
        "description": "Create beautiful and functional websites and web apps.",
        "learning_resources": "FreeCodeCamp, MDN Web Docs, JavaScript.info"
    },
    "UI/UX & Product Design": {
        "subdomains": "Visual Design, UX Research, Prototyping",
        "skills": "Figma, Adobe XD, Design Thinking",
        "salary": "₹4–20 LPA",
        "companies": "Adobe, Figma, Canva, InVision",
        "description": "Design user-centered digital experiences.",
        "learning_resources": "Google UX Design Certificate, Figma Community, NNGroup"
    },
    "Blockchain Development": {
        "subdomains": "Smart Contracts, DApps, DeFi",
        "skills": "Solidity, Ethereum, Web3.js",
        "salary": "₹10–50 LPA",
        "companies": "Coinbase, Polygon, ConsenSys",
        "description": "Build decentralized applications and smart contracts.",
        "learning_resources": "CryptoZombies, Ethernaut, Alchemy University"
    },
    "Game Development": {
        "subdomains": "Unity, Unreal Engine, AR/VR",
        "skills": "C#, C++, Blender",
        "salary": "₹6–30 LPA",
        "companies": "Unity, Epic Games, Ubisoft",
        "description": "Create immersive gaming experiences.",
        "learning_resources": "Unity Learn, Unreal Engine Docs, Brackeys"
    },
    "Research & Academia": {
        "subdomains": "AI Research, Quantum Computing, Education",
        "skills": "Python, Research papers, Data Analysis",
        "salary": "₹8–25 LPA",
        "companies": "IITs, IISc, Microsoft Research, Google Research",
        "description": "Advance knowledge through research and teaching.",
        "learning_resources": "arXiv, Google Scholar, Coursera Research Methods"
    }
}

def calculate_career_match(responses):
    """Calculate career match scores based on user responses"""
    scores = {domain: 0 for domain in CAREER_DOMAINS.keys()}
    
    # Question 1: Task preference
    task_map = {
        "Problem-solving": ["Software Development", "Artificial Intelligence & Machine Learning", "Cybersecurity"],
        "Designing visuals": ["UI/UX & Product Design", "Web Development", "Game Development"],
        "Managing teams": ["Cloud Computing & DevOps", "Research & Academia"],
        "Research and innovation": ["Artificial Intelligence & Machine Learning", "Research & Academia", "Blockchain Development"],
        "Communication or writing": ["UI/UX & Product Design", "Research & Academia"]
    }
    if 'q1' in responses:
        for domain in task_map.get(responses['q1'], []):
            scores[domain] += 15
    
    # Question 2: Subject preference
    subject_map = {
        "Mathematics": ["Artificial Intelligence & Machine Learning", "Data Science", "Research & Academia"],
        "Programming": ["Software Development", "Web Development"],
        "Physics": ["Game Development", "Research & Academia"],
        "Art/Design": ["UI/UX & Product Design", "Game Development"],
        "Business/Management": ["Data Science", "Cloud Computing & DevOps"]
    }
    if 'q2' in responses:
        for domain in subject_map.get(responses['q2'], []):
            scores[domain] += 12
    
    # Question 3: Competitive coding
    if responses.get('q3') == "Yes":
        scores["Software Development"] += 10
        scores["Artificial Intelligence & Machine Learning"] += 8
    
    # Question 4: Creative vs Structured
    if responses.get('q4') == "Creative design":
        scores["UI/UX & Product Design"] += 15
        scores["Web Development"] += 10
        scores["Game Development"] += 10
    else:
        scores["Software Development"] += 10
        scores["Data Science"] += 10
        scores["Cybersecurity"] += 8
    
    # Question 5: People vs Machines
    if responses.get('q5') == "People":
        scores["UI/UX & Product Design"] += 10
        scores["Research & Academia"] += 8
    elif responses.get('q5') == "Machines":
        scores["Software Development"] += 8
        scores["Cybersecurity"] += 8
    
    # Question 6-8: Technical skills (weighted heavily)
    coding_comfort = responses.get('q6', 5)
    math_enjoyment = responses.get('q7', 5)
    analytical = responses.get('q8', 5)
    
    scores["Software Development"] += coding_comfort * 2
    scores["Web Development"] += coding_comfort * 1.5
    scores["Artificial Intelligence & Machine Learning"] += (coding_comfort + math_enjoyment + analytical) * 1.2
    scores["Data Science"] += (math_enjoyment + analytical) * 1.5
    scores["Cybersecurity"] += analytical * 2
    scores["Cloud Computing & DevOps"] += coding_comfort * 1.5
    
    # Question 9: Learning new languages
    if responses.get('q9') == "Yes":
        scores["Software Development"] += 8
        scores["Web Development"] += 8
        scores["Blockchain Development"] += 10
    
    # Question 10: Technology interest
    tech_map = {
        "Web Development": ["Web Development"],
        "Data Science": ["Data Science"],
        "Artificial Intelligence": ["Artificial Intelligence & Machine Learning"],
        "Cybersecurity": ["Cybersecurity"],
        "Cloud Computing": ["Cloud Computing & DevOps"],
        "Software Engineering": ["Software Development"]
    }
    if 'q10' in responses:
        for domain in tech_map.get(responses['q10'], []):
            scores[domain] += 20
    
    # Question 11: Solo vs Team
    if responses.get('q11') == "Solo work":
        scores["Software Development"] += 5
        scores["Research & Academia"] += 8
    else:
        scores["Cloud Computing & DevOps"] += 8
        scores["UI/UX & Product Design"] += 6
    
    # Question 12: Creativity importance
    creativity = responses.get('q12', 5)
    scores["UI/UX & Product Design"] += creativity * 2
    scores["Game Development"] += creativity * 1.8
    scores["Web Development"] += creativity * 1.2
    
    # Question 13: Leadership vs Technical
    if responses.get('q13') == "Leadership":
        scores["Cloud Computing & DevOps"] += 10
        scores["Research & Academia"] += 8
    else:
        scores["Software Development"] += 10
        scores["Artificial Intelligence & Machine Learning"] += 10
        scores["Cybersecurity"] += 8
    
    # Question 14: Experimenting
    if responses.get('q14') == "Yes":
        scores["Artificial Intelligence & Machine Learning"] += 10
        scores["Blockchain Development"] += 12
        scores["Game Development"] += 8
    
    # Question 15: Building vs Analyzing
    if responses.get('q15') == "Building systems":
        scores["Software Development"] += 12
        scores["Cloud Computing & DevOps"] += 12
        scores["Web Development"] += 10
    else:
        scores["Data Science"] += 15
        scores["Artificial Intelligence & Machine Learning"] += 12
        scores["Cybersecurity"] += 8
    
    # Question 16: Company type
    company_map = {
        "Big Tech (FAANG)": ["Software Development", "Artificial Intelligence & Machine Learning", "Cloud Computing & DevOps"],
        "Startups": ["Web Development", "Blockchain Development", "UI/UX & Product Design"],
        "Research or Academia": ["Research & Academia", "Artificial Intelligence & Machine Learning"],
        "Government / PSU": ["Cybersecurity", "Data Science"]
    }
    if 'q16' in responses:
        for domain in company_map.get(responses['q16'], []):
            scores[domain] += 10
    
    # Question 17: Dream job focus
    focus_map = {
        "Innovation": ["Artificial Intelligence & Machine Learning", "Blockchain Development", "Research & Academia"],
        "Stability": ["Software Development", "Cloud Computing & DevOps"],
        "Money": ["Artificial Intelligence & Machine Learning", "Blockchain Development", "Software Development"],
        "Fame / Recognition": ["Game Development", "UI/UX & Product Design", "Research & Academia"]
    }
    if 'q17' in responses:
        for domain in focus_map.get(responses['q17'], []):
            scores[domain] += 10
    
    # Question 18: Freelancing
    if responses.get('q18') == "Yes":
        scores["Web Development"] += 12
        scores["UI/UX & Product Design"] += 12
        scores["Blockchain Development"] += 8
    
    # Question 19: Learning time
    learning_time = responses.get('q19', 10)
    if learning_time > 20:
        scores["Artificial Intelligence & Machine Learning"] += 10
        scores["Blockchain Development"] += 8
        scores["Research & Academia"] += 8
    
    # Question 20: Work environment
    env_map = {
        "Remote": ["Web Development", "UI/UX & Product Design", "Blockchain Development"],
        "Hybrid": ["Software Development", "Data Science"],
        "Office": ["Cloud Computing & DevOps", "Cybersecurity"]
    }
    if 'q20' in responses:
        for domain in env_map.get(responses['q20'], []):
            scores[domain] += 8
    
    # Calculate percentages
    max_score = max(scores.values()) if scores.values() else 1
    percentages = {domain: min(int((score / max_score) * 100), 100) for domain, score in scores.items()}
    
    # Get top 2 matches
    sorted_careers = sorted(percentages.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_careers[:2]


def render_home():
    """Render home page"""
    st.title("🎓 Career Decider – Find Your Ideal Path in Computer Science")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Welcome to Career Decider! 👋
        
        Are you a B.Tech Computer Science student confused about which career path to choose? 
        You're in the right place!
        
        **What we offer:**
        - 📝 A comprehensive 20-question assessment
        - 🎯 AI-powered career recommendations
        - 💼 Detailed insights about top CS domains
        - 📚 Personalized learning resources
        - 📊 Match confidence scores
        
        **How it works:**
        1. Answer 20 questions about your interests, skills, and preferences
        2. Get instant career recommendations based on your profile
        3. Explore detailed career paths with salary ranges and companies
        4. Download your personalized career report
        
        Take just 5-7 minutes to discover your ideal career path!
        """)
        
        if st.button("🚀 Start the Test", type="primary", use_container_width=True):
            st.session_state.page = 'test'
            st.rerun()
    
    with col2:
        st.info("""
        **📈 Career Domains We Cover:**
        - Software Development
        - Data Science
        - AI & Machine Learning
        - Cybersecurity
        - Cloud & DevOps
        - Web Development
        - UI/UX Design
        - Blockchain
        - Game Development
        - Research & Academia
        """)
        
        # Add some spacing
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Professional-looking credit under the box
        st.markdown(
            '<p style="text-align:center; color:gray; font-size:14px;"><em>Project by <strong>Aryan Bajpai</strong></em></p>',
            unsafe_allow_html=True
        )


def render_test():
    """Render test page with questions"""
    st.title("📝 Career Assessment Test")
    st.markdown("Answer all 20 questions honestly to get the best recommendations.")
    
    progress = len(st.session_state.responses) / 20
    st.progress(progress)
    st.caption(f"Progress: {len(st.session_state.responses)}/20 questions answered")
    
    with st.form("career_test"):
        st.subheader("A. Interests & Passion 🎯")
        
        q1 = st.radio("1. What kind of tasks excite you the most?",
                     ["Problem-solving", "Designing visuals", "Managing teams", 
                      "Research and innovation", "Communication or writing"],
                     key="q1_input")
        
        q2 = st.radio("2. Which subject do you enjoy the most?",
                     ["Mathematics", "Programming", "Physics", "Art/Design", "Business/Management"],
                     key="q2_input")
        
        q3 = st.radio("3. Do you enjoy competitive coding or logical puzzles?",
                     ["Yes", "No"],
                     key="q3_input")
        
        q4 = st.radio("4. Do you prefer creative design or structured logic?",
                     ["Creative design", "Structured logic"],
                     key="q4_input")
        
        q5 = st.radio("5. Would you like to work with people or machines?",
                     ["People", "Machines", "Both"],
                     key="q5_input")
        
        st.subheader("B. Skills & Technical Comfort 💻")
        
        q6 = st.slider("6. How comfortable are you with coding?", 1, 10, 5, key="q6_input")
        
        q7 = st.slider("7. How much do you enjoy mathematics?", 1, 10, 5, key="q7_input")
        
        q8 = st.slider("8. How strong are you in analytical thinking?", 1, 10, 5, key="q8_input")
        
        q9 = st.radio("9. Do you enjoy learning new programming languages?",
                     ["Yes", "No"],
                     key="q9_input")
        
        q10 = st.selectbox("10. Which technology interests you most?",
                          ["Web Development", "Data Science", "Artificial Intelligence",
                           "Cybersecurity", "Cloud Computing", "Software Engineering"],
                          key="q10_input")
        
        st.subheader("C. Work & Personality 👥")
        
        q11 = st.radio("11. Do you prefer solo work or teamwork?",
                      ["Solo work", "Teamwork"],
                      key="q11_input")
        
        q12 = st.slider("12. How important is creativity in your career?", 1, 10, 5, key="q12_input")
        
        q13 = st.radio("13. Do you like leadership roles or technical depth?",
                      ["Leadership", "Technical Expertise"],
                      key="q13_input")
        
        q14 = st.radio("14. Do you enjoy experimenting with new ideas?",
                      ["Yes", "No"],
                      key="q14_input")
        
        q15 = st.radio("15. Would you prefer building systems or analyzing data?",
                      ["Building systems", "Analyzing data"],
                      key="q15_input")
        
        st.subheader("D. Goals & Lifestyle 🎯")
        
        q16 = st.selectbox("16. What type of company would you like to work in?",
                          ["Big Tech (FAANG)", "Startups", "Research or Academia", "Government / PSU"],
                          key="q16_input")
        
        q17 = st.radio("17. What's your dream job focus?",
                      ["Innovation", "Stability", "Money", "Fame / Recognition"],
                      key="q17_input")
        
        q18 = st.radio("18. Are you open to freelancing or startups?",
                      ["Yes", "No"],
                      key="q18_input")
        
        q19 = st.slider("19. How much time can you dedicate to learning new skills weekly (hours)?",
                       0, 40, 10, key="q19_input")
        
        q20 = st.radio("20. Which work environment appeals to you most?",
                      ["Remote", "Hybrid", "Office"],
                      key="q20_input")
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            submitted = st.form_submit_button("✅ Submit & Get Results", type="primary", use_container_width=True)
        
        if submitted:
            # Save responses
            st.session_state.responses = {
                'q1': q1, 'q2': q2, 'q3': q3, 'q4': q4, 'q5': q5,
                'q6': q6, 'q7': q7, 'q8': q8, 'q9': q9, 'q10': q10,
                'q11': q11, 'q12': q12, 'q13': q13, 'q14': q14, 'q15': q15,
                'q16': q16, 'q17': q17, 'q18': q18, 'q19': q19, 'q20': q20
            }
            
            # Calculate results
            st.session_state.result = calculate_career_match(st.session_state.responses)
            st.session_state.page = 'result'
            st.rerun()

def render_result():
    """Render result page"""
    if not st.session_state.result:
        st.warning("Please take the test first!")
        if st.button("Go to Test"):
            st.session_state.page = 'test'
            st.rerun()
        return
    
    st.title("🎯 Your Career Recommendations")
    
    top_matches = st.session_state.result
    
    # Display top match
    st.success(f"### 🌟 Top Recommendation: {top_matches[0][0]}")
    st.metric("Match Score", f"{top_matches[0][1]}%", delta="Best Fit")
    
    domain_info = CAREER_DOMAINS[top_matches[0][0]]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        **📋 Description:**  
        {domain_info['description']}
        
        **🎓 Key Skills Required:**  
        {domain_info['skills']}
        
        **💰 Average Salary Range:**  
        {domain_info['salary']}
        """)
    
    with col2:
        st.markdown(f"""
        **🏢 Top Companies:**  
        {domain_info['companies']}
        
        **🔧 Subdomains:**  
        {domain_info['subdomains']}
        
        **📚 Learning Resources:**  
        {domain_info['learning_resources']}
        """)
    
    # Display second match
    if len(top_matches) > 1:
        st.info(f"### 🥈 Alternative Path: {top_matches[1][0]}")
        st.metric("Match Score", f"{top_matches[1][1]}%", delta="Good Fit")
        
        domain_info2 = CAREER_DOMAINS[top_matches[1][0]]
        
        with st.expander("View Details"):
            st.markdown(f"""
            **Description:** {domain_info2['description']}
            
            **Key Skills:** {domain_info2['skills']}
            
            **Salary Range:** {domain_info2['salary']}
            
            **Top Companies:** {domain_info2['companies']}
            
            **Learning Resources:** {domain_info2['learning_resources']}
            """)
    
    # Download report button
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("📥 Download Career Report", type="primary", use_container_width=True):
            report = generate_report(top_matches)
            st.download_button(
                label="Download as Text File",
                data=report,
                file_name=f"career_report_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain"
            )
    
    # Retake test button
    st.markdown("---")
    if st.button("🔄 Retake Test"):
        st.session_state.responses = {}
        st.session_state.result = None
        st.session_state.page = 'test'
        st.rerun()

def generate_report(matches):
    """Generate downloadable career report"""
    report = f"""
╔══════════════════════════════════════════════════════════════╗
║           CAREER DECIDER - PERSONALIZED REPORT               ║
╚══════════════════════════════════════════════════════════════╝

Generated on: {datetime.now().strftime('%B %d, %Y at %H:%M')}

════════════════════════════════════════════════════════════════

🎯 YOUR TOP CAREER RECOMMENDATIONS

════════════════════════════════════════════════════════════════

🌟 PRIMARY RECOMMENDATION: {matches[0][0]}
   Match Score: {matches[0][1]}%
   
   {CAREER_DOMAINS[matches[0][0]]['description']}
   
   📋 Subdomains: {CAREER_DOMAINS[matches[0][0]]['subdomains']}
   
   🎓 Key Skills Required:
   {CAREER_DOMAINS[matches[0][0]]['skills']}
   
   💰 Average Salary Range: {CAREER_DOMAINS[matches[0][0]]['salary']}
   
   🏢 Top Hiring Companies:
   {CAREER_DOMAINS[matches[0][0]]['companies']}
   
   📚 Recommended Learning Resources:
   {CAREER_DOMAINS[matches[0][0]]['learning_resources']}

════════════════════════════════════════════════════════════════
"""
    
    if len(matches) > 1:
        report += f"""
🥈 ALTERNATIVE PATH: {matches[1][0]}
   Match Score: {matches[1][1]}%
   
   {CAREER_DOMAINS[matches[1][0]]['description']}
   
   📋 Subdomains: {CAREER_DOMAINS[matches[1][0]]['subdomains']}
   
   🎓 Key Skills: {CAREER_DOMAINS[matches[1][0]]['skills']}
   
   💰 Salary Range: {CAREER_DOMAINS[matches[1][0]]['salary']}
   
   🏢 Companies: {CAREER_DOMAINS[matches[1][0]]['companies']}

════════════════════════════════════════════════════════════════
"""
    
    report += """
📌 NEXT STEPS:

1. Deep dive into the recommended domain through online courses
2. Build projects to showcase your skills
3. Connect with professionals in the field on LinkedIn
4. Participate in hackathons and coding competitions
5. Keep learning and stay updated with industry trends

════════════════════════════════════════════════════════════════

Good luck on your career journey! 🚀

Generated by Career Decider - Your AI Career Guidance Tool
════════════════════════════════════════════════════════════════
"""
    return report

def render_about():
    """Render about page"""
    st.title("ℹ️ About Career Decider")
    
    st.markdown("""
    ### What is Career Decider?
    
    Career Decider is an AI-powered career guidance tool specifically designed for B.Tech Computer Science students. 
    It helps you discover the most suitable career path based on your interests, skills, and preferences.
    
    ### How does it work?
    
    Our intelligent algorithm analyzes your responses to 20 carefully crafted questions covering:
    - **Interests & Passion**: What excites and motivates you
    - **Skills & Technical Comfort**: Your technical abilities and learning preferences
    - **Work & Personality**: Your work style and personality traits
    - **Goals & Lifestyle**: Your career aspirations and lifestyle preferences
    
    The system then matches your profile against 10 major Computer Science career domains and provides 
    personalized recommendations with confidence scores.
    
    ### Career Domains Covered
    
    We provide guidance on the following career paths:
    """)
    
    cols = st.columns(2)
    domains_list = list(CAREER_DOMAINS.keys())
    
    for idx, domain in enumerate(domains_list):
        with cols[idx % 2]:
            st.info(f"**{domain}**\n\n{CAREER_DOMAINS[domain]['description']}")
    
    st.markdown("""
### Why Trust Career Decider?

- ✅ **Data-Driven**: Based on industry trends and real career paths
- ✅ **Comprehensive**: Covers all major CS career domains
- ✅ **Personalized**: Tailored recommendations based on your unique profile
- ✅ **Actionable**: Provides specific resources and next steps
- ✅ **Free**: Completely free to use with no hidden charges

### About the Creator

Created with ❤️ for CS students to make informed career decisions.  
Created by Aryan Bajpai

---

**Disclaimer**: This tool provides guidance based on your inputs. Final career decisions should consider 
multiple factors including market trends, personal circumstances, and professional advice.
""")


# Main app logic
def main():
    # Sidebar navigation
    with st.sidebar:
        st.title("🧭 Navigation")
        
        menu_items = {
            "🏠 Home": "home",
            "📝 Take the Test": "test",
            "🎯 Career Result": "result",
            "ℹ️ About": "about"
        }
        
        for label, page in menu_items.items():
            if st.button(label, use_container_width=True, 
                        type="primary" if st.session_state.page == page else "secondary"):
                st.session_state.page = page
                st.rerun()
        
        st.markdown("---")
        st.markdown("""
        ### 📊 Quick Stats
        - **10** Career Domains
        - **20** Assessment Questions
        - **100%** Free
        
        ### 💡 Tips
        - Answer honestly
        - Take your time
        - No right/wrong answers
        """)
    
    # Render appropriate page
    if st.session_state.page == 'home':
        render_home()
    elif st.session_state.page == 'test':
        render_test()
    elif st.session_state.page == 'result':
        render_result()
    elif st.session_state.page == 'about':
        render_about()

if __name__ == "__main__":
    main()