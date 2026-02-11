import sys
import os
from PySide6.QtWidgets import QApplication

# this adds the current dir to the path so python can find any file 
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from ui.main_window import MainWindow
    print("[DEBUG] Imports successful")
except ImportError as e:
    print(f"[DEBUG] Import Error: {e}")
    sys.exit(1)

def main():
    app = QApplication(sys.argv)
    print("[DEBUG] QApplication started")

    stylepath = os.path.join(os.path.dirname(__file__), "ui", "style.qss")

    if os.path.exists(stylepath):
        with open(stylepath, "r") as f:
            app.setStyleSheet(f.read())
            print("[DEBUG] Stylesheet loaded")

    else:
        print(f"[DEBUG] Stylesheet not found at {stylepath}")

    try:
        window = MainWindow()
        window.show()
        print("[DEBUG] Window shown")
        sys.exit(app.exec())
    except Exception as e:
        print(f"[DEBUG] Runtime Error: {e}")
    finally:
        print(f"[DEBUG] Application shutting down")

if __name__ == "__main__":
    main()