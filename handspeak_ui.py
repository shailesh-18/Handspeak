from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,
    QFrame, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize
import sys

class HandspeakUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HANDSPEAK")
        self.setGeometry(100, 100, 900, 600)
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout(self)

        # ===== Header with Title and Icon on Left =====
        header_layout = QHBoxLayout()
        
        # Add icon to the left of the header (change to your icon file path)
        header_icon = QLabel()
        header_icon.setPixmap(QIcon("icons/header_icon.png").pixmap(40, 40))  # Adjust the size of the icon
        header_layout.addWidget(header_icon, alignment=Qt.AlignLeft)

        # Title text
        header = QLabel("HANDSPEAK")
        header.setFont(QFont("Arial", 30, QFont.Bold))  # Increased font size
        header.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(header)
        
        header_layout.setAlignment(Qt.AlignCenter)
        main_layout.addLayout(header_layout)

        # ===== Add space between header and body =====
        main_layout.addSpacing(30)  # Increased space after the header

        # ===== Main Body Layout =====
        body_layout = QHBoxLayout()

        # ------ Left Menu ------ 
        menu_layout = QVBoxLayout()
        menu_layout.setAlignment(Qt.AlignCenter)  # Align buttons to the center
        menu_layout.setSpacing(15)  # Increased spacing between buttons

        def menu_button(icon_path, text, color):
            btn = QPushButton(f"  {text}")
            btn.setFont(QFont("Arial", 14, QFont.Bold))  # Increased font size
            btn.setStyleSheet(f"color: {color}; text-align: left; border: none;")
            btn.setIcon(QIcon(icon_path))  
            btn.setIconSize(QSize(30, 30))  # Increased icon size
            btn.setCursor(Qt.PointingHandCursor)
            return btn

        # Add buttons to the menu layout (centered)
        menu_layout.addWidget(menu_button("icons/start.png", "START COMMUNICATION", "green"))
        menu_layout.addWidget(menu_button("icons/history.png", "HISTORY", "red"))
        menu_layout.addWidget(menu_button("icons/manual.png", "USER MANUAL", "red"))
        menu_layout.addWidget(menu_button("icons/settings.png", "SETTINGS", "red"))
        menu_layout.addWidget(menu_button("icons/about.png", "ABOUT", "red"))

        # ===== Add space between the menu and live preview =====
        menu_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # ------ Live Preview Box ------ 
        preview_frame = QFrame()
        preview_frame.setStyleSheet("background-color: black;")
        preview_frame.setMinimumSize(350, 350)

        preview_layout = QVBoxLayout(preview_frame)
        preview_label = QLabel("LIVE PREVIEW")
        preview_label.setStyleSheet("color: white;")
        preview_label.setFont(QFont("Arial", 14))  # Increased font size for preview label
        preview_label.setAlignment(Qt.AlignCenter)
        preview_layout.addWidget(preview_label)

        # Add menu and preview to main body
        body_layout.addLayout(menu_layout)
        body_layout.addWidget(preview_frame)
        main_layout.addLayout(body_layout)

        # ===== Add space between preview and quote =====
        main_layout.addSpacing(30)

        # ===== Quote =====
        quote = QLabel("“Breaking Barriers, One Sign at a Time”")
        quote.setStyleSheet("color: red; font-style: italic;")
        quote.setFont(QFont("Arial", 12))
        quote.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(quote)

        # ===== Add space between quote and accept button =====
        main_layout.addSpacing(30)

        # ===== Accept Button =====
        accept_btn = QPushButton("Accept")
        accept_btn.setFont(QFont("Arial", 16, QFont.Bold))  # Increased font size for the button
        accept_btn.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 2px solid black;
                padding: 12px;
            }
            QPushButton:hover {
                background-color: lightgray;
            }
        """)
        accept_btn.setFixedHeight(60)
        main_layout.addWidget(accept_btn, alignment=Qt.AlignCenter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HandspeakUI()
    window.show()
    sys.exit(app.exec_())


# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,
#     QFrame, QSpacerItem, QSizePolicy
# )
# from PyQt5.QtGui import QFont, QIcon, QPixmap
# from PyQt5.QtCore import Qt, QSize
# import sys

# class HandspeakUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("HANDSPEAK")
#         self.setGeometry(100, 100, 900, 600)
#         self.initUI()

#     def initUI(self):
#         main_layout = QVBoxLayout(self)

#         # ===== Header with Title and Icon on Left =====
#         header_layout = QHBoxLayout()

#         header_icon = QLabel()
#         header_icon.setPixmap(QPixmap("icons/header_icon.png").scaled(40, 40, Qt.KeepAspectRatio))
#         header_layout.addWidget(header_icon, alignment=Qt.AlignLeft)

#         header = QLabel("HANDSPEAK")
#         header.setFont(QFont("Arial", 26, QFont.Bold))
#         header.setAlignment(Qt.AlignCenter)
#         header_layout.addWidget(header)

#         header_layout.addSpacerItem(QSpacerItem(40, 10, QSizePolicy.Expanding))
#         main_layout.addLayout(header_layout)

#         # ===== Add space between header and body =====
#         main_layout.addSpacing(20)

#         # ===== Main Body Layout =====
#         body_layout = QHBoxLayout()

#         # ------ Left Menu ------ 
#         menu_layout = QVBoxLayout()
#         menu_layout.setAlignment(Qt.AlignTop)
#         menu_layout.setSpacing(15)

#         def menu_button(icon_path, text, color):
#             btn = QPushButton(f"  {text}")
#             btn.setFont(QFont("Arial", 14, QFont.Bold))
#             btn.setStyleSheet(f"color: {color}; text-align: left; border: none;")
#             btn.setIcon(QIcon(icon_path))  
#             btn.setIconSize(QSize(30, 30))
#             btn.setCursor(Qt.PointingHandCursor)
#             btn.setFlat(True)
#             btn.setMinimumHeight(40)
#             return btn

#         menu_layout.addWidget(menu_button("icons/start.png", "START COMMUNICATION", "green"))
#         menu_layout.addWidget(menu_button("icons/history.png", "HISTORY", "red"))
#         menu_layout.addWidget(menu_button("icons/manual.png", "USER MANUAL", "red"))
#         menu_layout.addWidget(menu_button("icons/settings.png", "SETTINGS", "red"))
#         menu_layout.addWidget(menu_button("icons/about.png", "ABOUT", "red"))
#         menu_layout.addStretch()

#         # ------ Live Preview Box ------ 
#         preview_frame = QFrame()
#         preview_frame.setStyleSheet("background-color: black;")
#         preview_frame.setMinimumSize(400, 400)

#         preview_layout = QVBoxLayout(preview_frame)
#         preview_label = QLabel("LIVE PREVIEW")
#         preview_label.setStyleSheet("color: white;")
#         preview_label.setFont(QFont("Arial", 16))
#         preview_label.setAlignment(Qt.AlignCenter)
#         preview_layout.addWidget(preview_label)

#         # Add menu and preview to main body
#         body_layout.addLayout(menu_layout)
#         body_layout.addSpacing(40)
#         body_layout.addWidget(preview_frame)
#         main_layout.addLayout(body_layout)

#         # ===== Add space between preview and quote =====
#         main_layout.addSpacing(20)

#         # ===== Quote =====
#         quote = QLabel("\u201cBreaking Barriers, One Sign at a Time\u201d")
#         quote.setStyleSheet("color: red; font-style: italic;")
#         quote.setFont(QFont("Arial", 12))
#         quote.setAlignment(Qt.AlignCenter)
#         main_layout.addWidget(quote)

#         # ===== Add space between quote and accept button =====
#         main_layout.addSpacing(20)

#         # ===== Accept Button =====
#         accept_btn = QPushButton("Accept")
#         accept_btn.setFont(QFont("Arial", 16, QFont.Bold))
#         accept_btn.setStyleSheet(""" 
#             QPushButton {
#                 background-color: white;
#                 border: 2px solid black;
#                 padding: 12px 30px;
#             }
#             QPushButton:hover {
#                 background-color: lightgray;
#             }
#         """)
#         accept_btn.setFixedHeight(50)
#         main_layout.addWidget(accept_btn, alignment=Qt.AlignCenter)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = HandspeakUI()
#     window.show()
#     sys.exit(app.exec_())




