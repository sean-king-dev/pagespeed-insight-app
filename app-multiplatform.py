from flask import Flask, render_template, request, jsonify, Response
import requests
import json
from config import Config
from flask_cors import CORS
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
import sys

app = Flask(__name__)
CORS(app)
config = Config()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PageSpeed Analyzer")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.url_label = QLabel("Enter URL:")
        self.url_input = QLineEdit()
        self.fetch_button = QPushButton("Fetch PageSpeed Data")
        self.fetch_button.clicked.connect(self.fetch_data)

        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.fetch_button)

        self.central_widget.setLayout(layout)

    def fetch_data(self):
        url = self.url_input.text()

        if not url:
            self.show_message("Error", "Please provide a URL.")
            return

        api_key = config.API_KEY
        base_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'

        params = {
            'url': url,
            'key': api_key,
        }

        try:
            response = requests.get(base_url, params=params)
            data = json.loads(response.text)

            # Display or process the data as needed
            print("PageSpeed Data:", data)
        except Exception as e:
            self.show_message("Error", f"Failed to fetch PageSpeed data.\nError: {e}")

    def show_message(self, title, message):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

def run_flask_app():
    app.run(debug=True, host='127.0.0.1', port=5000)

if __name__ == '__main__':
    # Start the Flask app with the development server in a separate thread
    flask_app_thread = threading.Thread(target=run_flask_app)
    flask_app_thread.start()

    # Create and show the PyQt5 GUI
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
