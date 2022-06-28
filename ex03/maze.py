import tkinter as tk
import mazemaker as mm
from random import randint




if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root,width = 1500,height = 900,bg = "black")

    tori = tk.PhotoImage(file = "fig/6.png")

    canvas.create_image(300,400,image = tori)