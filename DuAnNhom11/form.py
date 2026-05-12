# ===== FILE: form.py =====

import tkinter as tk
from tkinter import ttk
from chucnang import chon_mon
def tao_form(
    root,
    them_mon,
    sua_mon,
    xoa_mon,
    thong_ke
):
    dang_them = False
    def set_dang_them():

        nonlocal dang_them

        dang_them = True
    #STYLE 
    style = ttk.Style()

    style.theme_use("default")

    style.configure(
        "Treeview",
        background="white",
        foreground="black",
        rowheight=30,
        fieldbackground="white",
        font=("Arial", 10)
    )

    style.configure(
        "Treeview.Heading",
        font=("Arial", 11, "bold")
    )

    #TIÊU ĐỀ 
    title = tk.Label(
        root,
        text="QUẢN LÝ MÓN ĂN",
        font=("Arial", 24, "bold"),
        bg="#F5F5F5",
        fg="#2E7D32"
    )

    title.pack(pady=20)

    #FRAME INPUT 
    frame_input = tk.Frame(
        root,
        bg="white",
        bd=2,
        relief="groove"
    )

    frame_input.pack(
        pady=10
    )

    #LABEL 
    font_label = ("Arial", 11)

    #TÊN MÓN 
    tk.Label(
        frame_input,
        text="Tên món",
        bg="white",
        font=font_label
    ).grid(row=0, column=0, padx=5, pady=10)

    entry_ten = tk.Entry(
        frame_input,
        width=18,
        font=("Arial", 11)
    )

    entry_ten.grid(row=0, column=1, padx=5)

    #LOẠI MÓN
    tk.Label(
        frame_input,
        text="Loại món",
        bg="white",
        font=font_label
    ).grid(row=1, column=0, padx=5, pady=10)

    entry_loai = tk.Entry(
        frame_input,
        width=18,
        font=("Arial", 11)
    )

    entry_loai.grid(row=1, column=1, padx=5)

    #NGUYÊN LIỆU 
    tk.Label(
        frame_input,
        text="Nguyên liệu",
        bg="white",
        font=font_label
    ).grid(row=0, column=2, padx=5, pady=10)

    entry_nguyenlieu = tk.Entry(
        frame_input,
        width=18,
        font=("Arial", 11)
    )

    entry_nguyenlieu.grid(row=0, column=3, padx=5)

    #THỜI GIAN
    tk.Label(
        frame_input,
        text="Thời gian",
        bg="white",
        font=font_label
    ).grid(row=1, column=2, padx=5, pady=10)

    entry_thoigian = tk.Entry(
        frame_input,
        width=18,
        font=("Arial", 11)
    )

    entry_thoigian.grid(row=1, column=3, padx=5)

    #FRAME NÚT 
    frame_btn = tk.Frame(
        root,
        bg="#F5F5F5"
    )

    frame_btn.pack(pady=15)
    
    
    #NÚT THÊM 
    btn_them = tk.Button(
        frame_btn,
        text="Thêm",
        width=12,
        bg="#4CAF50",
        fg="black",
        font=("Arial", 10, "bold"),
        relief="flat",
        command=lambda: 
            [set_dang_them(),
            them_mon(
                tree,
                entry_ten,
                entry_loai,
                entry_nguyenlieu,
                entry_thoigian
        )]
    )

    btn_them.grid(row=0, column=0, padx=8)

    #NÚT SỬA
    btn_sua = tk.Button(
        frame_btn,
        text="Sửa",
        width=12,
        bg="#FF9800",
        fg="black",
        font=("Arial", 10, "bold"),
        relief="flat",
        command=lambda: sua_mon(
            tree,
            entry_ten,
            entry_loai,
            entry_nguyenlieu,
            entry_thoigian
        )
    )

    btn_sua.grid(row=0, column=1, padx=8)

    #NÚT XÓA 
    btn_xoa = tk.Button(
        frame_btn,
        text="Xóa",
        width=12,
        bg="#C65850",
        fg="black",
        font=("Arial", 10, "bold"),
        relief="flat",
        command=lambda: xoa_mon(tree)
    )

    btn_xoa.grid(row=0, column=2, padx=8)

    #NÚT THỐNG KÊ
    btn_thongke = tk.Button(
        frame_btn,
        text="Thống kê",
        width=12,
        bg="#2196F3",
        fg="black",
        font=("Arial", 10, "bold"),
        relief="flat",
        command=lambda: thong_ke(tree)
    )

    btn_thongke.grid(row=0, column=3, padx=8)

    #FRAME BẢNG 
    frame_table = tk.Frame(
        root,
        bg="white",
        bd=2,
        relief="groove"
    )

    frame_table.pack(
        padx=15,
        pady=15,
        fill="both",
        expand=True
    )

    #CỘT
    columns = (
        "Tên món",
        "Loại món",
        "Nguyên liệu",
        "Thời gian"
    )

    tree = ttk.Treeview(
        frame_table,
        columns=columns,
        show="headings",
        height=10
    )

    for col in columns:

        tree.heading(col, text=col)

        tree.column(
            col,
            width=180,
            anchor="center"
        )

    tree.pack(fill="both", expand=True)
    def chon_mon_wrapper(event):

        nonlocal dang_them

        if dang_them:
            dang_them = False
            return

        chon_mon(
            event,
            tree,
            entry_ten,
            entry_loai,
            entry_nguyenlieu,
            entry_thoigian
        )

    tree.bind(
        "<<TreeviewSelect>>",
        chon_mon_wrapper
    )
    return tree