import tkinter as tk

from form import tao_form
from chucnang import *
from thongke import thong_ke

root = tk.Tk()

root.title("Quản Lý Món Ăn")
root.geometry("900x600")
root.configure(bg="#F5F5F5")

tao_form(
    root,
    them_mon,
    sua_mon,
    xoa_mon,
    thong_ke
)

root.mainloop()