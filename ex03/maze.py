import tkinter as tk
from random import randint

def key_down(event):
    global key
    
    key = event.keysym

def key_up(event):
    
    global key
    key=""

def main_proc():
    global cx,cy
    delta = {"Up"  :[0,-20],#キー：押されていうkey、値:移動幅を表している
            "Down" :[0,+20],
            "Right":[+20,0],
            "Left" :[-20,0],
            ""     :[0,0]}
    cx,cy = cx+delta[key][0],cy+delta[key][1]
    canvas.coords("tori",cx,cy)
    root.after(100,main_proc)





if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root,width = 1500,height = 900,bg = "black")
    canvas.pack()
    tori = tk.PhotoImage(file = "fig/6.png")
    cx,cy =30,40
    canvas.create_image(cx,cy,image = tori,tag ="tori")

    key = ""

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()

    

    


    root.mainloop()