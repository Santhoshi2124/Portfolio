import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import base64
from io import BytesIO

# Utility to convert image to base64
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

# Set Streamlit page config
st.set_page_config(page_title="Santhoshimaa M.K | Portfolio",page_icon="👩‍💻", layout="wide")

# Background image setup
with open("bg_dark.jpeg", "rb") as bg_file:
    bg_base64 = base64.b64encode(bg_file.read()).decode()



image = Image.open("profile.jpeg")
img_base64 = image_to_base64(image)

st.markdown(f"""
<div class="profile-card">
  <img src='data:image/jpeg;base64,{img_base64}' class="profile-pic"/>
  <p class="profile-name">Santhoshimaa<br>(B.E In ISE)</p>
</div>

<style>
.profile-card {{
    position: fixed;
    top: 70px;
    right: 20px;
    width: 180px;
    padding: 12px;
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px);
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    z-index: 100;
    text-align: center;
}}

.profile-pic {{
    width: 100%;
    border-radius: 12px;
    margin-bottom: 8px;
}}

.profile-name {{
    color: #ddd;
    font-size: 13px;
}}

@media only screen and (max-width: 768px) {{
    .profile-card {{
        position: static;
        margin: 20px auto;
        width: 60%;
    }}
}}
</style>
""", unsafe_allow_html=True)


