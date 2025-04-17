import streamlit as st
from PIL import Image
from pathlib import Path
current_path = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css=current_path/"styles"/"main.css"
resume=current_path/"assets"/"resume.pdf"
profilepic=""


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
    "Speech Or Text to Sign converstion": "https://github.com/DhumalePrasad04/Speech-or-Text-to-Sign-conversion",
    "Stock Analysis and precdection":"https://github.com/DhumalePrasad04/secure-world",
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



