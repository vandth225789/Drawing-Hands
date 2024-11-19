import cv2
import numpy as np

# Tính khoảng cách giữa hai điểm
def calculate_distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Vẽ các đoạn thẳng
def draw_lines(img, drawing):
    points = drawing["points"]
    color = drawing["color"]
    for i in range(1, len(points)):
        cv2.line(img, tuple(points[i-1]), tuple(points[i]), color, 5)

# Vẽ nút xóa
def draw_clear_button(img, x, y, w, h):
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), -1)
    cv2.putText(img, 'Clear', (x + 20, y + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# Vẽ các nút màu
def draw_color_buttons(img, buttons):
    for button in buttons:
        color = button["color"]
        x, y, w, h = button["position"]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, -1)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)  # Viền trắng

# Kiểm tra nút xóa được nhấn
def check_clear_button(x, y, button_x, button_y, button_w, button_h):
    return button_x < x < button_x + button_w and button_y < y < button_y + button_h

# Kiểm tra nút màu được nhấn
def check_color_button(x, y, buttons):
    for button in buttons:
        bx, by, bw, bh = button["position"]
        if bx < x < bx + bw and by < y < by + bh:
            return button["color"]
    return None

# Hàm hiển thị màu hiện tại
def show_current_color(img, color, position=(400, 40)):
    cv2.putText(
        img,
        f"My Color:",
        (position[0], position[1]),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),  # Màu chữ (trắng)
        1,
        cv2.LINE_AA
    )
    # Vẽ ô màu bên cạnh text
    cv2.rectangle(
        img,
        (position[0] + 120, position[1] - 15),
        (position[0] + 150, position[1] + 5),
        color,
        -1,
    )