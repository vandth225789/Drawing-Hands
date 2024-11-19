# Ứng Dụng Vẽ Bằng Cử Chỉ Bàn Tay Python, OpenCV và MediaPipe

Dự án này là một ứng dụng vẽ tay sử dụng webcam để nhận diện cử chỉ tay và vẽ trên màn hình. Ứng dụng cung cấp các chức năng như xóa màn hình, thay đổi màu vẽ và bắt đầu/dừng vẽ bằng các cử chỉ đơn giản.

---

[![Xem Tài Liệu](https://img.shields.io/badge/Xem-Tài%20Liệu-green)](https://docs.google.com/document/d/12OOda6gAK0OvTL3b-nwiLH6AVl8bIGBD-68NNF4BEkA/edit?tab=t.0)

---


## Tính Năng

- **Nhận Diện Cử Chỉ Tay**: Sử dụng ngón trỏ để vẽ và dừng vẽ khi đưa ngón cái lại gần ngón trỏ.
- **Vẽ Động**: Vẽ các đường liên tục dựa trên vị trí được nhận diện từ tay.
- **Chọn Màu Vẽ**: Thay đổi màu vẽ bằng các nút màu trên màn hình.
- **Xóa Màn Hình**: Xóa toàn bộ hình vẽ bằng nút xóa.
- **Tùy Chỉnh Dễ Dàng**: Điều chỉnh kích thước khung hình, màu sắc và các thiết lập khác trong `config.py`.

---

## Ứng Dụng Vẽ Bằng Cử Chỉ Bàn Tay

- **`config.py`**: Chứa các thiết lập và hàm khởi tạo.
- **`drawing.py`**: Xử lý nhận diện bàn tay và logic vẽ.
- **`helpers.py`**: Các hàm tiện ích hỗ trợ vẽ và tương tác.
- **`main.py`**: Chương trình chính và vòng lặp xử lý.
- **`requirements.txt`**: Danh sách các thư viện cần cài đặt.



---

## Hướng Dẫn Cài Đặt

1. **Clone Repository**:
   ```bash
   git clone https://github.com/vandth225789/Drawing-Hands/
   cd Drawing-Hands
2. **Cài Đặt Thư Viện: Sử dụng tệp requirements.txt để cài đặt các thư viện cần thiết**:
   ```bash
   pip install -r requirements.txt
3. **Chạy Ứng Dụng**:
    ```bash
   python main.py

---

## Cách Hoạt Động

### **Cấu Hình (`config.py`)**
- **Kích Thước Khung Hình**: Điều chỉnh `FRAME_WIDTH` và `FRAME_HEIGHT` để thay đổi kích thước khung hình của webcam.
- **Nút Màu**: Tùy chỉnh `COLOR_BUTTONS` để thêm hoặc thay đổi các tùy chọn màu sắc.
- **Nút Xóa**: Sử dụng `CLEAR_BUTTON` để định vị lại nút xóa.

### **Logic Chính (`main.py`)**
- Quay video từ webcam.
- Xử lý các điểm bàn tay bằng MediaPipe Hands.
- Hiển thị và quản lý các phần tử vẽ trên màn hình.

### **Logic Vẽ (`drawing.py`)**
- Nhận diện cử chỉ tay để bắt đầu, dừng hoặc xóa các nét vẽ.
- Nhận diện tay khi tương tác với nút màu hoặc nút xóa.

### **Hàm Tiện Ích (`helpers.py`)**
- Bao gồm các hàm hỗ trợ vẽ hình, tính khoảng cách và nhận diện nút.

---

## Hướng Dẫn Sử Dụng

- **Bắt Đầu Vẽ**: Di chuyển ngón trỏ.
- **Dừng Vẽ**: Đưa ngón cái lại gần ngón trỏ.
- **Xóa Màn Hình**: Nhấn nút "Clear".
- **Thay Đổi Màu**: Nhấn vào một trong các nút màu trên màn hình.

---

## Yêu Cầu Hệ Thống

- **Python**: 3.7 trở lên.
- **Webcam**: Để nhận diện tay.
- **Iriun Webcam**: Có thể dùng liên kết với điện thoại thay thế Webcam hệ thống.

### Các thư viện cần thiết:
- `opencv-python`
- `mediapipe`
- `numpy`

## Nâng Cấp Trong Tương Lai

- Thêm nhiều tùy chọn màu sắc.
- Hỗ trợ lưu và tải hình vẽ.
- Thêm các cử chỉ tay nâng cao để điều khiển ứng dụng.
- Tối ưu hóa hiệu suất cho các thiết bị cấu hình thấp.

---

## Cảm Ơn

- **OpenCV**: Xử lý hình ảnh và khả năng vẽ.
- **MediaPipe**: Nhận diện cử chỉ tay.

Bạn có thể tùy chỉnh và nâng cấp dự án theo nhu cầu. Chúng tôi hoan nghênh mọi đóng góp!


