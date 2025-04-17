import streamlit as st
from PIL import Image
from pathlib import Path
current_path = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css=current_path/"styles"/"main.css"
resume=current_path/"assets"/"resume.pdf"
profilepic=current_path/"assets"/"profile pic.jpg"


page_title="Prasad's Portfolio"
page_icon=":wave:"
name="Dhumale Prasad"
description="""I am a Fresher who's interest peaks in AI and playing with llm  """
email="dhumaleprasad04@gmail.com"
social_media={
    "LinkedIn":"https://www.linkedin.com/in/prasad-dhumale-aa1032261/",
    "Github":"https://github.com/DhumalePrasad04",
    "X":"https://x.com/DhumaleTiku"
}
projects={
    "CoTrue":"https://github.com/DhumalePrasad04/COtrue",
    "CoTrue2.0":"https://github.com/DhumalePrasad04/CoTrue-2.0",
    "Speech Or Text to Sign conversion": "https://github.com/DhumalePrasad04/Speech-or-Text-to-Sign-conversion",
    "Stock Analysis and prediction":"https://github.com/DhumalePrasad04/secure-world",
    "local Chatbot":"https://github.com/DhumalePrasad04/Local-Chatbot-jarvis-",
}

st.set_page_config(
    page_title=page_title,
    page_icon=page_icon,)
st.title("Prasad's Portfolio")

with open(css) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume,"rb") as f:
    pdf=f.read()

col1,col2=st.columns(2,gap="small")

with col1:
    st.image(profilepic,width=250)
with col2:
    st.subheader(name)
    st.write(description)
    st.download_button(
        label="Download Resume",
        data=pdf,
        file_name=resume.name,
        mime="application/octet-stream",
    )
    st.write("📩",email)
st.write("#")
cols=st.columns(len(social_media))
for index,(platform,link) in enumerate(social_media.items()):
    cols[index].write(f"[{platform}]({link})")

st.header("EDUCATION")
st.write(
    """
- #### EDUCATION 
<ul> 
<li>GRADUATION | REVA UNIVERSITY, B. Tech in Computer Science and Engineering (2022-2026) CGPA: 9.25 (up to 5th Semester).</li>
<li>SENIOR SECONDARY | Diamond Independent P U College, Bhalki (2020-2022) Percentage: 94.5%.</li>
<li>HIGHER SECONDARY | Geetha High School Chegunta (2019-2020) CGPA:10.0 </li> 
</ul>


    """,
    unsafe_allow_html=True
)


