import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from accounter import Accounter
from ui_window import Ui_MainWindow
from view import *


class UIController:
        """Starts application"""
        def app_init(self):
            self.app = QApplication(sys.argv)
            self.window = QDialog()
            QShortcut(QKeySequence("Ctrl+Q"), self.window, self.window.close)

        def ui_setup(self):
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.ui.dateEdit.setDate(QDate.currentDate())
            self.ui.from_date.setDate(QDate.currentDate())
            self.ui.to_date.setDate(QDate.currentDate())

        def load_data(self):
            self.acc = Accounter()
            self.acc.load_data()
            self.acc.sort_by_date()
            ui_helper = Helper()
            ui_helper.load_to_table(self.ui, self.acc)

        def interface_setup(self):
            self.interface = Interface()
            self.ui.push_button.clicked.connect(self.interface.make_push_button_clicked(self.acc, self.ui))
            self.ui.pop_button.clicked.connect(self.interface.make_pop_button_clicked(self.acc, self.ui))
            self.ui.filter_button.clicked.connect(self.interface.make_filter_button_clicked(self.acc, self.ui))

        def app_run(self):
            self.window.show()
            self.app.exec_()
            self.acc.save_data()
            sys.exit()


if __name__ == "__main__":
    controller = UIController()
    controller.app_init()
    controller.ui_setup()
    controller.load_data()
    controller.interface_setup()
    controller.app_run()