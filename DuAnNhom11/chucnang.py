import tkinter as tk
from tkinter import messagebox

def them_mon(tree, entry_ten, entry_loai, entry_nguyenlieu, entry_thoigian):

    ten = entry_ten.get()
    loai = entry_loai.get()
    nguyenlieu = entry_nguyenlieu.get()
    thoigian = entry_thoigian.get()

    #KIỂM TRA RỖNG
    if (
    ten == "" or
    loai == "" or
    nguyenlieu == "" or
    thoigian == ""
        ):

        messagebox.showwarning(
        "Thông báo",
        "Vui lòng nhập đầy đủ thông tin"
        )

        return

    tree.insert("", tk.END, values=(
        ten,
        loai,
        nguyenlieu,
        thoigian
    ))
    #XÓA NỘI DUNG Ô NHẬP
    entry_ten.delete(0, tk.END)
    entry_loai.delete(0, tk.END)
    entry_nguyenlieu.delete(0, tk.END)
    entry_thoigian.delete(0, tk.END)

def xoa_mon(tree):

    selected = tree.selection()

    if not selected:
        messagebox.showwarning("Thông báo", "Chọn món cần xóa")
        return

    tree.delete(selected)

def sua_mon(tree, entry_ten, entry_loai, entry_nguyenlieu, entry_thoigian):

    selected = tree.selection()

    if not selected:
        messagebox.showwarning("Thông báo", "Chọn món cần sửa")
        return

    tree.item(selected, values=(
        entry_ten.get(),
        entry_loai.get(),
        entry_nguyenlieu.get(),
        entry_thoigian.get()
    ))
#CHỌN MÓN 
def chon_mon(
    event,
    tree,
    entry_ten,
    entry_loai,
    entry_nguyenlieu,
    entry_thoigian
):

    selected = tree.selection()

    if selected:

        values = tree.item(selected[0], "values")

        #HIỆN DỮ LIỆU LÊN Ô NHẬP
        entry_ten.delete(0, tk.END)
        entry_ten.insert(0, values[0])

        entry_loai.delete(0, tk.END)
        entry_loai.insert(0, values[1])

        entry_nguyenlieu.delete(0, tk.END)
        entry_nguyenlieu.insert(0, values[2])

        entry_thoigian.delete(0, tk.END)
        entry_thoigian.insert(0, values[3])