import cv2 ## Cài đặt import thư viện cv2
from pyzbar import pyzbar # py -m pip install pyzbar

# Hàm giải mã QR code
def decode_qr(image):
  # Sử dụng pyzbar để giải mã
  qr_codes = pyzbar.decode(image)
  for qr_code in qr_codes:
    x, y, w, h = qr_code.rect
    # Vẽ khung quanh mã QR
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) # vẽ hình vuông lên mã QR

    # Giải mã QR code và in ra kết quả
    qr_data = qr_code.data.decode("utf-8")
    qr_type = qr_code.type
    print(f"Found {qr_type}: {qr_data}")

    # Hiển thị nội dung mã QR trên hình ảnh
    cv2.putText(image, qr_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

  return image
# Mở camera
cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  if not ret:
    break

  # Giải mã mã QR trong khung hình
  frame = decode_qr(frame)

  # Hiển thị hình ảnh có chứa mã QR
  cv2.imshow("QR Code Scanner", frame)

  # Nhấn 'q' để thoát
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()