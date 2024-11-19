import cv2
import mediapipe as mp
import os

# Kích thước khung hình
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Nút xóa
CLEAR_BUTTON = (20, 20, 100, 40)

# Nút đổi màu
COLOR_BUTTONS = [
    {"color": (0, 0, 255), "position": (140, 20, 40, 40)},  # Đỏ (BGR: Blue = 0, Green = 0, Red = 255)
    {"color": (0, 255, 0), "position": (200, 20, 40, 40)},  # Xanh (BGR: Blue = 0, Green = 255, Red = 0)
    {"color": (0, 255, 255), "position": (260, 20, 40, 40)},  # Vàng (BGR: Blue = 0, Green = 255, Red = 255)
]

# Hàm khởi tạo webcam
def initialize_webcam():
    cap = cv2.VideoCapture(0)
    cap.set(3, FRAME_WIDTH)
    cap.set(4, FRAME_HEIGHT)
    cap.set(10, 150)  # Độ sáng
    return cap

# Hàm khởi tạo MediaPipe Hands
def initialize_mediapipe():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils
    return hands, mp_draw
