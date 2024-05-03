import sys
from PySide6.QtWidgets import QApplication
import qdarkstyle
from gui import MainWindow  # Assuming gui.py contains your MainWindow class

def main():
    app = QApplication([])
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    show_main_window()

    sys.exit(app.exec())

def show_main_window():
    window = MainWindow()
    window.show()

if __name__ == "__main__":
    main()
