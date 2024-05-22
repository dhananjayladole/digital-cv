from pathlib import Path

import streamlit as st
import webbrowser
from PIL import Image


# --- Path setting ---
current_dir = Path(__file__). parent if "__file__" in locals() else path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic_path = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Dhananjay Ladole"
PAGE_ICON = ":random:"
NAME = " Dhananjay Ladole "
DESCRIPTION = """
MBA-Business Analyst
"""
EMAIL = "dladole7@gmail.com"
Hire = "Hire Me Now!!!"
SOCIAL_MEDIA = {
    "✨LinkedIn": "https://www.linkedin.com/in/dhananjay-ladole-b59793215/",
    "✨GitHub": "https://github.com/dhananjayladole",
}

PROJECTS = {
    "🏆 Pratik Enterprizes Sales Dashboard - Comparing sales across stores": "",
    "🏆 Diversity and Inclusion Project - Power BI": "",
    "🏆 Research and Analysis Project - Perception on Shivaji Nagar Local MLA": "",
    "🏆 Churn Sales Project - Power BI" :"",
    "🏆 Converting Python code into Apk -(TicTacToe) " : "",
    "🏆 Creating Portfolio(Digital CV) using 'Python streamlit' " : "",
    
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


# --- HERO SECTION ---
#col1, col2 = st.columns(2, gap="medium")
col1, col2 = st.columns([1,2])

with col1:
    # Open and display profile picture
    profile_pic = Image.open(profile_pic_path)
    st.image(profile_pic, caption="", width=200)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📩", EMAIL)

# Button to open email client with your email pre-filled

if st.button("Hire Me Now!!!"):
        subject = "Job Opportunity"
        mailto_link = f"mailto:{EMAIL}?subject={subject}"
        mailto_link = f"mailto:{EMAIL}"
        webbrowser.open(f"mailto:{EMAIL}")

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("🏢 Experience")
st.write("---")
st.write(
    """
- ✔️ 1 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python PowerBI and Excel
- ✔️ Good understanding of statistical principles and their respective applications
"""
)

st.write('\n')
st.subheader("🧑🏻‍🎓 Qulifications")
st.write(
    """
- **Master's** :  M.B.A (Business Analytics) , At SPPU University
- **Degree**   :  Bachelor Of Enginnering  , SGBAU University
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("🎯 Skills")
st.write("---")
st.write(
    """
- 👩‍💻 **Programming:** Python
- 📊 **Data Visulization:** PowerBi, Tableau, MS Excel
- 🗄️ **Databases:** MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("💼 Work History")
st.write("---")

# --- Internship
st.write("**🌟 🧑‍💼 Data Analyst Intern | Collaborative Analytics (CPC)**")
st.write("08/2023 - 09/2023")
st.write(
    """
- ► Utilized Power BI, Excel, and other tools to collect, mine, analyze, and visualize data
- ► Assisted in various data analysis projects, contributing to actionable insights and recommendations
- ► Collaborated with team members to develop reports and dashboards for stakeholders
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

st.write("**🌟 🧑‍💼 Workshop Manager | Aspa bandson PVT.LTD**")
st.write("02/2021 - 01/2022")
st.write(
    """
- ► Utilized Excel and Power BI to analyse workshop performance metrics, identify trends, and generate reports for management review, enabling data-driven decision making and process improvemen
- ► Directed all aspects of workshop operations, including staff supervision, resource allocation, and customer service, ensuring optimal performance and customer satisfaction
- ► Iterations on the redesigned data model resulted in 22% better predictions. In order to find out how to boost sales, 

"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("🚀 Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"{project}")


# --- Send Message Box ---
st.write("\n")
st.subheader("Any Message / Queries")

message = st.text_input("Type your message / queries here:")
if st.button("Send"):
    if message:
        st.success("Sent Successfully!! Thank You....😊")
    else:
        st.warning("Please type a message before sending.")