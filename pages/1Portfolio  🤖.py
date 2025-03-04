import streamlit as st
import info
import pandas as pd

st.set_page_config(page_title="Portfolio", page_icon="🤖")

#About Me
def about_me_section():
    st.header("🤖 About Me")
    st.image(info.profile_picture, width=500)
    st.write(info.about_me)
    st.write("---")
about_me_section()

#SideBar links
def links_section():
    st.sidebar.header("Auspex Links")
    st.sidebar.text("Connect with me on the Noosphere")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src = "{info.linkedin_image_url}" alt="Linkedin" width= "85" height= "85"></a>'
    st.sidebar.markdown(linkedin_link,unsafe_allow_html=True)
    st.sidebar.text("Behold my forbidden knowledge")
    github_link = f'<a href="{info.my_github_url}"><img src = "{info.github_image_url}" alt="github" width= "75" height= "75"></a>'
    st.sidebar.markdown(github_link,unsafe_allow_html=True)
    st.sidebar.text("Submit inquiries here                                        (or pleas for enlightenment)")
    email_html = f'<a href="mailto:{info.my_email_address}"><img src = "{info.email_image_url}" alt="Email" width= "85" height= "85"></a>'
    st.sidebar.markdown(email_html,unsafe_allow_html=True)
links_section()

#Education
def education_section(education_data,course_data):
    st.header("💾 Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:** {education_data['Degree']}", unsafe_allow_html=True)
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}", unsafe_allow_html=True)
    st.write(f"**GPA:** {education_data['GPA']}", unsafe_allow_html=True)
    st.write(f"**Relevant Coursework:**", unsafe_allow_html=True)
    coursework= pd.DataFrame(course_data)
    st.dataframe(coursework,column_config={
        "code":"Course Code",
        "names":"Course Names",
        "semester_taken":"Semester Taken",
        "skills": "What I Learned"},
        hide_index=True
        )
    st.write("---")
education_section(info.education_data,info.course_data)

#Professional Experience

def display_experience(experience_data):
    st.header("📟 Professional Experience")
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(job_title)
        expander.image(image, width=500)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")

display_experience(info.experience_data)

#Projects
def project_section(projects_data):
    st.header("🛠 Projects")
    for project_name, project_description in projects_data.items():
        expander = st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---") 

project_section(info.projects_data)

#Skills
def skills_section(programming_data,spoken_data,other_data):
    st.header("💡 Skills")
    st.subheader("Technological Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill,)}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken,proficiency in spoken_data.items():
        st.write(f"{spoken}{info.spoken_icons.get(spoken,)}:{proficiency}")
    st.subheader("Miscellaneous")
    for other,proficiency in other_data.items():
        st.write(f"{other}{info.other_icons.get(other,)}:{proficiency}")
    st.write("---")
skills_section(info.programming_data,info.spoken_data,info.other_data)


#Activities

def activities_section(leadership_data,more_data):
    st.header ("📡 Activities")
    tab1, tab2 = st.tabs(["Leadership", "Service"])
    with tab1:
        st.subheader("Leadership")
        for title, (details,image) in leadership_data.items():
            expander=st.expander(f"{title}")
            expander.image(image,width=500)
            for bullet in details:
               expander.write(bullet)
    with tab2:
        st.subheader("Service")
        for title, (details,image) in more_data.items():
            expander=st.expander(f"{title}")
            expander.image(image,width=500)
            for bullet in details:
               expander.write(bullet)   
    st.write("---")

activities_section(info.leadership_data,info.more_data)