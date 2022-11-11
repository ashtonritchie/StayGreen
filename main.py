import pyautogui as gui
import mouseinfo

speed_down = -100
sleeptime = 1
speed_up = 100
gui.FAILSAFE = True
#start = st.button('Begin Session')
#stop = st.button('Resume Work')

while 0 < 1:
    gui.scroll(int(speed_down))
    gui.sleep(int(sleeptime))
    gui.scroll(int(speed_up))
    gui.sleep(int(sleeptime))


