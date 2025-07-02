import cv2
import mediapipe as mp
import pyautogui
import time
from collections import deque
import pygetwindow as gw

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.75)

# Initialize webcam
cap = cv2.VideoCapture(0)

# Gesture movement buffers
x_history = deque(maxlen=5)
y_history = deque(maxlen=5)

# Cooldown setup
cooldown = 1.0
last_action_time = 0

# Set OpenCV window to be always on top
cv2.namedWindow("Gesture Controller", cv2.WINDOW_NORMAL)

# Function: detect only index finger up
def is_only_index_up(hand_landmarks):
    finger_tips = [4, 8, 12, 16, 20]
    finger_pips = [2, 6, 10, 14, 18]

    fingers = []
    for tip, pip in zip(finger_tips, finger_pips):
        tip_y = hand_landmarks.landmark[tip].y
        pip_y = hand_landmarks.landmark[pip].y
        fingers.append(tip_y < pip_y)

    return fingers[1] and not any(fingers[2:])  # Index finger only

while True:
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(img_rgb)
    gesture = "🖐️ Show only index finger"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if is_only_index_up(hand_landmarks):
                x = int(hand_landmarks.landmark[8].x * w)
                y = int(hand_landmarks.landmark[8].y * h)

                x_history.append(x)
                y_history.append(y)

                cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
                cv2.putText(img, f"Index: ({x},{y})", (x+20, y-20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)

                if len(x_history) == 5 and time.time() - last_action_time > cooldown:
                    dx = x_history[-1] - x_history[0]
                    dy = y_history[-1] - y_history[0]

                    if abs(dx) > 80 and abs(dx) > abs(dy):
                        if dx > 0:
                            pyautogui.keyDown('alt')
                            pyautogui.press('tab')
                            pyautogui.keyUp('alt')
                            gesture = "➡️ Switched to next app"
                        else:
                            pyautogui.keyDown('alt')
                            pyautogui.keyDown('shift')
                            pyautogui.press('tab')
                            pyautogui.keyUp('shift')
                            pyautogui.keyUp('alt')
                            gesture = "⬅️ Switched to previous app"
                        last_action_time = time.time()
                        x_history.clear()
                        y_history.clear()

                    elif abs(dy) > 80 and abs(dy) > abs(dx):
                        if dy > 0:
                            pyautogui.scroll(-500)  # Scroll Down
                            gesture = "⬇️ Scroll Down"
                        else:
                            pyautogui.scroll(500)   # Scroll Up
                            gesture = "⬆️ Scroll Up"

                        last_action_time = time.time()
                        x_history.clear()
                        y_history.clear()
            else:
                x_history.clear()
                y_history.clear()

    else:
        x_history.clear()
        y_history.clear()

    # Show gesture feedback
    cv2.putText(img, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 200, 50), 2)
    cv2.imshow("Gesture Controller", img)

    # 🔒 Make window always stay on top
    try:
        win = gw.getWindowsWithTitle("Gesture Controller")[0]
        win.alwaysOnTop = True
    except:
        pass

    # Quit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
