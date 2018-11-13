import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import cash_book


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.amount_of_products = 0  # this variable is used for counting the number of purchased item
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Main Window")
        # self.resize(800, 600)
        self.setFixedSize(800, 600)
        self.statusBar().showMessage("Hello Customers! Our best wishes to you!")
        # selected_color = QtGui.QColor(0, 255, 255)
        # self.setStyleSheet("QWidget {background-color: %s}" % selected_color.name())

        # CREATE MENU BAR
        menu_bar = self.menuBar()

        # CREATE ROOT MENUS
        manage = menu_bar.addMenu("Quản lý cửa hàng")
        product = menu_bar.addMenu("Hàng hóa")
        transaction = menu_bar.addMenu("Giao dịch")
        business_partners = menu_bar.addMenu("Đối tác")
        cash_book = menu_bar.addMenu("Sổ quỹ")
        report = menu_bar.addMenu("Báo cáo")

        # CREATE ACTION FOR MENUS
        save_action = QtWidgets.QAction("Lưu tùy chỉnh", self)
        save_action.setShortcut("Ctrl + S")

        cash_flow_action = QtWidgets.QAction("Dòng tiền", self)

        # ADD ACTION TO MENUS
        manage.addAction(save_action)
        cash_book.addAction(cash_flow_action)

        # ADD SEARCH BOX
        search_box = QtWidgets.QLineEdit(self)
        search_box.move(450, 30)
        search_box.resize(280, 25)

        # ADD BUTTON
        search_btn = QtWidgets.QPushButton(self)
        search_btn.setIcon(QtGui.QIcon("magnifying glass.png"))
        search_btn.move(730, 30)
        search_btn.resize(25, 25)

        add_product_btn = QtWidgets.QPushButton("Thêm vào", self)
        add_product_btn.move(600, 100)
        add_product_btn.resize(70, 30)

        # ADD TABLE
        self.purchased_list = QtWidgets.QTableWidget(self)
        self.purchased_list.setRowCount(0)
        self.purchased_list.setColumnCount(4)
        self.purchased_list.setHorizontalHeaderLabels(["Code", "Name", "Price", ""])
        self.purchased_list.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)   # disable editing feature
        self.purchased_list.move(100, 100)
        self.purchased_list.resize(450, 400)

        # TRIGGERED EVENTS
        save_action.triggered.connect(self.save_trigger)
        cash_flow_action.triggered.connect(self.money_transaction_trigger)
        add_product_btn.clicked.connect(lambda: self.insert_item_to_table(self.purchased_list))
        # need to fix this
        self.purchased_list.cellClicked.connect(self.delete_item_from_table)

    # DEFINE TRIGGERED EVENTS
    def save_trigger(self):
        print("luu thu gi do o day")

    def search_trigger(self):
        print("search thu gi do o day")

    def money_transaction_trigger(self):
        self.mt_trigger_pop_up = cash_book.SoQuyForm()
        self.mt_trigger_pop_up.show()

    def insert_item_to_table(self, table, item_code="102020", item_name="Random", price="11000"):
        # table.setRowCount(self.amount_of_products)
        # self.amount_of_products += 1
        # table.setItem(self.amount_of_products-1, 0, QtWidgets.QTableWidgetItem(item_code))
        # table.setItem(self.amount_of_products-1, 1, QtWidgets.QTableWidgetItem(item_name))
        # table.setItem(self.amount_of_products-1, 2, QtWidgets.QTableWidgetItem(price))
        # table.setItem(self.amount_of_products-1, 3, QtWidgets.QTableWidgetItem("X"))

        # fixed code
        row_position = table.rowCount()
        table.insertRow(row_position)
        table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(item_code))
        table.setItem(row_position, 1, QtWidgets.QTableWidgetItem(item_name))
        table.setItem(row_position, 2, QtWidgets.QTableWidgetItem(price))
        table.setItem(row_position, 3, QtWidgets.QTableWidgetItem("X"))

    def delete_item_from_table(self, row, column):
        if self.purchased_list.item(row, column).text() == 'X':
            print("delete row number %s" % row)
            self.purchased_list.removeRow(row)


# MAIN CODE HERE
app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())

print('Hello World !')


