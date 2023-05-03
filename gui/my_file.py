import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import QSize, Qt

class myWidget(QWidget):

    def __init__(self, path, parent=None):
        super().__init__(parent)

        pixmap = QPixmap(path)

        label = QLabel(self)
        label.setPixmap(pixmap)

        layout = QVBoxLayout(self)
        layout.addWidget(label)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mental app")

        self.setFixedSize(QSize(400, 400))


        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        btn = QPushButton("Привет!")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)

        self.stacklayout.addWidget(QLabel(
            "Ваше ментальное здоровье очень важно.\nНа следующей страничке вы можете выговориться и написать все,\nчто есть на душе. Порой это помогает собрать мысли и разобраться\nс трудностями! А еще эффективны объятья!"))


        btn = QPushButton("Дневник")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(QLineEdit())

        btn = QPushButton("Объятья")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(myWidget("animation.gif"))

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)

    def activate_tab_4(self):
        self.stacklayout.setCurrentIndex(3)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
