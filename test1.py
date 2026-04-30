import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

label = QLabel("Hello World")
label.resize(640, 480)
label.show()

sys.exit(app.exec())