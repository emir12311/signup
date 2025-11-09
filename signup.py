from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QInputDialog, QLineEdit
from signupwindow import SignUp
from mainwindow import Main
from adminwindow import Admin
import sys,sqlite3
from hashlib import sha256
class SignupWindow(QWidget, SignUp):
    def __init__(self):
        super().__init__()
        self.u = SignUp()
        self.u.setupUi(self)
        self.setupui()

    def setupui(self):
        for g in range(1,32):
            if g < 10:
                self.u.comboBox_3.addItem("0" + str(g))
            else:
                self.u.comboBox_3.addItem(str(g))
        for y in range(2025, 1699, -1):
            self.u.comboBox_2.addItem(str(y))
        self.u.comboBox_2.setCurrentIndex(-1)
        self.u.comboBox_3.setCurrentIndex(-1)
        self.mbox = QMessageBox()
        self.u.pushButton.clicked.connect(self.createaccount)

    def createaccount(self):
        self.alllineedit = [self.u.lineEdit.text(),self.u.lineEdit_2.text(),self.u.lineEdit_3.text(),self.u.lineEdit_4.text()]
        self.allradio = [self.u.radioButton.isChecked(),self.u.radioButton_2.isChecked(),self.u.radioButton_3.isChecked()]
        self.allcombobox = [self.u.comboBox.currentText(),self.u.comboBox_2.currentText(),self.u.comboBox_3.currentText()]
        if any(l == "" for l in self.alllineedit) or all(r == False for r in self.allradio) or any(c == "" for c in self.allcombobox):
            self.mbox.setText("Formu Komple Doldurunuz.")
            self.mbox.setWindowTitle("Hata")
            self.mbox.exec_()
        else:
            self.isim = self.u.lineEdit.text()
            self.soyisim = self.u.lineEdit_2.text()
            self.eposta = self.u.lineEdit_3.text()
            self.telno = self.u.lineEdit_4.text()
            self.dogumtarih = f"{self.u.comboBox.currentText()}/{self.u.comboBox_3.currentText()}/{self.u.comboBox_2.currentText()}"
            if self.u.radioButton.isChecked():
                self.cinsiyet = "Erkek"
            elif self.u.radioButton_2.isChecked():
                self.cinsiyet = "Kadın"
            else:
                self.cinsiyet = "Belirtilmemiş"
            self.insert_to_db(self.isim,self.soyisim,self.eposta,self.telno,self.dogumtarih,self.cinsiyet)
            self.mbox.setText(f"Sayın {self.isim} {self.soyisim} hesabınız başarıyla kurulmuştur.")
            self.mbox.setWindowTitle("Başarılı!")
            self.mbox.exec_()

    def insert_to_db(self, var1, var2, var3, var4, var5, var6):
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS kullanici_kayit (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            s1 TEXT,
            s2 TEXT,
            s3 TEXT,
            s4 TEXT,
            s5 TEXT,
            s6 TEXT
        )
        """)
        cursor.execute("""
        INSERT INTO kullanici_kayit (s1, s2, s3, s4, s5, s6)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (var1, var2, var3, var4, var5, var6))
        conn.commit()
        conn.close()

class AdminWindow(QWidget, Admin):
    def __init__(self):
        super().__init__()
        self.u = Admin()
        self.u.setupUi(self)
        self.setupui()

    def setupui(self):
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM kullanici_kayit")
        users = cursor.fetchall()

        for user in users:
            display_text = f"{user[0]}. {user[1]} {user[2]}, {user[3]}, {user[4]}, {user[5]}, {user[6]}"
            self.u.listWidget.addItem(display_text)

        conn.close()
        
        
class MainWindow(QWidget, Main):
    def __init__(self):
        super().__init__()
        self.u = Main()
        self.u.setupUi(self)
        self.setupui()
        
    def setupui(self):
        self.u.pushButton.pressed.connect(self.signup)
        self.u.pushButton_2.pressed.connect(self.adminlogin)
        
    def signup(self):
        self.signwindow = SignupWindow()
        self.signwindow.show()
        
    def adminlogin(self):
        password, confirmed = QInputDialog.getText(
            self, "Admin Girişi", "Admin şifresini giriniz:", 2
        )

        if not confirmed:
            return

        correct_password = "e9cee71ab932fde863338d08be4de9dfe39ea049bdafb342ce659ec5450b69ae"

        if sha256(password.encode()).hexdigest() == correct_password:
            self.adminwindow = AdminWindow()
            self.adminwindow.show()
        else:
            mbox = QMessageBox(self)
            mbox.setText("Hatalı şifre.")
            mbox.setWindowTitle("Erişim Engellendi")
            mbox.exec_()
        
        

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
