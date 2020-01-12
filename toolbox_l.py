import sys

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QToolBox, QLabel, QApplication, QPushButton, QVBoxLayout, QWidget


class СQPushButton(QPushButton):
    def __init__(self, obj, icon=None, text=None, parent=None):
        super().__init__(icon, text, parent)
        self.obj = obj
        self.clicked.connect(self.run)
        self.setFlat(True)
        # self.setStyleSheet("color: blue; text-decoration: underline; text-align: left;")

    def run(self):
        print('кнопка')


class VContainer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.addWidgets(widgets)
        self.vcontainer = QVBoxLayout(self)
        self.vcontainer.setGeometry(QRect(0, 0, 10, 10))

    def addWidgets(self, widgets):
        for widget in widgets:
            self.vcontainer.addWidget(widget)
        self.vcontainer.addStretch(1)
        self.vcontainer.setSpacing(1)


class CToolBox(QToolBox):
    def __init__(self):
        super().__init__(parent=None)
        self.initUI()

    def initUI(self):
        self.addItem(QLabel('Содержимое вкладки №1'), QIcon('ico/git.png'), 'Git')
        self.addItem(QLabel('Содержимое вкладки №2'), QIcon('ico/folder.png'), 'Папки')
        self.addItem(QLabel('Содержимое вкладки №3'), QIcon('ico/github.png'), 'GitHub')
        self.addItem(QLabel('Содержимое вкладки №4'), QIcon('ico/organaizer.png'), 'Органайзер')
        container_db = VContainer(self)
        widgets = (
            СQPushButton(obj=self, icon=QIcon('ico/barrel.png'), text='size_test1', parent=container_db),
            СQPushButton(obj=self, icon=QIcon('ico/barrel.png'), text='size_test2', parent=container_db),
            СQPushButton(obj=self, icon=QIcon('ico/barrel.png'), text='size_test3', parent=container_db),
            СQPushButton(obj=self, icon=QIcon('ico/barrel.png'), text='size_test4', parent=container_db),)
        container_db.addWidgets(widgets)


        self.addItem(container_db, QIcon('ico/db.png'), 'Базы')
        # self.setItemEnabled(1, False)
        self.setCurrentIndex(4)
        self.setStyleSheet("""QPushButton { color: blue;
        
        text-align: left;
        }
        QPushButton:hover {
        text-decoration: underline;
        }""")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CToolBox()
    window.resize(500, 500)
    window.show()
    sys.exit(app.exec_())
