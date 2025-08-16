# ✋💡 Hand Gesture Controlled Screen Brightness

A Python project that lets you control your **screen brightness using hand gestures** via your webcam.  
It uses **MediaPipe** for hand tracking, **OpenCV** for video processing, and **WMI** to adjust brightness on Windows.

---

## 🚀 Features
- Detects hand landmarks in **real-time** using MediaPipe.
- Controls **screen brightness** by measuring distance between thumb and index finger.
- Displays **live brightness percentage** and visual bar on screen.
- Shows **FPS counter** for performance monitoring.
- Works with both **left and right hands**.

---

## 🛠️ Tech Stack
- [Python 3.x](https://www.python.org/)
- [OpenCV](https://opencv.org/) - For webcam feed & drawing
- [MediaPipe](https://developers.google.com/mediapipe) - For hand tracking
- [NumPy](https://numpy.org/) - For mathematical operations
- [WMI](https://pypi.org/project/WMI/) - For controlling Windows brightness

---

## 📂 Project Structure
```
├── hand_tracking_module.py   # Utility class for hand detection & landmark extraction
├── brightness_control.py     # Main script to control brightness using gestures
└── README.md                 # Project documentation
```

---

## ⚙️ Installation & Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate    # On Windows
   ```

3. Install required dependencies:
   ```bash
   pip install opencv-python mediapipe numpy wmi
   ```

---

## ▶️ Running the Program

Run the following command from the project directory:
```bash
python brightness_control.py
```

---

## 🎮 How It Works
1. Show your **hand** to the webcam.
2. The program detects **thumb tip (id 4)** and **index finger tip (id 8)**.
3. The **distance between them** is mapped to a brightness value.
   - Fingers close together → Low brightness.
   - Fingers far apart → High brightness.
4. The system brightness is updated in **real time**.

---

## ⚠️ Limitations
- Works only on **Windows** (due to WMI brightness control).
- Requires a **laptop monitor or supported display** (desktop monitors may not support WMI brightness).
- Webcam required.

---

## 📜 License
This project is licensed under the **MIT License**.
