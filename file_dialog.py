import sys
from math import cos, pi, sin

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog

SCREEN_SIZE = [500, 500]
# Задаём длину стороны и количество углов
SIDE_LENGTH = 200


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
        self.N, ok_pressed = QInputDialog.getInt(self, "Звздочетное окно", "Введите n:", 5, 5, 100, 1)
        if ok_pressed:
            self.do_paint = True
            self.update()



    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_star(qp)
            qp.end()

    def xs(self, x):
        return x + SCREEN_SIZE[0] // 2

    def ys(self, y):
        return SCREEN_SIZE[1] // 2 - y

    def draw_star(self, qp):

        # Считаем координаты и переводим их в экранные
        nodes = [(SIDE_LENGTH * cos(i * 2 * pi / self.N),
                  SIDE_LENGTH * sin(i * 2 * pi / self.N))
                 for i in range(self.N)]
        nodes2 = [(int(self.xs(node[0])),
                   int(self.ys(node[1]))) for node in nodes]

        # Рисуем пятиугольник
        for i in range(-1, len(nodes2) - 1):
            qp.drawLine(*nodes2[i], *nodes2[i + 1])

        # Изменяем цвет линии
        pen = QPen(Qt.red, 2)
        qp.setPen(pen)

        # Рисуем звезду
        if self.N % 2 == 0:
            for i in range(-1, self.N - 2, 2):
                qp.drawLine(*nodes2[i], *nodes2[i + 2])
            for i in range(-2, self.N - 2, 2):
                qp.drawLine(*nodes2[i], *nodes2[i + 2])
        else:
            for i in range(-2, len(nodes2) - 2):
                qp.drawLine(*nodes2[i], *nodes2[i + 2])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
sys.excepthook = except_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawStar()
    ex.show()
    sys.exit(app.exec())