from tkinter import *
from cv2 import *
import PIL.Image,PIL.ImageTk
import threading
import imutils
import time



stream=VideoCapture("DRS_VDO2.mp4")
def play(speed):
  frame1=stream.get(CAP_PROP_POS_FRAMES)
  stream.set(CAP_PROP_POS_FRAMES, frame1+speed)
  grabbed,frame=stream.read()
  frame=imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
  frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
  canvas.image=frame
  canvas.create_image(0,0,anchor=NW,image=frame)
  canvas.create_text(140,30,fill="black",font="Times 20 italic bold",text="DECISION PENDING")      


def pending(decision):
    cv_dp=cvtColor(imread("DRS_DP.png"),COLOR_BGR2RGB)
    frame=imutils.resize(cv_dp, width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_dp))
    canvas.image=frame
    canvas_image=canvas.create_image(0,0,anchor=NW,image=frame)
    time.sleep(1)

    cv_sponsor=cvtColor(imread("DRS_Sponsor.png"),COLOR_BGR2RGB)
    frame=imutils.resize(cv_sponsor, width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_sponsor))
    canvas.image=frame
    canvas_image=canvas.create_image(0,0,anchor=NW,image=frame)
    time.sleep(2)

    if decision=="OUT":
        cv_out=cvtColor(imread("DRS_Out.png"),COLOR_BGR2RGB)
        frame=imutils.resize(cv_out, width=SET_WIDTH,height=SET_HEIGHT)
        frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_out))
        canvas.image=frame
        canvas_image=canvas.create_image(0,0,anchor=NW,image=frame)
    else:
        cv_notout=cvtColor(imread("DRS_Notout.png"),COLOR_BGR2RGB)
        frame=imutils.resize(cv_notout, width=SET_WIDTH,height=SET_HEIGHT)
        frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_notout))
        canvas.image=frame
        canvas_image=canvas.create_image(0,0,anchor=NW,image=frame)
   
def Out():
    thread=threading.Thread(target=pending, args=("OUT",))
    thread.daemon=1
    thread.start()
    
def Notout():
    thread=threading.Thread(target=pending, args=("NOTOUT",))
    thread.daemon=1
    thread.start()
    
SET_WIDTH=640
SET_HEIGHT=426

window=Tk()
window.title("DECISION REVIEW SYSTEM")
canvas=Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
cv_bg=cvtColor(imread("DRS_BG.png"), COLOR_BGR2RGB)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_bg))
canvas_image=canvas.create_image(0,0,anchor=NW,image=photo)
canvas.pack()
rwfast=Button(window,text="<<<<REWIND(FAST)",width=50,borderwidth=10,command=lambda:play(-10))
rwfast.pack()
rwslow=Button(window,text="<<REWIND(SLOW)",width=50,borderwidth=10,command=lambda:play(-2))
rwslow.pack()
fwfast=Button(window,text="FORWARD(FAST)>>>>",width=50,borderwidth=10,command=lambda:play(10))
fwfast.pack()
fwslow=Button(window,text="FORWARD(SLOW)>>",width=50,borderwidth=10,command=lambda:play(2))
fwslow.pack()
out=Button(window,text="DECISION:OUT",width=50,borderwidth=10,command=Out)
out.pack()
nout=Button(window,text="DECISION: NOT OUT",width=50,borderwidth=10,command=Notout)
nout.pack()
window.mainloop()
