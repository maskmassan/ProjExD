from itertools import count
import tkinter as tk
from random import randint
import maze_maker as mm
import tkinter.messagebox as ms

def key_down(event):
    global key 
    key = event.keysym
    
    
    

def countup():
    global tmr,jid
    tmr +=1
    jid = root.after(1000,countup)
    

def key_up(event):
    
    global key
    key=""

def main_proc():
    global cx,cy,mx,my,m
    delta = {"Up"   : [0, -1],
             "Down" : [0, +1],
             "Left" : [-1, 0],
             "Right": [+1, 0],
             ""     : [0,  0],
             }
    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]] == 0: #移動先が床なら
            mx += delta[key][0]
            my += delta[key][1]
    except:
        pass
    cx, cy = 100*mx+50, 100*my+50
    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)
    if cx ==1350:
        if cy ==750:
            m+=1

    if m==1:
        ms.showinfo("終了","攻略されました")
        ms.showinfo("終了",f"{tmr}秒かかりました")
        root.bind("<keyPress>",countup)
            

            


if __name__ == "__main__":
    root = tk.Tk()
    
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root,width = 1500,height = 900,bg = "black")

    canvas.pack()
    maze_bg=mm.make_maze(15,9)#1壁、0は床
    mm.show_maze(canvas,maze_bg)#canvasにmaze_bgを書く
    canvas.create_rectangle(1300,700, 1400, 800, fill = 'red') #ゴール地点
    canvas.create_rectangle(100,100, 200, 200, fill = 'blue')#スタート地点

    tori = tk.PhotoImage(file = "fig/6.png")
    
    cx,cy =30,40
    canvas.create_image(cx,cy,image = tori,tag ="tori")

    key = ""

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    mx,my=1,1
    tmr =0
    m=0
    jid =None


    main_proc()
    countup()


    

    

    


    root.mainloop()