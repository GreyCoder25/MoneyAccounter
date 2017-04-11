# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Tue Apr 11 17:27:10 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 467)
        icon = QtGui.QIcon.fromTheme("terminator")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 617, 501))
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 20, 600, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.table.setMouseTracking(False)
        self.table.setColumnCount(3)
        self.table.setObjectName("table")
        self.table.setRowCount(0)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setDefaultSectionSize(100)
        self.table.horizontalHeader().setMinimumSectionSize(100)
        self.table.verticalHeader().setVisible(True)
        self.amountLine = QtWidgets.QLineEdit(self.centralwidget)
        self.amountLine.setGeometry(QtCore.QRect(10, 260, 91, 27))
        self.amountLine.setObjectName("amountLine")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(500, 260, 111, 27))
        self.dateEdit.setObjectName("dateEdit")
        self.commentLine = QtWidgets.QLineEdit(self.centralwidget)
        self.commentLine.setGeometry(QtCore.QRect(110, 260, 381, 27))
        self.commentLine.setObjectName("commentLine")
        self.push_button = QtWidgets.QPushButton(self.centralwidget)
        self.push_button.setGeometry(QtCore.QRect(10, 300, 91, 26))
        self.push_button.setObjectName("push_button")
        self.pop_button = QtWidgets.QPushButton(self.centralwidget)
        self.pop_button.setGeometry(QtCore.QRect(110, 300, 91, 26))
        self.pop_button.setObjectName("pop_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 230, 101, 17))
        self.label.setObjectName("label")
        self.use_this_date_cb = QtWidgets.QCheckBox(self.centralwidget)
        self.use_this_date_cb.setGeometry(QtCore.QRect(490, 230, 151, 22))
        self.use_this_date_cb.setObjectName("use_this_date_cb")
        self.filter_button = QtWidgets.QPushButton(self.centralwidget)
        self.filter_button.setGeometry(QtCore.QRect(10, 360, 91, 26))
        self.filter_button.setObjectName("filter_button")
        self.from_date = QtWidgets.QDateEdit(self.centralwidget)
        self.from_date.setGeometry(QtCore.QRect(230, 360, 91, 27))
        self.from_date.setObjectName("from_date")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 340, 66, 17))
        self.label_2.setObjectName("label_2")
        self.to_date = QtWidgets.QDateEdit(self.centralwidget)
        self.to_date.setGeometry(QtCore.QRect(330, 360, 91, 27))
        self.to_date.setObjectName("to_date")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 340, 66, 17))
        self.label_3.setObjectName("label_3")
        self.by_date_cb = QtWidgets.QCheckBox(self.centralwidget)
        self.by_date_cb.setGeometry(QtCore.QRect(110, 360, 97, 22))
        self.by_date_cb.setObjectName("by_date_cb")
        self.sort_by_value_cb = QtWidgets.QCheckBox(self.centralwidget)
        self.sort_by_value_cb.setGeometry(QtCore.QRect(110, 390, 121, 22))
        self.sort_by_value_cb.setObjectName("sort_by_value_cb")
        self.by_comment_cb = QtWidgets.QCheckBox(self.centralwidget)
        self.by_comment_cb.setGeometry(QtCore.QRect(110, 420, 121, 22))
        self.by_comment_cb.setObjectName("by_comment_cb")
        self.by_comment_le = QtWidgets.QLineEdit(self.centralwidget)
        self.by_comment_le.setGeometry(QtCore.QRect(230, 420, 191, 27))
        self.by_comment_le.setObjectName("by_comment_le")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Accounter"))
        self.push_button.setText(_translate("MainWindow", "push"))
        self.pop_button.setText(_translate("MainWindow", "pop"))
        self.label.setText(_translate("MainWindow", "NEW RECORD"))
        self.use_this_date_cb.setText(_translate("MainWindow", "use this date?"))
        self.filter_button.setText(_translate("MainWindow", "filter"))
        self.label_2.setText(_translate("MainWindow", "FROM"))
        self.label_3.setText(_translate("MainWindow", "TO"))
        self.by_date_cb.setText(_translate("MainWindow", "by date"))
        self.sort_by_value_cb.setText(_translate("MainWindow", "sort by value"))
        self.by_comment_cb.setText(_translate("MainWindow", "by comment"))

