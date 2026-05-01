import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as tkagg

# =========================
# BIẾN
# =========================
df = None

# =========================
# WINDOW
# =========================
root = tk.Tk()
root.title("PHÂN TÍCH BÁN HÀNG")
root.geometry("1400x800")

# =========================
# LAYOUT
# =========================
left = tk.Frame(root, bg="#2c3e50", width=250)
left.pack(side="left", fill="y")

right = tk.Frame(root, bg="white")
right.pack(side="right", fill="both", expand=True)

# =========================
# CLEAR
# =========================
def clear():
    for w in right.winfo_children():
        w.destroy()

# =========================
# LOAD FILE
# =========================
def open_file():
    global df

    file = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
    if not file:
        return

    df = pd.read_csv(file, encoding='ISO-8859-1')
    df.columns = df.columns.str.strip()

    # xử lý
    df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
    df = df.dropna(subset=['OrderDate', 'Sales'])

    df['Month'] = df['OrderDate'].dt.month
    df['Year'] = df['OrderDate'].dt.year
    df['Quarter'] = df['OrderDate'].dt.quarter

    messagebox.showinfo("OK", "Đã tải dữ liệu")

# =========================
# VẼ CHART
# =========================
def draw(data, title, kind="bar"):
    clear()

    fig, ax = plt.subplots(figsize=(8,4))

    if kind == "line":
        ax.plot(data.index, data.values, marker='o')
    elif kind == "bar":
        ax.bar(data.index.astype(str), data.values)
    elif kind == "pie":
        ax.pie(data.values, labels=data.index, autopct='%1.1f%%')

    ax.set_title(title)

    canvas = tkagg.FigureCanvasTkAgg(fig, master=right)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# =========================
# CÁC CHỨC NĂNG
# =========================
def month_chart():
    if df is None: return
    data = df.groupby('Month')['Sales'].sum().sort_index()
    draw(data, "Doanh thu theo tháng", "line")

def year_chart():
    if df is None: return
    data = df.groupby('Year')['Sales'].sum()
    draw(data, "Doanh thu theo năm")

def quarter_chart():
    if df is None: return
    data = df.groupby('Quarter')['Sales'].sum()
    draw(data, "Doanh thu theo quý")

def category_chart():
    if df is None: return
    if 'Category' not in df.columns:
        messagebox.showerror("Lỗi", "Không có cột Category")
        return
    data = df.groupby('Category')['Sales'].sum()
    draw(data, "Doanh thu theo loại mặt hàng")

def pie_chart():
    if df is None: return
    data = df.groupby('Category')['Sales'].sum()
    draw(data, "Tỷ lệ doanh thu", "pie")

# =========================
# MENU BUTTON
# =========================
def btn(text, cmd):
    tk.Button(left, text=text, command=cmd,
              bg="#3498db", fg="white",
              font=("Arial", 11, "bold"),
              width=25, pady=6).pack(pady=5)

tk.Label(left, text="MENU", bg="#2c3e50", fg="white",
         font=("Arial", 16, "bold")).pack(pady=10)

btn("Mở file CSV", open_file)
btn("Doanh thu tháng", month_chart)
btn("Doanh thu năm", year_chart)
btn("Doanh thu quý", quarter_chart)
btn("Theo loại mặt hàng", category_chart)
btn("Biểu đồ tròn", pie_chart)

# =========================
# START
# =========================
tk.Label(right, text="MỞ FILE CSV ĐỂ BẮT ĐẦU",
         font=("Arial", 20)).pack(expand=True)

root.mainloop()