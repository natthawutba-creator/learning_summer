import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)

label = QLabel("<font color=red size=40>Hello World</font>")
label.resize(640, 480)
label.setWindowTitle("My Programe")
label.show()

sys.exit(app.exec())