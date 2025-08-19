import streamlit as st
from pathlib import Path
import base64

# Path Setup
current_path = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_path = current_path/"styles"/"main.css"
resume_path = current_path/"assets"/"Dhumale_Prasad_Resume.pdf"
profile_pic_path = current_path/"assets"/"profile pic.jpg"

# Configuration
page_title = "Prasad's Portfolio"
page_icon = "👨‍💻"
name = "Dhumale Prasad"
description = """Tech enthusiast and AI developer with a passion for creating innovative solutions. 
Skilled in machine learning, natural language processing, and software development."""
email = "dhumaleprasad04@gmail.com"

# Social Media Links with Icons and Colors
social_media = {
    "LinkedIn": {
        "link": "https://www.linkedin.com/in/prasad-dhumale-aa1032261/",
        "icon": "linkedin",
        "color": "#0077B5"
    },
    "GitHub": {
        "link": "https://github.com/DhumalePrasad04",
        "icon": "github",
        "color": "#333333"
    },
    "Twitter": {
        "link": "https://x.com/DhumaleTiku",
        "icon": "twitter",
        "color": "#1DA1F2"
    }
}

# Projects with Detailed Information
projects = {
    "CoTrue": {
        "link": "https://github.com/DhumalePrasad04/COtrue",
        "description": "An AI-powered fact-checking application that verifies information using natural language processing and trustworthy sources.",
        "tech": ["Python", "NLP", "Machine Learning"]
    },
    "CoTrue 2.0": {
        "link": "https://github.com/DhumalePrasad04/CoTrue-2.0",
        "description": "Enhanced version with improved accuracy, real-time verification, and multi-source validation algorithms.",
        "tech": ["Python", "Deep Learning", "Web APIs"]
    },
    "Speech/Text to Sign": {
        "link": "https://github.com/DhumalePrasad04/Speech-or-Text-to-Sign-conversion",
        "description": "Accessibility tool that translates spoken or written language into sign language using computer vision techniques.",
        "tech": ["Computer Vision", "NLP", "React"]
    },
    "Stock Analysis": {
        "link": "https://github.com/DhumalePrasad04/secure-world",
        "description": "Advanced stock market analysis tool that predicts trends using historical data and machine learning models.",
        "tech": ["Python", "ML", "Time Series Analysis"]
    },
    "Local Chatbot": {
        "link": "https://github.com/DhumalePrasad04/Local-Chatbot-jarvis-",
        "description": "Privacy-focused AI assistant that runs locally without requiring internet connectivity.",
        "tech": ["Python", "NLP", "TensorFlow"]
    }
}

# Education Information
education = [
    {
        "degree": "B. Tech in Computer Science and Engineering",
        "institution": "REVA UNIVERSITY",
        "period": "2022-2026",
        "score": "CGPA: 9.25 (up to 5th Semester)"
    },
    {
        "degree": "Senior Secondary",
        "institution": "Diamond Independent P U College, Bhalki",
        "period": "2020-2022",
        "score": "Percentage: 94.5%"
    },
    {
        "degree": "Higher Secondary",
        "institution": "Geetha High School Chegunta",
        "period": "2019-2020",
        "score": "CGPA: 10.0"
    }
]

# Achievements
achievements = [
    "4x Hackathon winner 🏆",
    "Winner at HackHorizon 1.0",
    "Winner at HackHorizon 2.0",
    "Winner under the Track of Best use of AI in Stocks",
    "Secured 2nd Prize in the AI/ML Track at BLITZ'24"
]

# Skills
skills = {
    "Programming Languages": ["Python", "Java", "C"],
    "AI/ML": [ "scikit-learn", "NLP"],
    "Web Development": ["FastApi", "Flask", "Streamlit"],
    "Data Analysis": ["Pandas", "NumPy", "Matplotlib", "SQL"],
    "Tools": ["Git", "Docker", "VS Code", "Jupyter"]
}

# Function to read and encode images for custom HTML
def get_img_as_base64(file_path):
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Page Configuration
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")

