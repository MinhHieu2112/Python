import tkinter as tk
from tkinter import Label
from ultralytics import YOLO
import cv2
from PIL import Image, ImageTk
import threading

# Load model YOLO (dùng model nhẹ YOLOv8n)
model = YOLO("yolov8n.pt")

# Biến toàn cục
running = False

def start_detection():
    global running
    running = True
    threading.Thread(target=detect_objects, daemon=True).start()

def stop_detection():
    global running
    running = False

def detect_objects():
    global running
    cap = cv2.VideoCapture(0)  # mở webcam
    while running:
        ret, frame = cap.read()
        if not ret:
            break

        # YOLO inference
        results = model(frame, verbose=False)
        annotated_frame = results[0].plot()  # vẽ bounding boxes

        # Đếm số đối tượng
        num_objects = len(results[0].boxes)

        # Chuyển sang ảnh Tkinter
        cv2image = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)

        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)
        count_label.config(text=f"Đã phát hiện: {num_objects} đối tượng")

    cap.release()

# Tạo GUI Tkinter
root = tk.Tk()
root.title("YOLO Đếm Vật Thể")
root.geometry("800x600")

video_label = Label(root)
video_label.pack()

count_label = Label(root, text="Đã phát hiện: 0 đối tượng", font=("Arial", 16))
count_label.pack(pady=10)

start_button = tk.Button(root, text="Bắt đầu", command=start_detection, bg="green", fg="white")
start_button.pack(side="left", padx=20)

stop_button = tk.Button(root, text="Dừng", command=stop_detection, bg="red", fg="white")
stop_button.pack(side="right", padx=20)

root.mainloop()
