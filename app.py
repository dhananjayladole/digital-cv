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

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("🏢 Experience")
st.write("---")
st.write(
    """
- ✔️ ** ServiceNow Developer with 2.7 years of experience** developing, customizing, and supporting ITSM modules (Incident, Problem, Change, Request)
- ✔️  Proficient in **Glide scripting (client/server), Business Rules, Client Scripts, UI/Data Policies, Scheduled Jobs, and ACLs**
- ✔️  Experienced in **custom application development, catalog item design, workflow/Flow Designer automations, and update‑set management**
- ✔️  ** MBA in Business Analytics** with hands‑on skills in **SQL, Power BI, and Excel** for data analysis and reporting
- ✔️  Strong analytical thinking, attention to detail, and a growth mindset; collaborates effectively with cross‑functional teams to deliver ITIL‑aligned solutions
"""
)

# --- QUALIFICATIONS ---
st.write("\n")
st.subheader("🧑🏻‍🎓 Qualifications")
st.write("---")
st.write("**Master of Business Administration (MBA) – Business Analytics** | Sinhgad Institute of Management, Pune              *Aug 2022 – Jun 2024*  \nCGPA: 6.56")
st.write("**Bachelor of Engineering (BE) – Mechanical Engineering** | SHVPM COET, Amravati                                      *Aug 2017 – Jun 2022*  \nCGPA: 8.71")

# --- SKILLS ---
st.write("\n")
st.subheader("🎯 Skills")
st.write("---")
st.write(
    """
- 🛠️  ** ServiceNow Platform:** ITSM (Incident, Problem, Change, Request), Service Catalog, Custom Applications, Flow Designer, Update Sets, ACLs, CMDB (basic)
- 💻  ** Scripting & Automation:** GlideScript (client/server), Business Rules, Client Scripts, Script Includes, Scheduled Jobs, REST API (basic)
- 📊  ** Data & Analytics:** SQL, Power BI, Excel (advanced), Data Visualization, Dashboard Development
- 📈  ** Reporting & Insights:** Performance Analytics, KPI Tracking, SLA Management
- 🤝  ** Soft Skills:** Analytical Thinking, Attention to Detail, Time Management, Team Collaboration, Effective Communication
"""
)

# --- WORK HISTORY ---
st.write("\n")
st.subheader("💼 Work History")
st.write("---")

# --- Professional Experience
st.write("**🌟 🧑‍💼 ServiceNow Developer | Technozest Technologies Pvt. Ltd., Pune**")
st.write("Dec 2022 – Present")
st.write(
    """
- ✔️ Developed and customized ITSM modules (Incident, Problem, Change, Request) with catalog items, workflows, and scripted automations
- ✔️ Configured **Access Control Rules (ACLs)** to secure tables and fields based on roles and conditions
- ✔️ Built and maintained custom ServiceNow applications to streamline internal processes
- ✔️ Automated tasks using Glide scripting, Script Includes, Scheduled Jobs, and Flow Designer, cutting manual effort by 30%
- ✔️ Managed Update Sets across dev, test, and prod; supported platform upgrades and patching
- ✔️ Collaborated with stakeholders to gather requirements, conduct UAT, and deploy enhancements
- ✔️ Implemented SLA definitions and notification triggers; reduced incident resolution time via scripted escalations
"""
)

# --- Internship
st.write("**🌟 🧑‍💼 Data Analyst Intern | Collaborative Analytics (CPC), Remote**")
st.write("Aug 2023 – Sep 2023 | Part‑time Internship")
st.write(
    """
- ✔️ Queried and prepared large datasets using **SQL** for business analytics objectives
- ✔️ Built interactive dashboards in **Power BI** to visualize public perception and customer churn trends
- ✔️ Presented data‑driven insights and recommendations to academic stakeholders
"""
)

# --- Projects & Accomplishments ---
st.write("\n")
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
