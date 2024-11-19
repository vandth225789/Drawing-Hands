from helpers import calculate_distance, check_clear_button, check_color_button

# Hàm xử lý nhận diện bàn tay và vẽ
def process_hand_landmarks(results, img, all_drawings, current_points, is_drawing, clear_button, color_buttons, frame_width, frame_height, current_color):
    is_clear_pressed = False
    selected_color = None

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Kiểm tra tất cả các ngón để xóa
            for id, lm in enumerate(hand_landmarks.landmark):
                x = int(lm.x * frame_width)
                y = int(lm.y * frame_height)

                # Kiểm tra nút xóa
                if check_clear_button(x, y, *clear_button):
                    is_clear_pressed = True
                    break

                # Kiểm tra nút đổi màu
                selected_color = check_color_button(x, y, color_buttons)
                if selected_color:
                    current_color = selected_color
                    is_drawing = False
                    break

            if is_clear_pressed or selected_color:
                break

            # Chỉ sử dụng ngón trỏ (Index Finger) để vẽ
            x1 = int(hand_landmarks.landmark[8].x * frame_width)  # Ngón trỏ
            y1 = int(hand_landmarks.landmark[8].y * frame_height)

            # Tiếp tục hoặc bắt đầu vẽ
            if not is_drawing:
                current_points.append((x1, y1))
                is_drawing = True
            else:
                current_points.append((x1, y1))

            # Kiểm tra khoảng cách ngón cái và ngón trỏ để dừng vẽ
            thumb_x = int(hand_landmarks.landmark[4].x * frame_width)
            thumb_y = int(hand_landmarks.landmark[4].y * frame_height)
            distance = calculate_distance(x1, y1, thumb_x, thumb_y)

            if distance < 50 and is_drawing:
                all_drawings.append({"points": current_points[:], "color": current_color})
                current_points.clear()
                is_drawing = False

    # Nếu bất kỳ ngón nào chạm vào nút xóa
    if is_clear_pressed:
        all_drawings.clear()
        current_points.clear()
        is_drawing = False

    return all_drawings, current_points, is_drawing, current_color
