from config import initialize_webcam, initialize_mediapipe, FRAME_WIDTH, FRAME_HEIGHT, CLEAR_BUTTON, COLOR_BUTTONS
from helpers import draw_clear_button, draw_lines, draw_color_buttons, show_current_color, cv2
from drawing import process_hand_landmarks

# Khởi tạo
cap = initialize_webcam()
hands, mp_draw = initialize_mediapipe()

# Danh sách vẽ
all_drawings = []  # Lưu tất cả các đoạn vẽ (mỗi đoạn là {"points": [...], "color": ...})
current_points = []  # Điểm của đoạn vẽ hiện tại
is_drawing = False

# Màu mặc định
current_color = (0, 255, 0)  # Xanh

# Vòng lặp chính
while True:
    ret, img = cap.read()
    if not ret:
        break

    # Chuyển khung hình sang RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    # Vẽ các đoạn cũ
    for drawing in all_drawings:
        draw_lines(img, drawing)

    # Vẽ nút xóa
    draw_clear_button(img, *CLEAR_BUTTON)

    # Vẽ các nút màu
    draw_color_buttons(img, COLOR_BUTTONS)

    # Hiển thị màu hiện tại
    show_current_color(img, current_color)

    # Xử lý bàn tay
    all_drawings, current_points, is_drawing, current_color = process_hand_landmarks(
        results, img, all_drawings, current_points, is_drawing, CLEAR_BUTTON, COLOR_BUTTONS, FRAME_WIDTH, FRAME_HEIGHT, current_color
    )

    # Vẽ đoạn hiện tại
    if current_points:
        draw_lines(img, {"points": current_points, "color": current_color})

    # Hiển thị
    cv2.imshow("Drawing", img)

    # Thoát khi nhấn 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
