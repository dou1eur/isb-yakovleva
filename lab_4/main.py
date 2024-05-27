import logging
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QMessageBox,
    QComboBox,)

from funсtions import collision_search, luna_algorithm, number_search

logging.basicConfig(filename="lab_4//report.log", filemode="a", level=logging.INFO)


class MainWindow(QWidget):

    def __init__(self):
        """
        Initializing the main window with options and input fields
        """
        super().__init__()
        self.setWindowTitle("Options")
        layout = QVBoxLayout()

        self.options = QComboBox()
        self.options.addItem("Search for card number")
        self.options.addItem("Check Luna algorithm")
        self.options.addItem("Collision Search")
        self.options.currentIndexChanged.connect(self.selection)
        layout.addWidget(self.options)

        self.button_hash = QLineEdit()
        layout.addWidget(self.button_hash)

        self.button_last_numbers = QLineEdit()
        layout.addWidget(self.button_last_numbers)

        self.button_path = QLineEdit()
        layout.addWidget(self.button_path)

        self.button_iin = QLineEdit()
        layout.addWidget(self.button_iin)

        self.button_options = QPushButton("Выполнить")
        self.button_options.clicked.connect(self.parameters)
        layout.addWidget(self.button_options)

        self.setLayout(layout)

    def selection(self, index):
        """
        Handles options in a separate menu

        Args:
            index (int): index of the selected option
        """
        option = self.options.currentText()
        match index:
            case 0:
                self.button_hash.setPlaceholderText("Enter hash")
                self.button_last_numbers.setPlaceholderText("Enter the last numbers of the card")
                self.button_path.setPlaceholderText("Enter the path where you want to save the number")
                self.button_iin.setPlaceholderText("Enter iin")
            case 1:
                self.button_last_numbers.setPlaceholderText("Enter the card number to check the Luna algorithm")
            case 2:
                self.button_hash.setPlaceholderText("Enter hash")
                self.button_last_numbers.setPlaceholderText("Enter the last numbers of the card")
                self.button_iin.setPlaceholderText("Enter iin")

    def parameters(self):
        """
        Execute the selected option based on user input
        """
        option = self.options.currentText()
        match option:
            case "Search for card number":
                self.card_number()
            case "Check Luna algorithm":
                self.algorithm()
            case "Collision Search":
                self.collision()

    def card_number(self) -> None:
        """
        Perform a search for a card number based on user input
        """
        try:
            iin_values = self.button_iin.text().split(",")
            if number_search(
                self.button_hash.text(),
                int(self.button_last_numbers.text()),
                self.button_path.text(),
                iin_values): 
                QMessageBox.information(self, "Card number found", "Card number found")
                logging.info("card number found")
            else:
                QMessageBox.information(self, "Card number not found", "Card number not found")
        except Exception as e:
            logging.error(f"Error in number_search {e}")

    def algorithm(self) -> None:
        """
        Check the Luna algorithm based on user input
        """
        try:
            if not luna_algorithm(self.button_last_numbers.text()):
                QMessageBox.information(
                    self, "Luna algorithm not passed", "Luna algorithm not passed")
            else:
                QMessageBox.information(self, "Luna algorithm passed", "Luna algorithm passed")
            logging.info("Luna algorithm work")
        except Exception as e:
            logging.error(f"Error luna algorithm {e}")

    def collision(self) -> None:
        """
        Perform a hash collision search
        """
        try:
            iin_values = self.button_iin.text().split(",")
            if collision_search(
                self.button_hash.text(),
                int(self.button_last_numbers.text()),
                iin_values):
                QMessageBox.information(self, "Statistics collected", "Statistics collected")
                logging.info("Statistics collected")
            else:
                QMessageBox.information(self, "Statistics not collected", "Statistics not collected")
        except Exception as e:
            logging.error(f"Error during collision search {e}")


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exec_()
    except Exception as e:
        logging.error(f"Problems in main {e}")