# Load CSS
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load Resume
with open(resume_path, "rb") as pdf_file:
    pdf_data = pdf_file.read()

# Header Section
st.markdown("""
<div class="header animate-fadeIn">
    <h1>Prasad's Portfolio</h1>
    <p>AI Developer | CS Student | Innovator</p>
</div>
""", unsafe_allow_html=True)

# Profile Section
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown(f"""
    <div class="animate-fadeIn" style="text-align: center;">
        <img src="data:image/jpg;base64,{get_img_as_base64(profile_pic_path)}" 
             class="profile-image" width="230px">
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="profile-info animate-fadeIn">
        <h2>{name}</h2>
        <p class="profile-description">{description}</p>
        <p><i class="fas fa-envelope"></i> {email}</p>
    </div>
    """, unsafe_allow_html=True)

    # Download Button
    st.download_button(
        label="📄 Download Resume",
        data=pdf_data,
        file_name=resume_path.name,
        mime="application/octet-stream",
        key="resume-download",
    )

# Social Media Section - Single Row
st.markdown("""
<div class="social-media-section animate-fadeIn">
    <h2 class="social-media-title">Connect With Me</h2>
    <div class="social-links-row">
""", unsafe_allow_html=True)

for platform, info in social_media.items():
    st.markdown(f"""
    <div class="social-icon-wrapper">
        <a href="{info['link']}" target="_blank" class="social-icon-link">
            <i class="fab fa-{info['icon']}" style="color: {info['color']};"></i>
            <span>{platform}</span>
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# Education Section
st.markdown("""
<div class="section animate-fadeIn">
    <h2 class="section-title">Education</h2>
""", unsafe_allow_html=True)

for item in education:
    st.markdown(f"""
    <div class="education-item">
        <div class="education-title">{item['degree']}</div>
        <div class="education-institution">{item['institution']} | {item['period']}</div>
        <div class="education-date">{item['score']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Skills Section
st.markdown("""
<div class="section animate-fadeIn">
    <h2 class="section-title">Skills</h2>
    <div class="skills-container">
""", unsafe_allow_html=True)

for category, skill_list in skills.items():
    skill_tags = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skill_list])
    st.markdown(f"""
    <div class="skill-category">
        <h3 class="skill-category-title">{category}</h3>
        <div class="skill-tags">{skill_tags}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# Achievements Section
st.markdown("""
<div class="section animate-fadeIn">
    <h2 class="section-title">Achievements</h2>
    <ul class="achievement-list">
""", unsafe_allow_html=True)

for achievement in achievements:
    st.markdown(f"""
    <li class="achievement-item">{achievement}</li>
    """, unsafe_allow_html=True)

st.markdown("</ul></div>", unsafe_allow_html=True)

# Projects Section
st.markdown("""
<div class="section animate-fadeIn">
    <h2 class="section-title">Projects</h2>
    <div class="projects-grid">
""", unsafe_allow_html=True)

for project_name, project_info in projects.items():
    # Create tech tags HTML
    tech_tags = ""
    for tech in project_info['tech']:
        tech_tags += f'<span class="tech-tag">{tech}</span>'

    st.markdown(f"""
    <div class="project-card">
        <div class="project-header">
            <h3 class="project-name">{project_name}</h3>
        </div>
        <div class="project-content">
            <p class="project-description">{project_info['description']}</p>
            <div class="tech-tags">{tech_tags}</div>
        </div>
        <div class="project-footer">
            <a href="{project_info['link']}" class="project-link" target="_blank">
                View on GitHub <i class="fas fa-external-link-alt"></i>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# Add Font Awesome for icons and Google Fonts
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# Add custom animation scripts
st.markdown("""
<script>
    document.addEventListener('DOMContentLoaded', (event) => {
        const animatedElements = document.querySelectorAll('.animate-fadeIn');
        animatedElements.forEach((element, index) => {
            setTimeout(() => {
                element.style.opacity = 1;
            }, index * 200);
        });
    });
</script>
""", unsafe_allow_html=True)