st.markdown(f"""
            
    <style>
            
            
            
        .stApp {{
            background-image: url("data:image/jpeg;base64,{bg_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        
        
        .block-container {{
            padding-top: 40px;
            padding-right: 160px;
        }}
        h1, h2, h3, h4, h5, h6, p, span, li, .markdown-text-container {{
            color: white !important;
        }}
        a {{
            color: #4dd0e1 !important;
        }}
        
        
    </style>
    
""", unsafe_allow_html=True)
st.markdown("""
    <style>
    
    .project-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 16px 40px rgba(0, 255, 255, 0.25);
    }
    span:hover {
        transform: scale(1.05);
        transition: 0.2s ease;
    }
    summary {
        transition: all 0.3s ease-in-out;
        cursor: pointer;
    }

    summary:hover {
        color: #00cfff;
        transform: scale(1.03);
        text-shadow: 0 0 6px rgba(0, 207, 255, 0.5);
    }
             h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)




# Header

st.markdown("""
<h3 style='
    font-size: 40px;
    font-weight: 600;
    color: white;
    text-shadow: 0 0 10px rgba(0, 204, 255, 0.8);
    margin-bottom: 10px;
'>👩‍💻 Santhoshimaa M.K</h3>
""", unsafe_allow_html=True)
st.markdown("<h4 style='color: gray;'>3rd Year Information Science Student | Developer | Tech Enthusiast</h4>", unsafe_allow_html=True)

# Contact

st.markdown("""
<h3 style='
    font-size: 18px;
    font-weight: 600;
    color: white;
    text-shadow: 0 0 4px rgba(0, 204, 255, 0.4);
    margin-bottom: 10px;
'>📫 Email : santoshimk2004@gmail.com</h3>
""", unsafe_allow_html=True)
st.markdown("""
<h3 style='
    font-size: 18px;
    font-weight: 600;
    color: white;
    text-shadow: 0 0 4px rgba(0, 204, 255, 0.4);
    margin-bottom: 10px;
'>📱 Phone : +91 7904286729</h3>
""", unsafe_allow_html=True)
st.markdown("""
<div style='
    font-size: 18px;
    font-weight: 600;
    color: white;
    text-shadow: 0 0 4px rgba(0, 204, 255, 0.4);
    margin-bottom: 10px;
'>
    🔗 <a href='https://www.linkedin.com/in/santhoshi-mk-47379725b' target='_blank' style='color: #4dd0e1; text-decoration: none;'>LinkedIn</a> |
    💻 <a href='https://github.com/Santhoshi2124' target='_blank' style='color: #4dd0e1; text-decoration: none;'>GitHub</a>
</div>
""", unsafe_allow_html=True)
with open("Santhoshimaa_Resume.pdf", "rb") as file:
    resume_bytes = file.read()
    resume_b64 = base64.b64encode(resume_bytes).decode()

    st.markdown(f"""
        <style>
                
        .angled-resume-button {{
            background: linear-gradient(135deg, #1a2c40, #223b58);
            color: white;
            padding: 12px 28px;
            border: none;
            font-size: 15px;
            font-weight: 500;
            text-decoration: none;
            display: inline-block;
            clip-path: polygon(8% 0%, 92% 0%, 100% 30%, 100% 70%, 92% 100%, 8% 100%, 0% 70%, 0% 30%);
            box-shadow: 0 8px 24px rgba(0, 255, 255, 0.15);
            transition: all 0.3s ease;
        }}
        .angled-resume-button:hover {{
            background: linear-gradient(135deg, #223b58, #1a2c40);
            transform: scale(1.05);
            box-shadow: 0 10px 30px rgba(0, 255, 255, 0.25);
        }}
        </style>
        <a href="data:application/octet-stream;base64,{resume_b64}" download="Santhoshimaa_Resume.pdf" target="_blank">
            <div class="angled-resume-button">📄 Resume</div>
        </a>
    """, unsafe_allow_html=True)
st.markdown("""
<hr style='
    border: none;
    height: 1.2px;
    background: linear-gradient(to right, #77cfd6, #a7dde0, #77cfd6);
    margin: 30px 0;
    opacity: 0.5;
    border-radius: 10px;
'>
""", unsafe_allow_html=True)



col1, col2 = st.columns(2)
st.markdown("""
<h3 id='career-objective' style='
    font-size: 26px;
    font-weight: 600;
    color: white;
    text-shadow: 0 0 10px rgba(0, 204, 255, 0.8);
    margin-bottom: 10px;
'>🎯 Career Objective</h3>
""", unsafe_allow_html=True)
st.markdown("""
    <div style='
        background: rgba(240, 242, 246, 0.08);
        backdrop-filter: blur(10px);
        border-left: 4px solid #4dd0e1;
        padding: 20px;
        border-radius: 12px;
        color: white;
        font-size: 16px;
        font-style: italic;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        text-align: justify;
    '>
        “Passionate 3rd year engineering student skilled in full-stack web development and real-world applications. 
        Eager to solve meaningful problems and collaborate in fast-paced environments.”
    </div>
    """, unsafe_allow_html=True)
st.markdown("""
<hr style='
    border: none;
    height: 1.2px;
    background: linear-gradient(to right, #77cfd6, #a7dde0, #77cfd6);
    margin: 30px 0;
    opacity: 0.5;
    border-radius: 10px;
'>
""", unsafe_allow_html=True)



st.markdown("""
<h3 style='
    font-size: 26px;
    font-weight: 600;
    color: white;
    text-shadow: 0 0 10px rgba(0, 204, 255, 0.8);
    margin-bottom: 10px;
'>🎓 Education</h3>
""", unsafe_allow_html=True)
st.markdown("""
    <div style='
                display: flex;
                flex-direction: column;
                gap: 16px;
                color: white;
        '>
    <div style='
                background: rgba(255,255,255,0.08);
                backdrop-filter: blur(8px);
                padding: 15px;
                border-left: 4px solid #4dd0e1;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        '>
                <b>B.E In Information Science And engineering(Pursuing)</b><br>
                CMR Institute Of Technology  CGPA-8.41 <span style='float: right;'><i>(2026)</i></span>
            </div>

    <div style='
                background: rgba(255,255,255,0.08);
                backdrop-filter: blur(8px);
                padding: 15px;
                border-left: 4px solid #4dd0e1;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        '>
                <b>PU (PCMC)</b><br>
                Gopalan PU College-92.66% <span style='float: right;'><i>(2022)</i></span>
            </div>

    <div style='
                background: rgba(255,255,255,0.08);
                backdrop-filter: blur(8px);
                padding: 15px;
                border-left: 4px solid #4dd0e1;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            '>
                <b>10th Grade</b><br>
                Cambridge School-90% <span style='float: right;'><i>(2020)</i></span>
    </div>

    </div>
        """, unsafe_allow_html=True)

st.markdown("""
<hr style='
    border: none;
    height: 1.2px;
    background: linear-gradient(to right, #77cfd6, #a7dde0, #77cfd6);
    margin: 30px 0;
    opacity: 0.5;
    border-radius: 10px;
'>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.block-container {
    padding-top: 40px !important;
    padding-right: 160px;
}

/* 👇 Add this for mobile responsiveness */
@media only screen and (max-width: 768px) {
    .block-container {
        padding-top: 70px !important;
        padding-right: 20px !important;
        padding-left: 20px !important;
    }
}
@media only screen and (max-width: 768px) {
    .profile-pic {
        border-radius: 50%;
        width: 120px;
        height: 120px;
        object-fit: cover;
    }
}
@media only screen and (max-width: 768px) {
    .element-container > div[data-testid="column"] {
        width: 100% !important;
        flex: 1 1 100% !important;
        max-width: 100% !important;
    }
}
html {
    scroll-behavior: smooth;
}


</style>
""", unsafe_allow_html=True)




# Project data
project_cards = [
    {
        "emoji": "🎒",
        "title": "Chimudra Fee Tracker",
        "tech_tags": ["Node.js", "Express.js", "MongoDB", "HTML", "CSS", "JavaScript"],
        "desc": "Built a secure full-stack fee management system for educational institutions. It supports real-time fee tracking, role-based login, and seamless data operations using Node.js, Express.js, and MongoDB. The responsive frontend enables easy navigation, while backend APIs ensure reliable and secure deployment. Designed to simplify school and coaching center operations.",
        "details": [
            "Implemented secure login with role-based access control for admin and staff.",
            "Designed RESTful APIs to manage fee records and student data.",
            "Integrated environment-based deployment using .env for security.",
            "Developed a responsive frontend for real-time fee updates and smooth navigation."
        ]
    },
    {
        "emoji": "🛍️",
        "title": "Mobile Accessories Web App",
        "tech_tags": ["HTML", "CSS", "Node.js", "Express.js", "MongoDB", "Mapbox API"],
        "desc": "Developed a product management web app for mobile accessories with full CRUD functionality. Built using Node.js, Express.js, and MongoDB, it features a user-friendly interface and secure, modular backend with middleware-based validation. Showcases strong backend skills, API integration, and scalable deployment in an e-commerce-like environment.",
        "details": [
            "Built CRUD operations for product listing and inventory tracking.",
            "Used middleware for request validation and modular routing in Express.js.",
            "Integrated Mapbox API to visualize delivery locations on an interactive map.",
            "Employed environment configuration for scalable deployment."
        ]
    },
    {
        "emoji": "♻️",
        "title": "Used Cloth Processing System",
        "tech_tags": ["HTML", "CSS", "JavaScript", "Python", "Flask",  "REST API", "SQLite"],
        "desc": "Built a full-stack cloth donation tracking system with user authentication and real-time form submission. Developed using Flask, SQLite, and AJAX for smooth, asynchronous interactions. Enables secure entry and monitoring of donor data through a clean UI. Highlights REST API design, state management, and full-stack development for NGO and small-scale inventory use cases.",
        "details": [
            "Developed user login and donor tracking dashboard with Flask.",
            "Enabled real-time form submission using AJAX for a smooth UX.",
            "Designed REST APIs for handling donor data and item entries.",
            "Stored data in SQLite for lightweight, efficient access."
        ]
    },
    {
        "emoji": "🧠",
        "title": "Alzheimer’s Disease Classifier (In Progress)",
        "tech_tags": ["Python", "TensorFlow", "Keras", "scikit-learn"],
        "desc": "Collaborating on a machine learning model to classify Alzheimer’s stages (CN, MCI, AD) using genome-wide expression data. Leveraging transfer learning, dimensionality reduction, and deep learning to improve accuracy on limited biomedical datasets. Focused on early diagnosis support through AI-driven genomic analysis.",
        "details": [
            "Applying transfer learning to handle limited medical data.",
            "Preprocessing genome-wide data for cleaner inputs and feature reduction.",
            "Fine-tuning deep learning models for multi-class classification (CN, MCI, AD).",
            "Exploring gene markers to enhance clinical insight and accuracy."
        ]
    }
]

# Projects Section
st.markdown("""
<h3 id='projects' style='
    font-size: 26px;
    font-weight: 600;
    color: white;
    text-shadow: 0 0 10px rgba(0, 204, 255, 0.8);
    margin-bottom: 10px;
'>💡 Projects</h3>
""", unsafe_allow_html=True)



for i in range(0, len(project_cards), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(project_cards):
            proj = project_cards[i + j]

            tech_tags = " ".join([
                f"<span style='background-color:#1e3a5f; color:#fff; padding:4px 10px; border-radius:12px; margin-right:6px; font-size:13px;'>{t}</span>"
                for t in proj["tech_tags"]
            ])

            detail_list = ''.join([f"<li>{bullet}</li>" for bullet in proj['details']])

            html_block = f"""
            <div style='
            background: rgba(255,255,255,0.07);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255,255,255,0.15);
            padding: 30px 25px;
            border-radius: 18px;
            margin: 20px 0;
            box-shadow: 0 12px 32px rgba(0,0,0,0.35);
            transition: all 0.3s ease-in-out;
            color: white;
            ' class='project-card'>
            <h3 style='margin-bottom: 10px;'>{proj['emoji']} {proj['title']}</h3>
            <p style='font-size: 15px; margin-bottom: 15px;'>{proj['desc']}</p>
            <p style='font-size: 15px;'><b style='color: white;'>Tech Stack:</b> {tech_tags}</p>
            <details style='
            background-color: rgba(255,255,255,0.09);
            color: white;
            padding: 12px 16px;
            border-radius: 12px;
            margin-top: 18px;
            font-size: 14px;
            '>
            <summary style='font-weight: bold; font-size: 15px;'>🔍 View Details</summary>
            <ul style='margin-top: 10px;'>{detail_list}</ul>
            </details>
            </div>
            """

            with cols[j]:
                st.markdown(html_block, unsafe_allow_html=True)
st.markdown("""
<hr style='
    border: none;
    height: 1.2px;
    background: linear-gradient(to right, #77cfd6, #a7dde0, #77cfd6);
    margin: 30px 0;
    opacity: 0.5;
    border-radius: 10px;
'>
""", unsafe_allow_html=True)

 
    # Technical Skills
st.markdown("""
<h3 id='technical-skills' style='
    font-size: 26px;
    font-weight: 600;
    color: white;
    text-shadow: 0 0 10px rgba(0, 204, 255, 0.8);
    margin-bottom: 10px;
'> 🛠️ Technical Skills</h3>
""", unsafe_allow_html=True)
st.markdown("""
    - **Languages**: C, Java, Python:DataStructure(Java)
    - **Web Technologies**: HTML, CSS, JavaScript
    - **Frameworks & Libraries**: Node.js, Express.js, React.js  , Flask
    - **Database**: MySQL, MongoDB  
    - **Tools**: VS Code, Power BI, Tableau, Git, LaTeX, Jupyter , Colab , Eclipse , Excel. 
    - **DevOps**: Jenkins, Gradle, Maven, Azure Pipelines (Basics)  
    - **OS**: Windows, Ubuntu
    - **Version Control**:Git , GitHub
    """)
st.markdown("""
<hr style='
    border: none;
    height: 1.2px;
    background: linear-gradient(to right, #77cfd6, #a7dde0, #77cfd6);
    margin: 30px 0;
    opacity: 0.5;
    border-radius: 10px;
'>
""", unsafe_allow_html=True)


# Achievements
st.markdown("""
<h3 id='co-curricular' style='
    font-size: 26px;
    font-weight: 600;
    color: white;
    text-shadow: 0 0 10px rgba(0, 204, 255, 0.8);
    margin-bottom: 10px;
'> 🎨Co-Curricular Activities & Hobbies</h3>
""", unsafe_allow_html=True)
st.markdown("""
    - 🧠 Filed 2 patents (Innovative bottle Design, Ergonomic Mouse Glove)  
    - 👩‍💻 Hackathon participant @ Areta 360  
    - 💡 Proposed HER-Guard to Yukti Repository : Recommended In the First Stage
    - 📚 Certifications : Java + DSA, Full Stack Web Dev (Udemy)  
    - ⚙️ Attended DevOps CI/CD Tools seminar  
    - 🧡 NSS: orphanage outreach & water conservation visits  
    - 🏸 Sports: Badminton, Table Tennis, Throw Ball
    - 🗣️ Languages : English, Kannada, Hindi, Telugu, Tamil, Sourashtra 
    - 🍳 Hobbies : Cooking, Dancing, Painting, Travelling, Singing, Photo/Video Editing
    """)

st.markdown("""
<hr style='
    border: none;
    height: 1.2px;
    background: linear-gradient(to right, #77cfd6, #a7dde0, #77cfd6);
    margin: 30px 0;
    opacity: 0.5;
    border-radius: 10px;
'>
""", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: white;'>Built with ❤️ by Santhoshimaa | LinkedIn-Ready & Recruiter-Friendly</div>", unsafe_allow_html=True)

