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
st.markdown("<h4 style='color: gray;'>4th Year Information Science Student | Developer | Tech Enthusiast</h4>", unsafe_allow_html=True)

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
        “Passionate 4th year engineering student skilled in full-stack web development and real-world applications. 
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
                CMR Institute Of Technology  CGPA-8.47 <span style='float: right;'><i>(2026)</i></span>
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
  "emoji": "🍽️",
  "title": "ToshiTadka – AI-Enhanced Food Delivery Platform",
  "tech_tags": ["MongoDB", "Express.js", "React", "Node.js", "Gemini AI", "REST API", "Context API"],
  "desc": "Developed a full-stack food delivery platform with AI-powered personalization. Features include restaurant browsing, a persistent cart, secure backend APIs, and smart Gemini AI integrations for food recommendations and conversational assistance.",
  "details": [
    "Built a responsive MERN-based platform with dynamic restaurant listings and a persistent shopping cart using React Context API.",
    "Engineered robust RESTful APIs to manage users, restaurants, orders, and cart data in MongoDB.",
    "Integrated Gemini AI to create a ‘Cravings Solver’ that converts natural-language cravings into dish recommendations.",
    "Developed an interactive ‘Foodie Friend’ chatbot for food discovery assistance and real-time order status updates.",
    "Implemented secure data handling, smooth frontend routing, and a scalable backend for reliable performance."
  ]
}
,
    {
  "emoji": "📱",
  "title": "Cart-Enabled Mobile Accessories Web Platform",
  "tech_tags": ["HTML", "CSS", "JavaScript", "Node.js", "Express.js", "MongoDB", "Mapbox API"],
  "desc": "Developed a full-stack platform for browsing and managing mobile accessories with secure authentication, smooth cart functionality, and integrated shop location mapping using Mapbox.",
  "details": [
    "Designed and implemented backend services using Node.js and Express.js with full CRUD operations for products and users.",
    "Integrated secure user authentication and product upload functionality to support real-world retail workflows.",
    "Utilized MongoDB for structured storage of product, user, and inventory data.",
    "Implemented Mapbox API to display shop locations, enhancing user interaction and store discovery.",
    "Built a responsive frontend using HTML, CSS, and JavaScript with a clean product catalog and smooth cart flow.",
    "Focused on scalable backend routing, inventory management logic, and overall usability for an efficient shopping experience."
  ]
}
,
    {
  "emoji": "👕",
  "title": "ClothCycle – Used Cloth Management Platform",
  "tech_tags": ["Python", "Flask", "SQLite", "SQLAlchemy", "HTML", "CSS", "Bootstrap"],
  "desc": "Developed a full-stack platform to manage the intake, tracking, and distribution of donated clothing with secure authentication, structured data management, and an interactive admin dashboard.",
  "details": [
    "Implemented secure user authentication using Flask-Login with session handling and password hashing for data protection.",
    "Designed structured donation forms to capture cloth type, condition, quantity, and donor details, storing all entries using SQLAlchemy ORM.",
    "Created an admin dashboard for streamlined viewing of records, updating donation status across stages, and managing outdated or duplicate entries.",
    "Developed a responsive frontend with Bootstrap and Jinja2 templates for an intuitive and clean user experience.",
    "Ensured scalability for future features including NGO collaboration modules, analytics dashboards, and extended distribution workflows."
  ]
}
,
    {
  "emoji": "🧬",
  "title": "Alzheimer’s Disease Classification System",
  "tech_tags": ["Python", "Transfer Learning", "Machine Learning", "Gene Expression Data", "Flask/Streamlit", "Pandas", "NumPy"],
  "desc": "Built an AI-powered system for classifying Alzheimer’s disease using gene expression data with transfer learning, supported by an interactive web interface for predictions and educational assistance.",
  "details": [
    "Applied transfer learning on genome-wide gene expression datasets to classify Alzheimer’s disease with improved accuracy and reduced training time.",
    "Designed complete workflows for preprocessing, feature extraction, model training, evaluation, and prediction.",
    "Developed an interactive web interface using Streamlit/Flask to allow users to upload data and receive real-time classification outputs.",
    "Integrated a knowledge-based chatbot to deliver Alzheimer’s awareness, symptom information, and care guidelines.",
    "Implemented visualization components for gene distributions, prediction confidence, and model performance metrics.",
    "Ensured modular, extensible system architecture for future enhancements such as multi-class classification and clinical dataset integration."
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
    - **Tools**: VS Code, Figma, Power BI, Tableau, Git, LaTeX, Jupyter , Colab , Eclipse , Excel. 
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
st.markdown("<div style='text-align: center; color: white;'>Built with ❤️ by Santhoshimaa</div>", unsafe_allow_html=True)

