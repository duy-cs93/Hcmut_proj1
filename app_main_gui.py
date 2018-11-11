import sys
from PyQt5 import QtWidgets, QtCore, QtGui


# class MainForm(QtWidgets.QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Amazon Simulation")
#         self.setGeometry(30, 40, 640, 480)
#         line_1 = QtWidgets.QLineEdit(self)
#         line_1.resize(500, 25)
#         line_1.move(50, 20)
#
#         btn_1 = QtWidgets.QPushButton(self)
#         btn_1.setText("Search")
#         btn_1.resize(50, 25)
#         btn_1.move(550, 20)
#         self.show()


class LoginForm(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Log in"
        self.left = 380
        self.top = 220
        self.width = 540
        self.height = 380
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # CREATE LABEL
        l1 = QtWidgets.QLabel(self)
        l2 = QtWidgets.QLabel(self)

        l1.setText("Tên đăng nhập: ")
        l1.move(30, 50)

        # CREATE ID TEXT BOX
        user_text = QtWidgets.QLineEdit(self)
        user_text.move(30, 80)
        user_text.resize(220, 25)

        l2.setText("Mật khẩu: ")
        l2.move(30, 120)

        # CREATE PASSWORD TEXT BOX
        password_text = QtWidgets.QLineEdit(self)
        password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        password_text.move(30, 150)
        password_text.resize(220, 25)

        # CREATE BUTTON IN THE WINDOW
        button = QtWidgets.QPushButton("Quản lý", self)
        button.move(200, 300)

        # CONNECT BUTTON TO FUNCTION ON_CLICK
        button.clicked.connect(self.on_click)

    @QtCore.pyqtSlot()
    def on_click(self):
        print("hello")

    def authenticate(self):
        print("Tiến hành confirm user và password")


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.so_luong_hang_hoa = 0  # this variable is used for counting the number of purchased item
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
        quan_ly = menu_bar.addMenu("Quản lý cửa hàng")
        hang_hoa = menu_bar.addMenu("Hàng hóa")
        giao_dich = menu_bar.addMenu("Giao dịch")
        doi_tac = menu_bar.addMenu("Đối tác")
        so_quy = menu_bar.addMenu("Sổ quỹ")
        bao_cao = menu_bar.addMenu("Báo cáo")

        # CREATE ACTION FOR MENUS
        luu_action = QtWidgets.QAction("Lưu tùy chỉnh", self)
        luu_action.setShortcut("Ctrl + S")

        dong_tien_action = QtWidgets.QAction("Dòng tiền", self)

        # ADD ACTION TO MENUS
        quan_ly.addAction(luu_action)
        so_quy.addAction(dong_tien_action)

        # ADD SEARCH BOX
        o_tim_kiem = QtWidgets.QLineEdit(self)
        o_tim_kiem.move(450, 30)
        o_tim_kiem.resize(280, 25)

        # ADD BUTTON
        tim_kiem_btn = QtWidgets.QPushButton(self)
        tim_kiem_btn.setIcon(QtGui.QIcon("magnifying glass.png"))
        tim_kiem_btn.move(730, 30)
        tim_kiem_btn.resize(25, 25)

        them_sp_btn = QtWidgets.QPushButton("Thêm vào", self)
        them_sp_btn.move(600, 100)
        them_sp_btn.resize(70, 30)

        # ADD COMBO BOX
        # list_hang_hoa = QtWidgets.QComboBox(self)
        # list_hang_hoa.move(30, 60)
        # list_hang_hoa.addItem("Táo")
        # list_hang_hoa.addItem("Cam")
        # list_hang_hoa.addItem("Mận")
        # list_hang_hoa.addItem("Dừa")
        # list_hang_hoa.addItem("Ổi")

        # ADD TABLE
        ban_tinh_tien = QtWidgets.QTableWidget(self)
        ban_tinh_tien.setRowCount(4)
        ban_tinh_tien.setColumnCount(3)
        # ban_tinh_tien.setHorizontalHeaderLabels(["Code", ""])
        ban_tinh_tien.move(100, 100)
        ban_tinh_tien.resize(400, 400)

        # TRIGGERED EVENTS
        luu_action.triggered.connect(self.save_trigger)
        dong_tien_action.triggered.connect(self.money_transaction_trigger)
        # list_hang_hoa.currentTextChanged.connect(self.combo_box_trigger)
        them_sp_btn.clicked.connect(lambda: self.insert_item_to_table(ban_tinh_tien))



    # DEFINE TRIGGERED EVENTS
    def save_trigger(self):
        print("luu thu gi do o day")

    def search_trigger(self):
        print("search thu gi do o day")

    def money_transaction_trigger(self):
        mt_trigger_pop_up = QtWidgets.QMainWindow(self)
        mt_trigger_pop_up.setWindowTitle("Dòng tiền")
        mt_trigger_pop_up.show()

    def combo_box_trigger(self, value):
        print("combobox changed ", value)

    def insert_item_to_table(self, table, item_code="102020", item_name="Random", price="11000"):
        table.setItem(self.so_luong_hang_hoa, 0, QtWidgets.QTableWidgetItem(item_code))
        table.setItem(self.so_luong_hang_hoa, 1, QtWidgets.QTableWidgetItem(item_name))
        table.setItem(self.so_luong_hang_hoa, 2, QtWidgets.QTableWidgetItem(price))
        self.so_luong_hang_hoa += 1


class Invoice:
    def __init__(self):
        print("TBD by Thach")


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())


