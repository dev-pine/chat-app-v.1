import streamlit as st
import threading
import time
from streamlit.components.v1 import html
st.title('검열없는 채팅방')
place = st.empty()
def check():
  while True:
    place.empty()
    with open("d.txt","r") as f:
      place.text(f.read())
    time.sleep(1)
check()
name = st.text_input("이름을 입력하세요: ")
text = st.text_input("문자를 입력하세요: ")
if st.button('대화 전송||대화확인'):
  if text:
    with open("d.txt","a") as f:
      f.write(name+":"+text)
      f.write("\n")
# p2 = threading.Thread(target=check)
# p2.start()
