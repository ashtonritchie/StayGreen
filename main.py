import pyautogui as gui
import streamlit as st
import os
os.environ['DISPLAY'] = ':0'
os.environ['XAUTHORITY'] = '/run/user/1000/gdm/Xauthority'

st.set_page_config(page_title="StayGreen", layout='wide')

st.write('''
    # Welcome to StayGreen!
    a simple solution for appearing online, offline
''')
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

col1, col2, col3 = st.columns(3)

with col1:
    with st.expander('Instructions', expanded=False):
        st.write('''
        To begin, simply click "Begin Session." Then, move your mouse to a scrollable window. I like to use a
        Teams chat. Remove your hand from the mouse and watch your window scroll up and down in perpetuity.
        Your online status will appear active to anyone who my be watching. When it's time to return to work, 
        click "Resume Work." Enjoy!
             ''')

speed_down = -100
sleeptime = 1
speed_up = 100
gui.FAILSAFE = False
start = st.button('Begin Session')
stop = st.button('Resume Work')

if start:
    st.markdown('<font color=‘red’>Session in progress...</font>', unsafe_allow_html=True)
    while start:
        gui.scroll(int(speed_down))
        gui.sleep(int(sleeptime))
        gui.scroll(int(speed_up))
        gui.sleep(int(sleeptime))
        if stop:
            break
        st.write('')






