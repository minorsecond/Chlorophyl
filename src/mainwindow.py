from gui import ui_mainwindow
from src import point_cloud
from PyQt5 import QtWidgets
import os


class MainWindow(QtWidgets.QMainWindow, ui_mainwindow.Ui_MainWindow):
    """
    Main UI Class
    """

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        ui_mainwindow.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Connections
        self.processButton.clicked.connect(self.process_button)
        self.inputDirectoryBrowseButton.clicked.connect(self.browse_button_clicked)

    def browse_button_clicked(self):
        """
        Open the directory browse window.
        """

        input_path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.inputDirectoryLineEdit.setText(input_path)

    def process_button(self):
        """
        Kicks off the processing when the process button is clicked.
        """
        input_path = self.inputDirectoryLineEdit.text()
        input_files = get_input_files(input_path)

        print(f"Found {len(input_files)} files")

        for file in input_files:
            pc = point_cloud.PointCloud(file)
            print(f"Total number of points in {file}: {pc.point_number}")
            gs = pc.get_vegetation()
            print(f"GS object: {gs}")


def get_input_files(input_path):
    """
    Gets the input files found within path.
    :return: List of files to process.
    """

    file_list = []

    for root, directory_names, filenames in os.walk(input_path):
        for file in filenames:
            if os.path.splitext(file)[1].lower() in ['.laz', '.las']:
                file_list.append(os.path.join(root, file))

    return file_list
