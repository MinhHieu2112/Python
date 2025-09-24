from tkinter import *

#Khởi tạo khung window
window = Tk()

#Tiêu đề giao diện
window.title("Giao diện")

#Kích thước giao diện ("Kích thước + tọa độ x, y khi hiển thị")
window.geometry("800x600+300+400")

#Màu sắc background giao diện
window.config(background="white")

#Ẩn icon thay đổi kích thước
window.resizable(False, False)

#Hiển thị giao diện
window.mainloop()