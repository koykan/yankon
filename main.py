import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw_circle)
        self.should_draw_circle = False

    def draw_circle(self):
        self.should_draw_circle = True
        self.update()

    def paintEvent(self, event):
        if self.should_draw_circle:
            painter = QPainter(self)
            painter.setPen(QColor(255, 255, 0))
            painter.setBrush(QColor(255, 255, 0))
            diameter = random.randint(10, 100)
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            painter.drawEllipse(x, y, diameter, diameter)
            self.should_draw_circle = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
