from pathlib import Path
import streamlit as st
import webbrowser
from PIL import Image

# --- Path setting ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Dhananjay_Ladole_Resume.pdf"
profile_pic_path = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Dhananjay Ladole"
PAGE_ICON = ":random:"
NAME = "Dhananjay Ladole"
DESCRIPTION = """
MBA-Business Analyst / Data Analyst
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
    "🏆 Churn Sales Project - Power BI": "",
    "🏆 Converting Python code into Apk - (TicTacToe)": "",
    "🏆 Creating Portfolio (Digital CV) using 'Python streamlit'": "",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2])

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
    webbrowser.open(mailto_link)
    st.success(" Pleased click on my email to send an email. Thank you!!")

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
- ✔️ Detail-oriented Business Analyst / Data Analyst based in Pune with extensive hands-on experience in Python, SQL, Excel, and Power BI.
- ✔️ Experienced in conducting business analysis, including customer growth analytics, Sales Analysis and identifying key lead indicators.
- ✔️ Certified in Python, Tableau, SPSS, IoT, Power BI, and Excel, demonstrating continuous commitment to technical proficiency.
- ✔️ Dedicated to delivering accurate insights and strategic recommendations through meticulous data analysis and visualization techniques.
- ✔️ Skilled in developing and maintaining dashboards, ensuring accurate and actionable reporting.
"""
)

st.write('\n')
st.subheader("🧑🏻‍🎓 Qualifications")
st.write("---")
st.write("**Master's**   : M.B.A (Business Analytics), Sinhgad Institute Of management (SPPU University) Aug 2022 - Jun 2024")
st.write("**Bachelor's** : Bachelor Of Engineering (Mechanical), SHVPM COET Amravati Aug 2017 - Jun 2022")

# --- SKILLS ---
st.write('\n')
st.subheader("🎯 Skills")
st.write("---")
st.write(
    """
- 📈 **Data Analysis & Reporting:** Power BI, Excel, Google Sheets
- 📊 **Statistical & Analytical Models:** Python, Statistical Analysis
- 💹 **Data Visualization:** Tableau, PowerBi , Google Studio
- 👨🏻‍💻 **Database Management:** SQL (Complex Queries, Data Extraction)
- 🔧 **ServiceNow & IT Operations:** ITSM, ITOM, Infrastructure Operations, Application Development & Management  
- 📊 **Business Analysis:** Customer Growth Analytics, KeyLead Indicators, Issue Diagnosis
- 🧑🏻‍💻 **Technical Proficiency:** Dashboard Development, Reporting System Maintenance
- ✨ **Soft Skills:** Quick Learner, Team Player, Effective Communication
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("💼 Work History")
st.write("---")

# --- Professional
st.write("**🌟 🧑‍💼 Data Analyst/ ServiceNow Admin | Technozest PVT.LTD**")
st.write("05/2025 - Present")
st.write(
    """
- ✔️ Utilized Excel and Power BI to analyze workshop performance metrics, identify trends, and generate reports for management review, enabling data-driven decision making and process improvement
- ✔️ Transitioned from Data Analyst to ServiceNow Admin role after 3 months.
- ✔️ Optimized SQL queries, improving database performance by 40%.
- ✔️ Automated monthly reports using Power BI, reducing manual effort by 50%.
- ✔️ Worked on ServiceNow ,ITSM for incident and change management.
- ✔️ Developed ServiceNow applications, streamlining IT operations.
- ✔️ Managed ITIL & Infrastructure Operations, ensuring system efficiency.

"""
)

#---Internship
st.write("**🌟 🧑‍💼 Data Analyst Intern | Collaborative Analytics (CPC)**")
st.write("08/2023 - 09/2023")
st.write(
    """
- ✔️ Utilized Power BI, Excel, and other tools to collect, mine, analyze, and visualize data
- ✔️ Assisted in various data analysis projects, contributing to actionable insights and recommendations
- ✔️ Collaborated with team members to develop reports and dashboards for stakeholders
- ✔️ Redesigned data model through iterations that improved predictions by 12%
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
