import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event): #ボタンがクリックされた時の動作
    btn = event.widget
    tex = btn["text"]
    #tkm.showinfo(f"{tex}がクリックされました")
    if tex=="=":#　=を押したとき
         eqn = entry.get()
         ans = eval(eqn)
         entry.delete(0, tk.END)
         entry.insert(tk.END,ans)

    elif tex=="C": #Cを押すと、全て消える
        entry.delete(0, tk.END)

    elif tex=="TAX":#税込みの価格を知る
        eqn = entry.get()
        ans = eval(eqn)*1.1
        entry.delete(0, tk.END)
        entry.insert(tk.END,ans)

    elif tex=="unico":#unicodeを知ることが出来る
        eqn = entry.get()
        ans = chr(eval(eqn))
        entry.delete(0, tk.END)
        entry.insert(tk.END,ans)

    else:
        entry.insert(tk.END,tex)

if __name__=="__main__":

    root = tk.Tk()
    root.geometry("300x600")#300×600の枠
    r,c=1,0

    entry = tk.Entry(root, justify="right",width =10,font=("Times New Roman",40))
    entry.grid(row=0,column=0,columnspan=3)

    for i,num in enumerate(["C","TAX","unico",9,8,7,6,5,4,3,2,1,0,"+","=","*","/","-"]):#表示されるコマンド
        btn = tk.Button(root,text=f"{num}",
        width =4,
        height=2,
        font=("Times New Roman",20))
        btn.grid(row = r , column=c)
        btn.bind("<1>",button_click)
        c+=1
        if (i-2)%3==0:
            r+=1
            c=0
            btn.bind("<1>",button_click)

        
        




root.mainloop()