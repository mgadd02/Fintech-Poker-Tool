import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        # Create labels for the outputs
        self.first_output = QLabel(self)
        self.first_output.move(20, 20)
        self.second_output = QLabel(self)
        self.second_output.move(20, 50)
        self.third_output = QLabel(self)
        self.third_output.move(20, 80)

        # Create the "Run" button
        self.run_button = QPushButton("Run", self)
        self.run_button.move(20, 120)
        self.run_button.clicked.connect(self.run)

    def run(self):
        # This is the function that gets called when the "Run" button is clicked
        # Replace the code below with whatever code you want to run when the button is clicked
        self.first_output.setText("First output")
        self.second_output.setText("Second output")
        self.third_output.setText("Third output")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())
