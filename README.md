# 🎓 Career Decider - AI-Powered Career Guidance Tool

An interactive Streamlit web application designed to help B.Tech Computer Science students discover their ideal career path through a comprehensive 20-question assessment.

![Career Decider](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 🌟 Features

- **20 Structured Questions**: Comprehensive assessment covering interests, skills, personality, and goals
- **10 Career Domains**: Detailed coverage of major CS career paths
- **AI-Powered Matching**: Intelligent algorithm that calculates career match scores
- **Personalized Reports**: Downloadable career report with recommendations
- **Clean UI**: Professional, responsive design with easy navigation
- **Detailed Insights**: Salary ranges, required skills, top companies, and learning resources

## 📋 Career Domains Covered

1. **Software Development** - Backend, Frontend, Full-Stack, DevOps
2. **Data Science** - Data Analysis, Engineering, Business Intelligence
3. **Artificial Intelligence & Machine Learning** - Deep Learning, NLP, Computer Vision
4. **Cybersecurity** - Ethical Hacking, Network Security, Cloud Security
5. **Cloud Computing & DevOps** - AWS, Azure, GCP, CI/CD
6. **Web Development** - Frontend, Backend, Full Stack
7. **UI/UX & Product Design** - Visual Design, UX Research, Prototyping
8. **Blockchain Development** - Smart Contracts, DApps, DeFi
9. **Game Development** - Unity, Unreal Engine, AR/VR
10. **Research & Academia** - AI Research, Quantum Computing, Education



## 📁 Project Structure

```
career-decider/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .streamlit/
│   └── config.toml            # Streamlit theme configuration
└── .gitignore                 # Git ignore file
```

## 🎯 How It Works

### 1. Assessment Process
Users answer 20 questions divided into 4 categories:
- **A. Interests & Passion** (5 questions)
- **B. Skills & Technical Comfort** (5 questions)
- **C. Work & Personality** (5 questions)
- **D. Goals & Lifestyle** (5 questions)

### 2. Scoring Algorithm
The app uses a weighted scoring system that:
- Analyzes responses across all 20 questions
- Assigns weights based on question importance
- Calculates match scores for each career domain
- Returns top 2 career recommendations with confidence percentages

### 3. Result Display
- **Primary Recommendation**: Best-fit career with highest match score
- **Alternative Path**: Second-best option for consideration
- **Detailed Information**: Skills, salary ranges, companies, learning resources
- **Downloadable Report**: Text-based career report



### Home Page
The landing page welcomes users and explains the assessment process.

### Assessment Test
Interactive questionnaire with progress tracking and various input types (radio buttons, sliders, dropdowns).

### Results Page
Personalized career recommendations with match scores, skills needed, salary information, and learning resources.

## 🛠️ Technologies Used

- **Streamlit**: Web application framework
- **Python**: Core programming language
- **Pandas**: Data manipulation
- **NumPy**: Numerical computations



### Environment Variables
No environment variables or API keys required - the app runs entirely on user inputs.

## 📊 Assessment Categories

### A. Interests & Passion
- Task preferences (problem-solving, design, management, etc.)
- Subject enjoyment (mathematics, programming, physics, etc.)
- Competitive coding interest
- Creative vs. structured preferences
- People vs. machines orientation

### B. Skills & Technical Comfort
- Coding comfort level (1-10 scale)
- Mathematics enjoyment (1-10 scale)
- Analytical thinking strength (1-10 scale)
- Programming language learning enthusiasm
- Technology area of interest

### C. Work & Personality
- Solo vs. teamwork preference
- Creativity importance (1-10 scale)
- Leadership vs. technical expertise
- Experimentation enthusiasm
- Building vs. analyzing preference

### D. Goals & Lifestyle
- Company type preference (Big Tech, Startups, Research, Government)
- Dream job focus (Innovation, Stability, Money, Recognition)
- Freelancing openness
- Weekly learning time commitment (0-40 hours)
- Work environment preference (Remote, Hybrid, Office)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request



## 📝 License

This project is licensed under the MIT License. 

## 👨‍💻 Author

Created with ❤️ for CS students by Aryan bajpai

## 🙏 Acknowledgments

- Career domain information compiled from industry research
- Salary ranges based on Indian tech industry standards (2024-2025)
- Learning resources curated from popular online platforms

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the documentation

## 🔮 Future Enhancements

- [ ] Add data visualization for results (bar charts, radar charts)
- [ ] Implement career path comparison feature
- [ ] Add success stories from each domain
- [ ] Include video resources and tutorials
- [ ] Create mobile-responsive design improvements
- [ ] Add export to PDF feature
- [ ] Implement user accounts and result history
- [ ] Add career roadmap visualization
- [ ] Include industry trends and growth projections
- [ ] Add mentor connection feature

## ⚠️ Disclaimer

This tool provides career guidance based on user inputs and predefined criteria. It should be used as one of many resources in making career decisions. Always consider:
- Current market trends
- Personal circumstances
- Professional advice from career counselors
- Industry-specific requirements
- Regional job market conditions

---

**Made with Streamlit** | **Python 3.8+** | **Open Source**


⭐ Star this repository if you find it helpful!
