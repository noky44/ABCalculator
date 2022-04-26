import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mb

def do_processing():
    n1 = int(entry11.get())
    c1 = int(entry12.get())
    n2 = int(entry21.get())
    c2 = int(entry22.get())
    
    if n1<=0 or n2<=0:
        mb.showerror(title="Error", message="Wrong number of visitors")
        return 
    
    popup_window(n1, c1, n2, c2) 

def popup_window(n1, c1, n2, c2):
    window = tk.Toplevel()
    window.geometry("280x300")
    window.title("A/B results")
    
    btnCloseWindow = ttk.Button(window, text="Close", style="W.TButton", command=window.destroy)
    btnCloseWindow.place(x=153, y=255, width=110, height=30)
    
    window.focus_force()

root = tk.Tk()
root.geometry("280x300")
root.title("A/B Calculator")

st = ttk.Style()
st.configure("W.TButton", font=("Helvetica", 10, "bold"))
st.configure("S.TLabel", font=("Helvetica", 10), foreground="#1D0046")

title = tk.Label(root, text="A/B Calculator", font=("Helvetica", 16, "bold"), fg="blue")
title.place(x=65, y=10)

label1 = tk.Label(root, text="Control group", font=("Helvetica", 12, "bold"), fg="#5C18BF")
label1.place(x=15, y=45)

label11 = ttk.Label(root, text="Visitors:", style="S.TLabel")
label11.place(x=15, y=80)

entry11 = ttk.Entry(root, font = ("Helvetica", 10), justify="center")
entry11.place(x=105, y=80, width=140, height=23)
entry11.insert(tk.END, "0")

label12 = ttk.Label(root, text="Conversions:", style="S.TLabel")
label12.place(x=15, y=110)

entry12 = ttk.Entry(root, font = ("Helvetica", 10), justify="center")
entry12.place(x=105, y=110, width=140, height=23)
entry12.insert(tk.END, "0")

label2 = tk.Label(root, text="Test group", font=("Helvetica", 12, "bold"), fg="#FB5531")
label2.place(x=15, y=145)

label21 = ttk.Label(root, text="Visitors:", style="S.TLabel")
label21.place(x=15, y=180)

entry21 = ttk.Entry(root, font = ("Helvetica", 10), justify="center")
entry21.place(x=105, y=180, width=140, height=23)
entry21.insert(tk.END, "0")

label22 = ttk.Label(root, text="Conversions:", style="S.TLabel")
label22.place(x=15, y=210)

entry22 = ttk.Entry(root, font = ("Helvetica", 10), justify="center")
entry22.place(x=105, y=210, width=140, height=23)
entry22.insert(tk.END, "0")

btnCalc = ttk.Button(root, text="Calculate", style="W.TButton", command=do_processing)
btnCalc.place(x=18, y=255, width=110, height=30)

btnCloseRoot = ttk.Button(root, text="Close", style="W.TButton", command=root.destroy)
btnCloseRoot.place(x=153, y=255, width=110, height=30)

root.mainloop()