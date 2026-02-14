# preview image app

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk


# pthoto view
def display_photo(path):
  new_img = PIL.Image.open(path).convert("L").resize((32, 32)).resize((300, 300), resample=0)
  # convert("L")  monokuro
  # resize((32, 32)) --> resize((300, 300), resample=0  mozaiku（画像を縮小してから拡大してリサイズすることでピクセルが落ちてモザイク風に）
  img_data = PIL.ImageTk.PhotoImage(new_img)
  img_label.configure(image=img_data)
  img_label.image = img_data

# open
def open_file():
  fd_path = fd.askopenfilename()
  if fd_path:
    display_photo(fd_path)

# display
top_view = tk.Tk()
top_view.geometry("600x400")

btn = tk.Button(text="ファイルを開く", command=open_file)
img_label = tk.Label()
btn.pack()
img_label.pack()
tk.mainloop()
