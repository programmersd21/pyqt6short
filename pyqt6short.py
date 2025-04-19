"""
A library for creating hassle-free PyQt6 apps in shorter ways.
"""

class GuiApps(object):
    """
    The class containing a collection PyQt6 GUI apps in the form of functions.
    """
    
    def __init__(self) -> None:
        super(GuiApps, self).__init__()

    def basic_app(self, title: str) -> None:
        """
        A basic app with pretty much nothing more than a blank window.
        """
        from PyQt6.QtWidgets import QApplication, QWidget
        import sys

        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowTitle(title)
        window.show()
        app.exec()

    def basic_app_with_widgets(self, title: str) -> None:
        """
        A basic app with widgets.
        """
        import sys
        from PyQt6.QtCore import QSize
        from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

        class MainWindow1(QMainWindow):
            def __init__(self):
                super().__init__()
                self.setWindowTitle(title)
                button = QPushButton("Press Me!")
                self.setFixedSize(QSize(400, 300))
                # Set the central widget of the Window.
                self.setCentralWidget(button)

        app = QApplication(sys.argv)
        window = MainWindow1()
        window.show()
        app.exec()

    def basic_app_with_signals(self, title: str) -> None:
        """
        A basic app with signals.
        """
        import sys
        from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

        class MainWindow2(QMainWindow):
            def __init__(self):
                super().__init__()
                self.setWindowTitle(title)

                button = QPushButton("Press Me!")
                button.setCheckable(True)
                button.clicked.connect(self.the_button_was_clicked)
                button.clicked.connect(self.the_button_was_toggled)

                # Set the central widget of the Window.
                self.setCentralWidget(button)

            def the_button_was_clicked(self):
                print("Clicked!")

            def the_button_was_toggled(self, checked):
                print("Checked?", checked)

        app = QApplication(sys.argv)
        window = MainWindow2()
        window.show()
        app.exec()
    
    def all_widgets_app(self, title: str):
        import sys
        from PyQt6.QtWidgets import (
            QApplication,
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLabel,
            QLCDNumber,
            QLineEdit,
            QMainWindow,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
            QVBoxLayout,
            QWidget,
        )

        # Subclass QMainWindow to customize your application's main window
        class MainWindow3(QMainWindow):
            def __init__(self):
                super().__init__()

                self.setWindowTitle(title)

                layout = QVBoxLayout()
                widgets = [
                    QCheckBox,
                    QComboBox,
                    QDateEdit,
                    QDateTimeEdit,
                    QDial,
                    QDoubleSpinBox,
                    QFontComboBox,
                    QLCDNumber,
                    QLabel,
                    QLineEdit,
                    QProgressBar,
                    QPushButton,
                    QRadioButton,
                    QSlider,
                    QSpinBox,
                    QTimeEdit,
                ]

                for w in widgets:
                    layout.addWidget(w())

                widget = QWidget()
                widget.setLayout(layout)

                # Set the central widget of the Window. Widget will expand
                # to take up all the space in the window by default.
                self.setCentralWidget(widget)

        app = QApplication(sys.argv)
        window = MainWindow3()
        window.show()
        app.exec()

class GuiWidgets(object):
    """
        Still in development!
    """
    ...

class Examples(object):
    """The class for Example"""
    def __init__(self) -> None:
        super(Examples, self).__init__()
        
    def run_basic_app(self):
        gui = GuiApps()
        gui.basic_app("myapp1")

    def run_basic_app_with_widgets(self):
        gui = GuiApps()
        gui.basic_app_with_widgets("myapp2")

    def run_basic_app_with_signals(self):
        gui = GuiApps()
        gui.basic_app_with_signals("myapp3")
        
    def run_all_widgets_app(self):
        gui = GuiApps()
        gui.all_widgets_app("myapp4")

    def run(self):
        from multiprocessing import Process
        
        # List of processes
        processes = [
            Process(target=self.run_basic_app),
            Process(target=self.run_basic_app_with_widgets),
            Process(target=self.run_basic_app_with_signals),
            Process(target=self.run_all_widgets_app)
        ]

        # Start all processes in a loop
        for process in processes:
            process.start()

        # Wait for all processes to complete
        for process in processes:
            process.join()