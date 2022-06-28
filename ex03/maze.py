import tkinter as tk
from random import randint
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    print(f"{key}キーが押されました")
def key_up(event):
    
    global key
    key=""

def main_proc():
    global cx,cy,mx,my
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





if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root,width = 1500,height = 900,bg = "black")

    canvas.pack()
    maze_bg=mm.make_maze(15,9)#1壁、0は床
    mm.show_maze(canvas,maze_bg)#canvasにmaze_bgを書く

    tori = tk.PhotoImage(file = "fig/6.png")
    cx,cy =30,40
    canvas.create_image(cx,cy,image = tori,tag ="tori")

    key = ""

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    mx,my=1,1

    main_proc()

    

    

    


    root.mainloop()