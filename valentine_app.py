import streamlit as st
from pathlib import Path

from streamlit.source_util import page_icon_and_name

st.set_page_config(
    page_title="Valentine 💘",
    page_icon = "🌹",
    layout = "centered")

PHOTO_PATH = Path("us.JPG")

if "page" not in st.session_state:
    st.session_state.page = "start"

def go(page):
    st.session_state.page = page

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffe6f2, #ffd6e8);
    font-family: "Helvetica Neue", Arial, sans-serif;
}
.val-card {
    background: transparent;
    padding: 0rem;
    border-radius: 0rem;
    border: none;
    box-shadow: none;
}
.val-title {
    font-size: 2.4rem;
    text-align: center;
    color: #c2185b;
    font-weight: 800;
}
.val-text {
    font-size: 1.1rem;
    color: #6d214f;
    line-height: 1.6;
}
.stButton > button {
    border-radius: 50px !important;
    padding: 0.6rem 1.2rem !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    border: none;
    background: linear-gradient(135deg, #ff5fa2, #ff8899) !important;
    color: white !important;
    box-shadow: 0 6px 18px rgba(0,0,0,0.12);
}
</style>
""", unsafe_allow_html=True)


def start_page():
    st.markdown('<div class="val-card">', unsafe_allow_html=True)
    st.markdown('<div class="val-title">Hey my cutie pie 💌</div>', unsafe_allow_html=True)
    st.markdown('<p class="val-text">I have a very cute Valentine question for you…</p>',
                unsafe_allow_html=True)
    if st.button("Start ❤️"):
        go("page1")
    st.markdown('</div>', unsafe_allow_html=True)


def page1():
    st.markdown('<div class="val-card">', unsafe_allow_html=True)
    st.markdown('<div class="val-title">🌹 Page 1 🌹</div>', unsafe_allow_html=True)
    st.markdown('<p class="val-text">Ready to continue?</p>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes"):
            go("page2")
    with col2:
        if st.button("No"):
            go("first_no_page")
    st.markdown('</div>', unsafe_allow_html=True)


def page2():
    st.markdown('<div class="val-card">', unsafe_allow_html=True)
    st.markdown('<div class="val-title"> Page 2 </div>', unsafe_allow_html=True)
    st.markdown('<p class="val-text">Are you prepared for the cutest question of 2026?</p>',
                unsafe_allow_html=True)
    if st.button("Continue"):
        go("big_question")
    st.markdown('</div>', unsafe_allow_html=True)


def big_question():
    st.markdown('<div class="val-card">', unsafe_allow_html=True)
    st.markdown('<div class="val-title">💘 The Big Question 💘</div>', unsafe_allow_html=True)
    st.markdown('<p class="val-text">Will you be my FOREVER VALENTINE ?</p>',
                unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("YES ❤️ "):
            go("yes_page")
    with col2:
        if st.button("NO 💔"):
            go("no_page")
    st.markdown('</div>', unsafe_allow_html=True)


def yes_page():
    st.markdown("""
        <div style="text-align:center;">
            <h1 style="color:#c2185b; font-size:2.5rem;">Yayyy! ❤️</h1>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <p class="val-text" style="font-size:1.2rem; color:#6d214f; line-height:1.6;">
            Awwww, you said <b>YES</b> 🥺💘 <br><br>
            Now you're officially my <b>Forever Valentine</b>. <br>
            No refunds. No returns. You're stuck with me 😌🌹  
        </p>
    """, unsafe_allow_html=True)
    st.markdown(
        '<a href="sms:+14698448748&body=Yes%20baby%20I%20said%20YES%20❤️" '
        'style="text-decoration:none;"><button>Text Seema I Said YES ❤️</button></a>',
        unsafe_allow_html=True
    )

    # SHOW PHOTO
    if PHOTO_PATH.exists():
        st.image(str(PHOTO_PATH), caption="Us 💕", use_container_width=True)
    else:
        st.warning("Add your picture as us.JPG in this folder!")

    if st.button("Replay 🔁"):
        go("start")


def no_page():
    st.markdown('<div class="val-card">', unsafe_allow_html=True)
    st.markdown('<div class="val-title">💔 Wow…</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="val-text">
    You said no???  
    Okay wow… bold choice 😭  
    But honestly…  
    <br><br>
    <b>Your loss 😌💅</b>  
    </p>
    """, unsafe_allow_html=True)

    if st.button("Go back ❤️"):
        go("big_question")
    if st.button("Restart 🔁"):
        go("start")

    st.markdown('</div>', unsafe_allow_html=True)

def first_no_page():
    st.markdown('<div class="val-card">', unsafe_allow_html=True)
    st.markdown('<div class="val-title">👀 You didn’t even try…</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <p class="val-text">
        Wowww, you said <b>no</b> before we even got to the actual question. 💀😂<br><br>
        Lowkey… <b>your loss</b> because you didn’t even participate properly.  
        But I’ll be nice and give you another chance. 😌🌹  
        </p>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Changed your mind? 👉 Take me back"):
            # send them back to Page 1 or straight to Page 2 if you prefer
            go("page1")
    with col2:
        if st.button("Restart from the beginning 🔁"):
            go("start")

    st.markdown('</div>', unsafe_allow_html=True)

# Router
page = st.session_state.page

if page == "start":
    start_page()
elif page == "page1":
    page1()
elif page == "page2":
    page2()
elif page == "big_question":
    big_question()
elif page == "yes_page":
    yes_page()
elif page == "no_page":
    no_page()
elif page == "first_no_page":
    first_no_page()

