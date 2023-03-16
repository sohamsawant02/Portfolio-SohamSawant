import streamlit as st
from PIL import Image

resume_file = "assets/Resume-Soham Sawant.pdf"
profile_pic = "assets/SohamDP.png"

PAGE_TITLE = "Portfolio-Soham Sawant"
SOCIAL_MEDIA = {
    "LinkedIn": "https://in.linkedin.com/in/soham-anant-sawant/",
    "GitHub": "https://github.com/sohamsawant02",
    "Twitter": "https://twitter.com/SohamSawant02",
    "Hackerrank": "https://www.hackerrank.com/sohamsawant2000"
}
PROJECTS = {
    "🎓 VIT Alumni Connect | TechStack: HTML, CSS, JS, PHP, MySQL": "https://github.com/sohamsawant02/VIT-Alumni-Directory",
    "🏏 My SportSpace | TechStack: HTML, Bootstrap, JS, PHP, MySQL": "https://github.com/sohamsawant02/MySportSpace",
    "🧑‍💼 Employee Leave Management | TechStack: Java (Swing), MySQL": "https://github.com/sohamsawant02/Employee-Leave-Management",
    "📚 Library Management System | TechStack: Java": "https://github.com/sohamsawant02/Library-Management-System"
}

CERTIFICATIONS ={
    "🥇 API Fundamentals Student Expert | Postman" : "https://badgr.com/public/assertions/rfVa5KaITcWjhIuV9mu-YA?identity__email=sohamsawant2000%40gmail.com",
    "🥇 SQL Certification | Hackerrank" : "https://www.hackerrank.com/certificates/a1731075d143",
    "🥇 Python Programming | Coursera" : "https://www.coursera.org/account/accomplishments/certificate/BG9QE8TDD6L7",
    "🥇 PHP Programming | Simplilearn" : "https://www.simplilearn.com/skillup-certificate-landing?token=eyJjb3Vyc2VfaWQiOiIxOTY4IiwiY2VydGlmaWNhdGVfdXJsIjoiaHR0cHM6XC9cL2NlcnRpZmljYXRlcy5zaW1wbGljZG4ubmV0XC9zaGFyZVwvdGh1bWJfMzkwMzM4OF8xNjY3NDU1NjExLnBuZyIsInVzZXJuYW1lIjoiU29oYW0gQW5hbnQgU2F3YW50In0%3D&utm_source=shared-certificate&utm_medium=lms&utm_campaign=shared-certificate-promotion&referrer=https%3A%2F%2Flms.simplilearn.com%2Fcourses%2F4587%2FIntroduction-to-PHP%2Fcertificate%2Fdownload-skillup&%24web_only=true&_branch_match_id=1130058193000949919&_branch_referrer=H4sIAAAAAAAAA8soKSkottLXL87MLcjJ1EssKNDLyczL1k%2FVzyo1c%2FP08kxyLU0CALi%2FxNclAAAA"
}

st.set_page_config(page_title=PAGE_TITLE)

# Use local css 
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)

with col2:
    st.title("Soham Sawant")
    st.write("IEEE-VIT TechWeb & Docs Team Member")
    st.write("Student at VIT, Mumbai")
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file,
        mime="application/octet-stream",
    )
    st.write("📫","sohamsawant2000@email.com")

st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.header("Experience & Qualifications")

st.write(
    """
✔️ Conducted a workshop on "Scrape the Web" at IEEE-VIT \n
✔️ Participated in Global Level IEEE Xtreme Coding Competition \n
✔️ Ranked 3rd in Diploma (Information Technology) at Vidyalankar Polytechnic \n
✔️ Participated in State Level IEEE Paper Presentation \n
✔️ Earned 13/15 shields in Cambridge English Flyers Exam \n
    """
)

# --- SKILLS ---
st.write('\n')
st.header("Hard Skills")
st.write(
    """
👩‍💻 Programming: Python (Scikit-learn, Pandas), JavaSQL \n
📊 Data Visulization: PowerBi, MS Excel, Plotly \n 
📚 Modeling: Logistic regression, linear regression, decision trees \n
🗄️ Databases: PostgreSQL, MySQL, Oracle
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.header("Work History")

# --- JOB 1
st.write("🚧 IEEE-VIT", "**TechWeb and Docs Team Member**")
st.write("08/2022 - Present")
st.write(
    """
► Working as a Workforce Member for 1 year in college committee.\n
► Served as instructor for my workshop on Web Scraping.\n
► Documenting the events and writing the reports.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧 School2000", "**Technical Incharge**")
st.write("01/2021 - Present")
st.write(
    """
► Designing PowerPoint Presentation for E-Lesson in various languages. \n
► Converting PowerPoint Presentation to the voice using online services. \n
► Working as a team to guide and coordinate the similar work to team members.
"""
)

# --- Certifications ---
st.write('\n')
st.header("Certifications")
for cert, link in CERTIFICATIONS.items():
    st.write(f"[{cert}]({link})")

# --- Projects ---
st.write('\n')
st.header("Projects & Accomplishments")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")