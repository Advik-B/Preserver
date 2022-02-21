import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QDesktopWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class MainUI(QWidget):
    def __init__(self, parent=None, **kwargs) -> None:
        super().__init__(parent, **kwargs)
        self.initUI()
    
    def initUI(self) -> None:
        self.setWindowTitle('GUI with Qt5')
        # Get the screen size of the primary screen
        desktop = QApplication.desktop()
        screenRect = desktop.screenGeometry()
        # Set the maximum size of the window
        self.setMaximumSize(screenRect.width() // 2, screenRect.height() // 2)
        self.resize(screenRect.width() // 2, screenRect.height() // 2)
        self.move(screenRect.width() // 4, screenRect.height() // 4)
        # Set the minimum size of the window
        self.setMinimumSize(screenRect.width() // 4, screenRect.height() // 4)
        # Set the window flags
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # All the window flags
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint)
        # self.setWindowFlags(Qt.WindowSystemMenuHint)
        # self.setWindowFlags(Qt.WindowTitleHint)
        # self.setWindowFlags(Qt.WindowFullscreenButtonHint)
        # self.setWindowFlags(Qt.WindowContextHelpButtonHint)
        # self.setWindowFlags(Qt.WindowShadeButtonHint)
        # self.setWindowFlags(Qt.WindowStaysOnBottomHint)
        # self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint)
        # self.setWindowFlags(Qt.WindowSystemMenuHint)
        # self.setWindowFlags(Qt.WindowTitleHint)
        # self.setWindowFlags(Qt.WindowFullscreenButtonHint)
        # self.setWindowFlags(Qt.WindowContextHelpButtonHint)
        # self.setWindowFlags(Qt.WindowShadeButtonHint)
        # self.setWindowFlags(Qt.WindowStaysOnBottomHint)
        # self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint)
        # self.setWindowFlags(Qt.WindowSystemMenuHint)
        # self.setWindowFlags(Qt.WindowTitleHint)
        # self.setWindowFlags(Qt.WindowFullscreenButtonHint)
        # self.setWindowFlags(Qt.WindowContextHelpButtonHint)
        # self.setWindowFlags(Qt.WindowShadeButtonHint)
        # self.setWindowFlags(Qt.WindowStaysOnBottomHint)
        # self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        # self.setWindowFlags(Qt.WindowMaximizeButtonHint)
        # Initialize the widgets
        self.initWidgets()
        # Show the window
        self.show()
    
    def initWidgets(self):
        self.desktop = QDesktopWidget()
        
def main():
    app = QApplication(sys.argv)
    windows = MainUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
