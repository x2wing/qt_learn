import sys

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QTreeView, QApplication


class ProjectModel(QStandardItemModel):
    """Класс создания модели для отображения в QTreeView"""
    def __init__(self,  parent=None):
        # вызываем родительский конструктор
        super(ProjectModel, self).__init__(parent)

        #метод заполнения модели
        self.get_contents()

    def get_contents(self):
        # очищаем модель. Необходимо для открытия другого проекта
        self.clear()
        # D - более короткая запись self.metadata
        # D = self.metadata
        # # выбрасываем "version" из метаданных
        # D.pop("version", None)
        # # получаем корневой элемент дерева
        root = self.invisibleRootItem()
        # # перебираем ключи верхнего уровня в метадате
        # for i1, k1 in enumerate(D.keys()):
        #     # Если ключе не "version"
        #     if k1 != "version":
        #         # установим его элементом первого уровня
        #         root.setChild(i1, QStandardItem(k1))
        #         # создаем элементы второго уровня
        #         u2 = root.child(i1)
        #         # перебираем ключи второго уровня
        #         for i2, k2 in enumerate(D[k1].keys()):
        #             # если это DSET(содержит DSET в названии)
        #             if k2.find("DSET") != -1:
        #                 # добавляем этот ключ в элемент второго уровня
        #                 u2.setChild(i2, QStandardItem(k2))
        for i in range(10):
            root.setChild(i, QStandardItem(f'item{i}'))
            print(root.child(i).data().index().data())


class Tree(QTreeView):
    def __init__(self):
        QTreeView.__init__(self)
        model = ProjectModel()

        self.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Tree()
    w.show()
    sys.exit(app.exec_())
