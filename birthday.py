import streamlit as st
import time
import random
from datetime import datetime

st.set_page_config(
    page_title="Happy Birthday Almas ❤️",
    page_icon="🎂",
    layout="centered"
)

# -------- STYLE --------
st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #ff758c, #ff7eb3);
}
.card {
    background: rgba(255,255,255,0.28);
    padding: 35px;
    border-radius: 22px;
    text-align: center;
    color: white;
    font-size: 22px;
    box-shadow: 0 20px 45px rgba(0,0,0,0.35);
}
.heart {
    position: fixed;
    bottom: -10px;
    font-size: 24px;
    animation: float 6s linear infinite;
}
@keyframes float {
    0% { transform: translateY(0); opacity: 1; }
    100% { transform: translateY(-110vh); opacity: 0; }
}
.name {
    font-size: 30px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# -------- FLOATING HEARTS --------
for _ in range(15):
    st.markdown(
        f"<div class='heart' style='left:{random.randint(0,100)}vw; animation-delay:{random.random()*5}s'>❤️</div>",
        unsafe_allow_html=True
    )

# -------- MIDNIGHT FEEL --------
hour = datetime.now().hour
if hour >= 0 and hour < 5:
    greeting = "Midnight feels different with you ✨"
else:
    greeting = "Today is special because of you ✨"

# -------- SESSION --------
if "step" not in st.session_state:
    st.session_state.step = 0

messages = [
    f"🎂 Happy Birthday <span class='name'>Almas</span> ❤️",
    greeting,
    "Ap meri dua ho, mera sukoon ho 🤍",
    "Ap wo h jissy ma sari zindgi dakhy guzar sakta hon🌸",
    "Main wada karta hoon har pal tumhara khayal rakhunga 💍",
    "Shayad ma rahon ya na rahon lakin meri muhabbat hamesha ap k sath rahy gi ❤️",
    "You are the most beautiful girl i ever seen in the world and life ",
    "Meri dua ha k ap jahan b raho lakin khush mery sath rahna kahin or ka sochna b mat  ",
    "Last but not least ",
     "Agr ap mera sath do gi to ma kisi k b paon pr jaon ga ",
    "Almas… kya tum meri zindagi ka hamesha ka hissa banogi? 💍✨"
]

st.title("🎉 A Special Surprise For You")
st.write("")

# -------- BUTTON --------
if st.button("💖 Load Love"):
    st.session_state.step += 1

# -------- MESSAGE DISPLAY --------
if st.session_state.step > 0:
    index = st.session_state.step - 1

    if index < len(messages):
        text = messages[index]
        placeholder = st.empty()
        typed = ""

        for char in text:
            typed += char
            placeholder.markdown(
                f"<div class='card'>{typed}</div>",
                unsafe_allow_html=True
            )
            time.sleep(0.05)

        st.progress((index + 1) / len(messages))

    else:
        st.success("💍 She said YES… and my world became complete ❤️")
        st.balloons()
