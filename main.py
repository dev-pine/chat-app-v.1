import streamlit as st
import threading
import time
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
    </style>
"""
html(css, unsafe_allow_html=True)
st.markdown('<div class="bottom-bar">', unsafe_allow_html=True)
text = st.text_input("문자를 입력하세요: ")
st.markdown('</div>', unsafe_allow_html=True)
st.title('검열없는 채팅방')
name = st.text_input("이름을 입력하세요: ")
place = st.empty()
if st.button('대화 전송||대화확인'):
  if text:
    with open("d.txt","a") as f:
      f.write(name+":"+text)
      f.write("\n")
def check():
  while True:
    place.empty()
    with open("d.txt","r") as f:
      place.text(f.read())
    time.sleep(1)
check()
# p2 = threading.Thread(target=check)
# p2.start()
