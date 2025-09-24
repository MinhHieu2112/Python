# ======================
# 1. Khai báo
# ======================
import cv2

# URL của camera điện thoại (IP thật từ app)
URL = "http://192.168.31.196:8080"

# ======================
# 2. main()
# ======================
def main():
    cap = cv2.VideoCapture(URL)  # Mở stream từ điện thoại

    if not cap.isOpened():
        print("Không thể kết nối tới camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Không nhận được frame từ camera.")
            break

        cv2.imshow("Phone Camera", frame)

        # Nhấn 'q' để thoát
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# ======================
# 3. Chạy chương trình
# ======================
if __name__ == "__main__":
    main()

