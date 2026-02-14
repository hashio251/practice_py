# omikuji app

import tkinter as tk
import omikuji

def display_label():
  result, message = omikuji.draw_omikuji()
  lbl.configure(text=f"{result}\n{message}")

top_view = tk.Tk() # create display
top_view.geometry("1000x800") # display w*h

lbl = tk.Label(text="ラベル") # create label
btn = tk.Button(text="押してください", command=display_label) # create btn

lbl.pack() # view label
btn.pack() # view btn
tk.mainloop() # view window