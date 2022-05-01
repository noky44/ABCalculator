import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mb
import os
import math
from scipy.stats import norm

def num_percent(num):
    return "{:.2f}".format(num*100).rjust(10) + "%"

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
    window.geometry("500x500")
    window.title("A/B results")
    
    textOutput = tk.Text(window, font=("Courier New", 10))
    textOutput.place(x=15, y=115, width=470, height=300)
    
    textOutput.insert(tk.END, "                                  Control       Test   " + os.linesep)
    textOutput.insert(tk.END, "                                  group         group  " + os.linesep)
    textOutput.insert(tk.END, "---------------------------------------------------------" + os.linesep)
    
    p1 = c1/n1
    p2 = c2/n2
    textOutput.insert(tk.END, "Conversion                   " + num_percent(p1) +"  "+ num_percent(p2) + os.linesep)
    
    sigma1 = math.sqrt(p1*(1-p1)/n1)
    sigma2 = math.sqrt(p2*(1-p2)/n2)
    textOutput.insert(tk.END, "Standard deviation           " + num_percent(sigma1) +"  "+ num_percent(sigma2) + os.linesep)
    
    textOutput.insert(tk.END, "---------------------------------------------------------" + os.linesep)
    
    #Add output of possible distributions
    z1 = 1.96
    lower1_95 = p1-z1*sigma1
    if lower1_95 < 0:
        lower1_95 = 0
    upper1_95 = p1+z1*sigma1
    if upper1_95 > 1:
        upper1_95 = 1
    
    lower2_95 = p2-z1*sigma2
    if lower2_95 < 0:
        lower2_95 = 0
    upper2_95 = p2+z1*sigma2
    if upper2_95 > 1:
        upper2_95 = 1
    
    textOutput.insert(tk.END, "95% possible distribution    " + os.linesep)
    textOutput.insert(tk.END, "                     from    " + num_percent(lower1_95) +"  "+ num_percent(lower2_95) + os.linesep)
    textOutput.insert(tk.END, "                       to    " + num_percent(upper1_95) +"  "+ num_percent(upper2_95) + os.linesep)
    textOutput.insert(tk.END, "---------------------------------------------------------" + os.linesep)
    
    z2 = 2.525
    lower1_99 = p1-z2*sigma1
    if lower1_99 < 0:
        lower1_99 = 0
    upper1_99 = p1+z2*sigma1
    if upper1_99 > 1:
        upper1_99 = 1
    
    lower2_99 = p2-z2*sigma2
    if lower2_99 < 0:
        lower2_99 = 0
    upper2_99 = p2+z2*sigma2
    if upper2_99 > 1:
        upper2_959 = 1
    
    textOutput.insert(tk.END, "99% possible distribution    " + os.linesep)
    textOutput.insert(tk.END, "                     from    " + num_percent(lower1_99) +"  "+ num_percent(lower2_99) + os.linesep)
    textOutput.insert(tk.END, "                       to    " + num_percent(upper1_99) +"  "+ num_percent(upper2_99) + os.linesep)
    textOutput.insert(tk.END, "---------------------------------------------------------" + os.linesep)
    
    # Calculate Z and P
    z_score = (p2-p1)/math.sqrt(sigma1*sigma1+sigma2*sigma2)
    textOutput.insert(tk.END, "Z = " + "{:.7f}".format(z_score) + os.linesep) 
    
    p_value = norm.sf(x=z_score, loc=0, scale=1)
    textOutput.insert(tk.END, "P = " + "{:.7f}".format(p_value) + os.linesep)
    
    # Add result interpretation
    confidence_95 = False
    if p_value < 0.025 or p_value > 0.975:
        confidence_95 = True
        
    confidence_99 = False
    if p_value < 0.005 or p_value > 0.995:
        confidence_99 = True    
    
    lblComment95 = tk.Label(window, text="95% confidence:", font=("Helvetica", 10, "bold"))
    lblComment95.place(x=25, y=25)
    
    if confidence_95:
        lblResult95 = tk.Label(window, text="YES", font=("Helvetica", 12, "bold"), fg="#008800")
        lblResult95.place(x=160, y=25)
    else:
        lblResult95 = tk.Label(window, text="NO", font=("Helvetica", 12, "bold"), fg="#ff0000")
        lblResult95.place(x=160, y=25)    
    
    lblComment99 = tk.Label(window, text="99% confidence:", font=("Helvetica", 10, "bold"))
    lblComment99.place(x=25, y=65)
    
    if confidence_99:
        lblResult99 = tk.Label(window, text="YES", font=("Helvetica", 12, "bold"), fg="#008800")
        lblResult99.place(x=160, y=65)
    else:
        lblResult99 = tk.Label(window, text="NO", font=("Helvetica", 12, "bold"), fg="#ff0000")
        lblResult99.place(x=160, y=65)
    
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

btnCalc = ttk.Button(root, text="Calculate", style="W.TButton", command=do_processing)
btnCalc.place(x=18, y=255, width=110, height=30)

btnCloseRoot = ttk.Button(root, text="Close", style="W.TButton", command=root.destroy)
btnCloseRoot.place(x=153, y=255, width=110, height=30)

root.mainloop()
