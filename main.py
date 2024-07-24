import streamlit as st
import time
import threading
from streamlit.components.v1 import html

# CSS to make the widget stick to the bottom
css = """
    <style>
    .bottom-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        padding: 10px;
        box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
    }
    .main-content {
        margin-bottom: 60px; /* Adjust based on the height of the bottom bar */
    }
    </style>
"""
html(css, unsafe_allow_html=True)

# Main content
st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.title('검열없는 채팅방')
place = st.empty()
st.markdown('</div>', unsafe_allow_html=True)

# Bottom bar
st.markdown('<div class="bottom-bar">', unsafe_allow_html=True)
text = st.text_input("문자를 입력하세요: ")
name = st.text_input("이름을 입력하세요: ")
if st.button('대화 전송||대화확인'):
    if text:
        with open("d.txt", "a") as f:
            f.write(name + ":" + text + "\n")
st.markdown('</div>', unsafe_allow_html=True)

# Function to check the file and update the displayed text
def check():
    while True:
        with open("d.txt", "r") as f:
            place.text(f.read())
        time.sleep(1)

# Run the check function in a separate thread
thread = threading.Thread(target=check, daemon=True)
thread.start()
