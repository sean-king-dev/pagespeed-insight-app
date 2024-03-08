from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
import requests
import json
import logging

class PageSpeedGUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PageSpeed Insights")
        self.setGeometry(100, 100, 400, 200)

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.url_label = QLabel("Enter URL:")
        self.url_input = QLineEdit()
        self.submit_button = QPushButton("Submit")
        self.results_label = QLabel("Results will be displayed here.")

        self.submit_button.clicked.connect(self.send_request)

        self.layout.addWidget(self.url_label)
        self.layout.addWidget(self.url_input)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.results_label)

        self.central_widget.setLayout(self.layout)

    def send_request(self):
        url = self.url_input.text()
        logging.debug(f"Request URL: {url}")

        try:
            response = requests.get(f'http://localhost:5000/api/pagespeed?url={url}')
            response.raise_for_status()

            data = response.json()

            # Process the data and update the GUI as needed
            # For simplicity, just displaying the raw data here
            self.results_label.setText(json.dumps(data, indent=2))
        except requests.exceptions.RequestException as e:
            self.results_label.setText(f"Error: {str(e)}")


if __name__ == '__main__':
    app = QApplication([])
    main_win = PageSpeedGUI()
    main_win.show()
    app.exec_()
