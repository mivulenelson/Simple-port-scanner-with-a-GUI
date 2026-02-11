Port Scanner
A high-performance, multi-threaded TCP port scanner built with Python 3 and PySide6. This tool allows security enthusiasts to audit network hosts for open services with a clean, modern interface.

🚀 Features
Multi-Threaded Engine: Utilizes QThreadPool and QRunnable to perform scans without freezing the GUI.

Smart Interface Detection: A built-in "Refresh IP" feature that automatically detects your local network interface IP.

Flexible Scanning: Support for single port targets or inclusive ranges (e.g., 20-1024).

Real-time Logging: Interactive console that reports findings as they are discovered.

 UI: Custom QSS styling for a high-contrast, auditor-friendly look.

🛠 Project Structure
The project follows a modular architecture to separate business logic from the presentation layer:

Plaintext
PortScanner/
├── main.py                 # Entry point of the application
├── scanner_app/
│   ├── core/               # Networking logic & multithreading
│   ├── ui/                 # PySide6 Windows, Widgets, and Styles
│   └── utils/              # Helper functions and logging
└── requirements.txt        # Dependency list
📦 Installation
Clone the repository:

Bash
git clone https://github.com/yourusername/portscanner.git
cd portscanner
Create a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
🖥 Usage
Run the application from the root directory:

Bash
python main.py
Click Refresh IP to detect your current local IP or type a target manually.

Enter the port range (e.g., 20-445).

Click Start Security Scan.

Use Clear Console to wipe the logs between different targets.

⚙️ Technical Details
Language: Python 3.x

GUI Framework: PySide6 (Qt for Python)

Concurrency: PySide6.QtCore.QThreadPool

Networking: socket (TCP connect_ex method)

⚠️ Disclaimer
This tool is intended for educational and ethical security testing purposes only. Scanning networks or hosts without explicit permission is illegal in many jurisdictions. The author assumes no liability for misuse of this software.

If you want to go the extra mile, take a high-quality screenshot of the running app and save it as screenshot.png in your folder. Then, add this line right under the main title in the README: ![App Screenshot](screenshot.png)

Would you like me to generate similar professional README files for the SecureVault or WebSentinel projects?
