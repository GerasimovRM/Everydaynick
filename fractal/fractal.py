

import sys
from math import cos, pi, sin

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog

SCREEN_SIZE = [500, 500]
# Задаём длину стороны и количество углов



class Fractal:
    def __init__(self, filename):
        with open(filename, "r") as f:
            self.side = int(f.readline())
            self.angle = int(f.readline())
            self.init = f.readline()
            self.exp = f.readline()


class DrawStar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, *SCREEN_SIZE)
        self.setWindowTitle('Рисуем звезду')

        self.btn = QPushButton("Рисуй", self)
        self.btn.clicked.connect(self.run)

        self.do_paint = False

    def run(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_fractal()
            qp.end()

    def xs(self, x):
        return x + SCREEN_SIZE[0] // 2

    def ys(self, y):
        return SCREEN_SIZE[1] // 2 - y

    def draw_fractal(self, qp):
        pass



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
sys.excepthook = except_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawStar()
    ex.show()
    sys.exit(app.exec())