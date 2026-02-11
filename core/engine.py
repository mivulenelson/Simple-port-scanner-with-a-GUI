import socket
from PySide6.QtCore import QObject, Signal, QRunnable, Slot


# Signals to communicate with the GUI
class ScanSignals(QObject):
    result = Signal(int, bool)
    finished = Signal()

# Class for Port Scanning
class PortScannerEngine(QRunnable):
    def __init__(self, target_ip, ports):
        super().__init__()
        self.target_ip = target_ip
        self.ports = ports
        self.signals = ScanSignals()

    @Slot()
    def run(self): # Function to scan the network
        for port in self.ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.8)

                    # connect_ex is better for scanners as it returns an error code instead of an exception
                    result = s.connect_ex((self.target_ip, port))
                    if result == 0:
                        self.signals.result.emit(port, True)
                    else:
                        pass
            except Exception as e:
                print(f"Connection error om port {port}: {e}")
                
        self.signals.finished.emit()
        
