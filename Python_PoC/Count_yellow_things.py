import cv2
import numpy as np

#Mở webcam
cap = cv2.VideoCapture(0)

#Định nghĩa màu sắc của đối tượng
lower_color = np.array([20,100,100])
upper_color = np.array([30, 255, 255])

#Biến để đếm sản phẩm có màu vàng
product_count = 0
while True:
    #Đọc từng khung hình từ webcam
    ret, frame = cap.read()

    #Kiểm tra xem khung hình có đọc thành công không
    if not ret:
        print("Không thể đọc từ webcam")
        break

    #Chuyển đổi khung hình sang không gian màu
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Tạo mặt nạ để phát hiện màu sắc
    mask = cv2.inRange(hsv_frame, lower_color, upper_color)

    #Áp dụng một số phép toán hình học để làm sạch mặt nạ
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) #Mở
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) #Đóng

    #Tìm các đường viền trong mặt nạ
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #Nếu có đường viền, vẽ hình chữ nhật và tâm màu đỏ
    if contours:
        product_count = 0 #Đặt lại số lượng sản phẩm

        for contour in contours:
            area = cv2.contourArea(contour) #Tính diện tích contour
            if area > 500: #Lọc theo diện tích
                product_count += 1 #Tăng số lượng sản phẩm

                (x, y, w, h) = cv2.boundingRect(contour) #Tìm tọa độ và kích thước của hình chữ nhật bao quanh

                #Tính toán tọa độ tâm
                center_x = x + w // 2
                center_y = y + h // 2

                #Vẽ hình chữ nhật bao quanh đối tượng
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2) #Vẽ ô vuông màu xanh lá cây

                #Vẽ tâm của đối tượng màu vàng bằng màu đỏ
                cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1) #Vẽ điểm tâm màu đỏ

    #Hiển thị số lượng sản phẩm màu vàng trên khung hình
    cv2.putText(frame, f'San pham mau vang: {product_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    #Hiển thị khung hình có đối tượng được theo dõi
    cv2.imshow('Object Tracking', frame)

    #Thoát nếu nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()


