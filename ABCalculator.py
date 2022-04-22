import tkinter as tk

def popup_window():
    window = tk.Toplevel()
    window.geometry("280x300")
    window.title("A/B results")
    
    btnCloseWindow = tk.Button(window, text="Close", activebackground="#ACACAC", font=("Helvetica", 10, "bold"), command=window.destroy)
    btnCloseWindow.place(x=153, y=255, width=110, height=30)

root = tk.Tk()
root.geometry("280x300")
root.title("A/B Calculator")

title = tk.Label(text="A/B Calculator", font=("Helvetica", 16, "bold"), fg="blue")
title.place(x=65, y=10)

label1 = tk.Label(text="Control group", font=("Helvetica", 12, "bold"), fg="#5C18BF")
label1.place(x=15, y=45)

label11 = tk.Label(text="Visitors:", font=("Helvetica", 10), fg="#1D0046")
label11.place(x=15, y=80)

entry11 = tk.Entry(font = ("Helvetica", 10))
entry11.place(x=105, y=80, width=140, height=23)

label12 = tk.Label(text="Conversions:", font=("Helvetica", 10), fg="#1D0046")
label12.place(x=15, y=110)

entry12 = tk.Entry(font = ("Helvetica", 10))
entry12.place(x=105, y=110, width=140, height=23)

label2 = tk.Label(text="Test group", font=("Helvetica", 12, "bold"), fg="#FB5531")
label2.place(x=15, y=145)

label21 = tk.Label(text="Visitors:", font=("Helvetica", 10), fg="#1D0046")
label21.place(x=15, y=180)

entry21 = tk.Entry(font = ("Helvetica", 10))
entry21.place(x=105, y=180, width=140, height=23)

label22 = tk.Label(text="Conversions:", font=("Helvetica", 10), fg="#1D0046")
label22.place(x=15, y=210)

entry22 = tk.Entry(font = ("Helvetica", 10))
entry22.place(x=105, y=210, width=140, height=23)

btnCalc = tk.Button(root, text="Calculate", activebackground="#ACACAC", font=("Helvetica", 10, "bold"), command=popup_window)
btnCalc.place(x=18, y=255, width=110, height=30)

btnCloseRoot = tk.Button(root, text="Close", activebackground="#ACACAC", font=("Helvetica", 10, "bold"), command=root.destroy)
btnCloseRoot.place(x=153, y=255, width=110, height=30)

root.mainloop()
