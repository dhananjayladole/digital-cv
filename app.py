from pathlib import Path
import streamlit as st
import webbrowser
from PIL import Image

# --- Path setting ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "DhananjayLadole_ServiceNow_Developer_Resume.pdf"
profile_pic_path = current_dir / "assets" / "profile-pic.jpeg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio | Dhananjay Ladole"
PAGE_ICON = ":random:"
NAME = "Dhananjay Ladole"
DESCRIPTION = """
ServiceNow Developer
"""
EMAIL = "dladole7@gmail.com"
Hire = "Hire Me Now!!!"
SOCIAL_MEDIA = {
    "✨LinkedIn": "https://www.linkedin.com/in/dhananjay-ladole-b59793215/",
    "✨GitHub": "https://github.com/dhananjayladole",
}

# --- UPDATED PROJECTS ---
PROJECTS = {
    "🏆 ServiceNow Incident Automation – Scripted SLA escalations to cut resolution time by 20%": "",
    "🏆 ServiceNow Catalog Transformation – Migrated 30+ legacy forms to modern catalog items": "",
    "🏆 Power BI Multi‑Store Sales Dashboard – Comparative sales analytics": "",
    "🏆 Diversity & Inclusion Analytics – Workforce demographics in Power BI": "",
    "🏆 Customer Churn Prediction – SQL + Power BI model for churn risk": "",
    "🏆 Streamlit Digital CV – This portfolio app": "",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2])

with col1:
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

if st.button("Hire Me Now!!!"):
    subject = "Job Opportunity"
    mailto_link = f"mailto:{EMAIL}?subject={subject}"
    webbrowser.open(mailto_link)
    st.success(" Pleased click on my email to send an email. Thank you!!")

# --- SOCIAL LINKS ---
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- PROFESSIONAL SUMMARY ---
st.write("\n")
st.subheader("💼 Professional Summary")
st.write("---")
st.write(
    """
- ✔️ ServiceNow Developer with 2.7 years of experience designing, developing, and customizing ITSM modules.
- ✔️ Proficient in Incident, Problem, Change, Request Management, Service Catalog, and Flow Designer.
- ✔️ Skilled in Glide scripting (Client/Server), Business Rules, UI Policies, Script Includes, and ACLs.
- ✔️ MBA in Business Analytics with strong data analysis skills using SQL, Power BI, and Excel.
- ✔️ Strong team player with effective communication and quick learning ability.
"""
)

# --- SKILLS ---
st.write("\n")
st.subheader("🧠 Skills")
st.write("---")
st.write(
    """
- 🛠️ ServiceNow: ITSM, Service Catalog, Custom Apps, CMDB, ACLs, Flow Designer
- 💻 Scripting: GlideScript, Script Includes, Business Rules, Client Scripts, Scheduled Jobs
- 📊 Data Tools: SQL, Power BI, Excel, Dashboard Building, Data Visualization
- 🔍 Analytics: SLA Management, KPI Reporting, Customer Insights
- 🤝 Soft Skills: Communication, Collaboration, Adaptability, Problem Solving
"""
)

# --- WORK HISTORY ---
st.write("\n")
st.subheader("🏢 Work Experience")
st.write("---")

st.write("**ServiceNow Developer | Technozest Technologies Pvt. Ltd. – Pune**")
st.write("Dec 2022 – Present")
st.write(
    """
- ✔️ Developed and customized ITSM modules (Incident, Problem, Change, Request Management).
- ✔️ Created catalog items, client/server scripts, business rules, UI policies, and Flow Designer flows.
- ✔️ Designed and deployed custom ServiceNow applications with user-specific ACLs.
- ✔️ Managed update sets, version control, and platform migrations.
- ✔️ Implemented SLA conditions, email notifications, and workflow automation.
- ✔️ Coordinated with cross-functional teams for UAT, go-lives, and post-deployment support.
"""
)

st.write("**Data Analyst Intern | Collaborative Analytics (CPC) – Remote**")
st.write("Aug 2023 – Sep 2023")
st.write(
    """
- ✔️ Used SQL for data extraction and preparation.
- ✔️ Created Power BI dashboards for customer churn and public opinion analysis.
- ✔️ Applied ETL processes and performance metrics for analytical reporting.
"""
)

# --- QUALIFICATIONS ---
st.write("\n")
st.subheader("🎓 Education")
st.write("---")

col1, col2 = st.columns([3, 1])
with col1:
    st.write("**Master of Business Administration (MBA), Business Analytics** – Sinhgad Institute of Management, Pune")
with col2:
    st.write("Aug 2022 – Jun 2024")
st.write("CGPA: 6.56")

col1, col2 = st.columns([3, 1])
with col1:
    st.write("**Bachelor of Engineering (BE), Mechanical Engineering** – SHVPM COET, Amravati")
with col2:
    st.write("Aug 2017 – Jun 2022")
st.write("CGPA: 8.71")

# --- PROJECTS ---
st.write("\n")
st.subheader("🚀 Projects")
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
