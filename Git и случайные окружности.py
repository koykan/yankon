import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt6.QtGui import QPainter, QColor


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Circle Drawer")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.button = QPushButton("Draw Circle", self.central_widget)
        self.button.setGeometry(150, 120, 100, 30)
        self.button.clicked.connect(self.draw_circle)

        self.should_draw_circle = False

    def draw_circle(self):
        self.should_draw_circle = True
        self.update()

    def paintEvent(self, event):
        if self.should_draw_circle:
            painter = QPainter(self)
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            painter.setPen(color)
            painter.setBrush(color)
            diameter = random.randint(10, 100)
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            painter.drawEllipse(x, y, diameter, diameter)
            self.should_draw_circle = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())

