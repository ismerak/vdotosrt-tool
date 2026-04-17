import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QCheckBox, 
                             QComboBox, QTextEdit, QFrame)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class VideoDownloaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # កំណត់ទំហំ និងចំណងជើង
        self.setWindowTitle('Video Downloader Pro v25.02.26')
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet("background-color: #800080; color: white;") # ពណ៌ស្វាយដិត

        # Main Layout (Horizontal)
        main_layout = QHBoxLayout()

        # --- ផ្នែកខាងឆ្វេង (Settings) ---
        left_panel = QVBoxLayout()
        
        title_label = QLabel("Functions")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("background-color: #a020f0; padding: 5px; font-weight: bold;")
        left_panel.addWidget(title_label)

        # ឧទាហរណ៍៖ ការបន្ថែម Checkbox និង Input
        func_layout = QVBoxLayout()
        cb1 = QCheckBox("Title + ID")
        cb2 = QCheckBox("Uploader")
        func_layout.addWidget(cb1)
        func_layout.addWidget(cb2)
        
        # កន្លែងដាក់ Link
        self.link_input = QTextEdit()
        self.link_input.setPlaceholderText("បញ្ចូល Link នៅទីនេះ...")
        self.link_input.setStyleSheet("background-color: white; color: black;")
        left_panel.addLayout(func_layout)
        left_panel.addWidget(QLabel("Link ( 0 )"))
        left_panel.addWidget(self.link_input)

        # ប៊ូតុង Start/Stop
        btn_layout = QHBoxLayout()
        start_btn = QPushButton("Start ▶")
        start_btn.setStyleSheet("background-color: #00ff00; color: black; font-weight: bold; height: 40px;")
        stop_btn = QPushButton("Stop ⏹")
        stop_btn.setStyleSheet("background-color: #cccccc; color: black; height: 40px;")
        btn_layout.addWidget(start_btn)
        btn_layout.addWidget(stop_btn)
        left_panel.addLayout(btn_layout)

        # --- ផ្នែកខាងស្តាំ (Status) ---
        right_panel = QVBoxLayout()
        status_label = QLabel("Awaiting the download")
        status_label.setStyleSheet("background-color: red; color: white; padding: 5px;")
        status_label.setAlignment(Qt.AlignCenter)
        
        self.status_list = QTextEdit()
        self.status_list.setReadOnly(True)
        self.status_list.setStyleSheet("background-color: #f0f0f0; color: black;")

        right_panel.addWidget(status_label)
        right_panel.addWidget(self.status_list)

        # បញ្ចូល Layout ទាំងពីរ
        main_layout.addLayout(left_panel, 60) # ឆ្វេងយក 60%
        main_layout.addLayout(right_panel, 40) # ស្តាំយក 40%

        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VideoDownloaderApp()
    ex.show()
    sys.exit(app.exec_())
