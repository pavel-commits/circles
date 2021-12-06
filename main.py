import sys
from random import randrange

from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setupUi(self)

        self.do_paint = False
        self.pushButton.clicked.connect(self.drawer)

    def drawer(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        for i in range(10):
            for j in range(10):
                qp.setBrush(QColor(randrange(255), randrange(255), randrange(255)))
                a = randrange(20, 100)
                qp.drawEllipse(10 + 100 * i, 10 + 100 * j,
                               a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())