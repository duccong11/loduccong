import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from nhansu import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # DATABASE
        self.conn = sqlite3.connect("nhansu.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS nhansu (
            cccd TEXT PRIMARY KEY,
            hoten TEXT,
            ngaysinh TEXT,
            gioitinh TEXT,
            diachi TEXT
        )
        """)
        self.conn.commit()

        # EVENT
        self.ui.btn_them.clicked.connect(self.them)
        self.ui.btn_sua.clicked.connect(self.sua)
        self.ui.btn_xoa.clicked.connect(self.xoa)
        self.ui.btn_tim.clicked.connect(self.tim)
        self.ui.tableWidget.clicked.connect(self.chon_dong)

        self.load_data()

    # LOAD DATA
    def load_data(self):
        self.ui.tableWidget.setRowCount(0)

        self.cursor.execute("SELECT * FROM nhansu")
        for row_idx, row_data in enumerate(self.cursor.fetchall()):
            self.ui.tableWidget.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    # THÊM
    def them(self):
        try:
            self.cursor.execute("INSERT INTO nhansu VALUES (?, ?, ?, ?, ?)", (
                self.ui.txt_cccd.text(),
                self.ui.txt_hoten.text(),
                self.ui.txt_ngaysinh.text(),
                self.ui.txt_gioitinh.currentText(),
                self.ui.txt_diachi.text()
            ))
            self.conn.commit()
            self.load_data()
            QMessageBox.information(self, "OK", "Thêm thành công")
        except:
            QMessageBox.warning(self, "Lỗi", "CCCD đã tồn tại")

    # SỬA
    def sua(self):
        self.cursor.execute("""
        UPDATE nhansu SET hoten=?, ngaysinh=?, gioitinh=?, diachi=?
        WHERE cccd=?
        """, (
            self.ui.txt_hoten.text(),
            self.ui.txt_ngaysinh.text(),
            self.ui.txt_gioitinh.currentText(),
            self.ui.txt_diachi.text(),
            self.ui.txt_cccd.text()
        ))
        self.conn.commit()
        self.load_data()

    # XÓA
    def xoa(self):
        self.cursor.execute("DELETE FROM nhansu WHERE cccd=?",
                            (self.ui.txt_cccd.text(),))
        self.conn.commit()
        self.load_data()

    # TÌM
    def tim(self):
        keyword = self.ui.txt_search.text()

        self.ui.tableWidget.setRowCount(0)

        self.cursor.execute("""
        SELECT * FROM nhansu
        WHERE cccd LIKE ? OR hoten LIKE ? OR diachi LIKE ?
        """, ('%'+keyword+'%', '%'+keyword+'%', '%'+keyword+'%'))

        for row_idx, row_data in enumerate(self.cursor.fetchall()):
            self.ui.tableWidget.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    # CLICK TABLE
    def chon_dong(self):
        row = self.ui.tableWidget.currentRow()

        self.ui.txt_cccd.setText(self.ui.tableWidget.item(row, 0).text())
        self.ui.txt_hoten.setText(self.ui.tableWidget.item(row, 1).text())
        self.ui.txt_ngaysinh.setText(self.ui.tableWidget.item(row, 2).text())
        self.ui.txt_gioitinh.setCurrentText(self.ui.tableWidget.item(row, 3).text())
        self.ui.txt_diachi.setText(self.ui.tableWidget.item(row, 4).text())


# RUN
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())