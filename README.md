<h1 align="center">🤖 SmartGestureControl</h1>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=24&pause=1000&color=9B59B6&center=true&vCenter=true&width=750&lines=Control+Your+PC+with+Index+Finger;Swipe,+Scroll+and+Switch+Apps;No+Mouse+or+Touch+Needed" alt="Typing SVG" />
</p>


---

## 📌 Overview

**SmartGestureControl** is an AI-powered real-time hand gesture recognition system that transforms your webcam into a touchless computer control interface.

Using advanced hand-tracking technology from **MediaPipe**, computer vision through **OpenCV**, and desktop automation via **PyAutoGUI**, users can interact with their PC using simple index-finger gestures.

The project eliminates the need for traditional mouse interactions and provides a futuristic, hands-free computing experience.

---

## 🎯 Problem Statement

Traditional computer interaction relies heavily on physical devices such as mice, touchpads, and touchscreens.

SmartGestureControl offers:

* Contactless interaction
* Improved accessibility
* Natural gesture-based control
* Enhanced productivity
* Human-computer interaction using AI

---

## ✨ Features

### 🖐️ Real-Time Hand Tracking

* Detects and tracks hand landmarks with high accuracy
* Works using a standard webcam or mobile camera

### 🔄 Gesture-Based Application Switching

Move your index finger horizontally:

➡️ Right Swipe → Next Application

⬅️ Left Swipe → Previous Application

Simulates:

```text
Alt + Tab
```

---

### 📜 Smart Scrolling

Move your index finger vertically:

⬆️ Up Gesture → Scroll Up

⬇️ Down Gesture → Scroll Down

Useful for:

* Web Browsing
* PDFs
* Documentation
* Presentations

---

### 🎥 Floating Camera Window

* Always-on-top webcam feed
* Live gesture visualization
* Real-time tracking feedback
* Easy monitoring while multitasking

---

### ⚡ Lightweight & Fast

* Low latency gesture detection
* Real-time processing
* Minimal resource consumption

---

## 🏗️ System Architecture

```text
Webcam Feed
      │
      ▼
   OpenCV
      │
      ▼
  MediaPipe
 Hand Tracking
      │
      ▼
 Gesture Detection
      │
      ▼
  PyAutoGUI
      │
      ▼
 PC Actions
(Scroll / App Switch)
```

---

## 🛠️ Tech Stack

| Technology  | Purpose                 |
| ----------- | ----------------------- |
| Python      | Core Development        |
| OpenCV      | Video Processing        |
| MediaPipe   | Hand Landmark Detection |
| PyAutoGUI   | Desktop Automation      |
| PyGetWindow | Window Management       |

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/SmartGestureControl.git

cd SmartGestureControl
```

### 2️⃣ Install Dependencies

```bash
pip install opencv-python mediapipe pyautogui pygetwindow
```

### 3️⃣ Run the Application

```bash
python main.py
```

---

## 🚀 How It Works

1. Launch the application.
2. Webcam starts capturing video.
3. MediaPipe detects hand landmarks.
4. Index finger movements are tracked.
5. Gestures are interpreted in real time.
6. Corresponding desktop actions are executed.

---

## 📸 Demo Screenshots

### Hand Detection

```text
[ Add Screenshot Here ]
```

### Swipe Gesture Detection

```text
[ Add Screenshot Here ]
```

### Scroll Gesture Detection

```text
[ Add Screenshot Here ]
```

---

## 🎮 Supported Gestures

| Gesture     | Action             |
| ----------- | ------------------ |
| Swipe Right | Switch Application |
| Swipe Left  | Switch Application |
| Move Up     | Scroll Up          |
| Move Down   | Scroll Down        |

---

## 📂 Project Structure

```text
SmartGestureControl/
│
├── main.py
├── requirements.txt
├── README.md
├── assets/
│   ├── screenshots/
│   └── demo.gif
│
└── modules/
    ├── hand_tracker.py
    ├── gesture_detector.py
    └── controller.py
```

---

## 🔮 Future Enhancements

* 🎤 Voice Command Integration
* 🖱️ Full Mouse Cursor Control
* ✌️ Multi-Gesture Recognition
* 📊 Gesture Analytics Dashboard
* 🎮 Gaming Gesture Controls
* 🤖 AI-Based Personalized Gestures

---

## 🌟 Applications

* Accessibility Solutions
* Smart Presentations
* Contactless Computing
* Interactive Kiosks
* Education & Learning
* Productivity Enhancement

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Khushanuma Shabbir Mansuri**

B.Tech Information Technology
NMIMS MPSTME

If you found this project useful, don't forget to ⭐ the repository!
