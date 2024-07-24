import streamlit as st
import threading
import time
st.title('나의 첫 웹서비스')
name = st.text_input("이름을 입력하세요: ")
text = st.text_input("문자를 입력하세요: ")
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
