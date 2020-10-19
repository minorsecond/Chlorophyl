from src import mainwindow
import sys

if __name__ == '__main__':
    app = mainwindow.QtWidgets.QApplication(sys.argv)
    window = mainwindow.MainWIndow()
    window.show()
    sys.exit(app.exec_())
