from pynput import mouse
from pynput.mouse import Button,Controller
mous=Controller()
import time
#1 Read pointer poosition
#print("Current pointer position is {0} ".format(mous.position))
#time.sleep(2)
'''
#2 Set Pointer Position
mous.position = (12, 118)
print("New Position of mouse will be {0} ".format(mous.position))
time.sleep(1)

#3 Move Pointer Position
# Move pointer relative to current position
i=1
while i<15:
    mous.move(5+i, -5+i)
    i+=1
    time.sleep(.2)

#4 Press and Release
mous.position = (1243, 10)
mous.press(Button.left)
mous.release(Button.left)


mous.click(Button.left,2)

mous.scroll(0,12)
'''
#def on_move(x,y):
    #print('Pointer moved to {0}'.format((x,y)))
a=None
b=None
c=None
d=None

def on_click(x,y,button,pressed):
    print("{0} at {1} ".format("pressed" if pressed else "Released",(x,y)))
    if not pressed:
         return False


#def on_scroll(x,y,dx,dy):
    #print('Scrolled {0} at {1}'.format('down' if dy < 0  else 'Up',(x,y)))
#i=input("Enter 1 or not ")
#a = "Pressed" if i==1 else "release" 
#print(a)

#with mouse.Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as l:
with mouse.Listener(on_click=on_click) as l: 
        l.join()
  #      print("end")

