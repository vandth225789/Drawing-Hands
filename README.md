# Ứng Dụng Vẽ Bằng Cử Chỉ Bàn Tay Python, OpenCV và MediaPipe

Dự án này là một ứng dụng vẽ tay sử dụng webcam để nhận diện cử chỉ tay và vẽ trên màn hình. Ứng dụng cung cấp các chức năng như xóa màn hình, thay đổi màu vẽ và bắt đầu/dừng vẽ bằng các cử chỉ đơn giản.

## Tính Năng

- **Nhận Diện Cử Chỉ Tay**: Sử dụng ngón trỏ để vẽ và dừng vẽ khi đưa ngón cái lại gần ngón trỏ.
- **Vẽ Động**: Vẽ các đường liên tục dựa trên vị trí được nhận diện từ tay.
- **Chọn Màu Vẽ**: Thay đổi màu vẽ bằng các nút màu trên màn hình.
- **Xóa Màn Hình**: Xóa toàn bộ hình vẽ bằng nút xóa.
- **Tùy Chỉnh Dễ Dàng**: Điều chỉnh kích thước khung hình, màu sắc và các thiết lập khác trong `config.py`.

---

## Cấu Trúc Dự Án
**Ứng Dụng Vẽ Bằng Cử Chỉ Bàn Tay**
**├── config.py # Chứa các thiết lập và hàm khởi tạo. **
**├── drawing.py # Xử lý nhận diện bàn tay và logic vẽ. **
**├── helpers.py # Các hàm tiện ích hỗ trợ vẽ và tương tác. **
**├── main.py # Chương trình chính và vòng lặp xử lý. **
**└── requirements.txt # Danh sách các thư viện cần cài đặt.**


---

## Hướng Dẫn Cài Đặt

1. **Clone Repository**:
   ```bash
   git clone https://github.com/your-repo/drawing-app.git
   cd drawing-app
2. **Cài Đặt Thư Viện: Sử dụng tệp requirements.txt để cài đặt các thư viện cần thiết**:
   ```bash
   pip install -r requirements.txt
3. **Chạy Ứng Dụng**:
    ```bash
   python main.py

