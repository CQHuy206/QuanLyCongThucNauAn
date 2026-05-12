import pandas as pd
from tkinter import messagebox
def thong_ke(tree):
    data = []
    #LẤY DỮ LIỆU TỪ BẢNG 
    for item in tree.get_children():
        values = tree.item(item, "values")
        data.append(values)
    #KIỂM TRA 
    if len(data) == 0:
        messagebox.showinfo(
            "Thống kê",
            "Chưa có dữ liệu"
        )
        return
    #TẠO DATAFRAME 
    df = pd.DataFrame(
        data,
        columns=[
            "Tên món",
            "Loại món",
            "Nguyên liệu",
            "Thời gian"
        ]
    )
    #THỐNG KÊ
    tong_mon = len(df)
    thongke_loai = df["Loại món"].value_counts()
    #TẠO CHUỖI HIỂN THỊ 
    ketqua = f"Tổng số món ăn: {tong_mon}\n\n"
    ketqua += "Thống kê loại món:\n"
    for loai, soluong in thongke_loai.items():
        ketqua += f"- {loai}: {soluong}\n"
    #HIỂN THỊ 
    messagebox.showinfo(
        "Thống kê",
        ketqua
    )