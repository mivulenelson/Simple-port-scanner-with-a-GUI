from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QTextEdit, QLabel )
from PySide6.QtCore import QThreadPool
from core.engine import PortScannerEngine
import socket


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Port Scanner")
        self.setMinimumSize(900, 500)
        self.threadpool = QThreadPool()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # IP input section with refresh
        ip_label_layout = QHBoxLayout()
        ip_label_layout.addWidget(QLabel("Target IP Address:"))

        self.refresh_btn = QPushButton("Refresh IP")
        self.refresh_btn.setFixedWidth(100)
        self.refresh_btn.setStyleSheet("background-color: #444; font-size: 10px;")
        ip_label_layout.addWidget(self.refresh_btn)

        layout.addLayout(ip_label_layout)
        self.ip_input = QLineEdit(self.get_local_ip())
        layout.addWidget(self.ip_input)

        # port range section
        layout.addWidget(QLabel("Port Range (e.g., 0-65535)"))
        self.port_range = QLineEdit("0-65535")
        layout.addWidget(self.port_range)

        # action buttons
        button_layout = QHBoxLayout()
        self.scan_btn = QPushButton("Start Port Scan")
        self.clear_btn = QPushButton("Clear Console")
        self.clear_btn.setStyleSheet("background-color: #d9534f;")

        button_layout.addWidget(self.scan_btn)
        button_layout.addWidget(self.clear_btn)
        layout.addLayout(button_layout)

        # output console
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        layout.addWidget(self.console)

        # signal connections
        self.scan_btn.clicked.connect(self.start_scan)
        self.clear_btn.clicked.connect(self.console.clear)
        self.refresh_btn.clicked.connect(self.update_ip_field)

    # logic to find the user's current network interface IP
    def get_local_ip(self):
        try:
            # connect to an external dummy address to see which interface the Os uses
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            return local_ip
        except Exception:
            return "127.0.0.1"
        
    def update_ip_field(self):
        new_ip = self.get_local_ip()
        self.ip_input.setText(new_ip)
        self.console.append(f"[*] Interface refreshed. Local IP detected: {new_ip}")

        
    def start_scan(self):
        target = self.ip_input.text().strip()
        port_text = self.port_range.text().strip()
        
        try:
            if "-" in port_text:
                r_start, r_end = map(int, port_text.split("-"))
                ports = range(r_start, r_end + 1)
            else:
                ports = [int(port_text)]
        except ValueError:
            self.console.append(f"[!] Invalid port range.")
            return
        self.console.append(f"[*] Starting scan on target: {target}......")
        self.scan_btn.setEnabled(False)

        worker = PortScannerEngine(target, ports)
        worker.signals.result.connect(self.update_ui)
        worker.signals.finished.connect(lambda: self.scan_btn.setEnabled(True))
        self.threadpool.start(worker)

    def update_ui(self, port, is_open):
        if is_open:
            self.console.append(f"[*] Port {port}: OPEN")