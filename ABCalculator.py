import tkinter as tk
import tkinter.ttk as ttk
import os

def popup_window():
    window = tk.Toplevel()
    window.geometry("500x500")
    window.title("A/B results")
    
    textOutput = tk.Text(window, font=("Courier New", 10))
    textOutput.place(x=15, y=115, width=470, height=300)
    
    textOutput.insert(tk.END, "                                  Control       Test   " + os.linesep)
    textOutput.insert(tk.END, "                                  group         group  " + os.linesep)
    textOutput.insert(tk.END, "----------------------------------------------------------" + os.linesep)
    
    btnCloseWindow = ttk.Button(window, text="Close", style="W.TButton", command=window.destroy)
    btnCloseWindow.place(x=370, y=455, width=110, height=30)

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
entry11.insert(tk.END, "255")

label12 = ttk.Label(root, text="Conversions:", style="S.TLabel")
label12.place(x=15, y=110)

entry12 = ttk.Entry(root, font = ("Helvetica", 10), justify="center")
entry12.place(x=105, y=110, width=140, height=23)
entry12.insert(tk.END, "26")

label2 = tk.Label(root, text="Test group", font=("Helvetica", 12, "bold"), fg="#FB5531")
label2.place(x=15, y=145)

label21 = ttk.Label(root, text="Visitors:", style="S.TLabel")
label21.place(x=15, y=180)

entry21 = ttk.Entry(root, font = ("Helvetica", 10), justify="center")
entry21.place(x=105, y=180, width=140, height=23)
entry21.insert(tk.END, "235")

label22 = ttk.Label(root, text="Conversions:", style="S.TLabel")
label22.place(x=15, y=210)

entry22 = ttk.Entry(root, font = ("Helvetica", 10), justify="center")
entry22.place(x=105, y=210, width=140, height=23)
entry22.insert(tk.END, "18")

btnCalc = ttk.Button(root, text="Calculate", style="W.TButton", command=popup_window)
btnCalc.place(x=18, y=255, width=110, height=30)

btnCloseRoot = ttk.Button(root, text="Close", style="W.TButton", command=root.destroy)
btnCloseRoot.place(x=153, y=255, width=110, height=30)

root.mainloop()
