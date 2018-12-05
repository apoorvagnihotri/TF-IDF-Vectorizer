import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import tfidf as src

# Credits: pythonspot.com
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'tf-idf Demo'
        self.left = 400
        self.top = 400
        self.width = 1050
        self.height = 220
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # Height
        a = 100
        wi = 1000
        font = QFont("Times", 20, QFont.Bold) 

        # Create OpenFileButton
        self.uploadButton = QPushButton('Open Training File', self)
        self.uploadButton.clicked.connect(self.open_file)
        self.uploadButton.resize(130,30)
        self.uploadButton.move(20, a-90)

        # Create TrainedOnFileLabel
        self.TrainedON = QLabel(self)
        self.TrainedON.setText("Trained on :")
        self.TrainedON.resize(wi-600,30)
        self.TrainedON.move(400, a-90)

        # Create a Parent Label
        self.label = QLabel(self)
        self.label.setText("TFIDF Vectorize")
        self.label.resize(wi,40)
        self.label.setFont(font)
        self.label.move(20, a-60)

        # Create a main Label
        self.label_names = QLabel(self)
        self.label_names.setText("Made by: Apoorv")
        font = QFont("Times", 14) 
        self.label_names.setFont(font)
        self.label_names.resize(wi,40)
        self.label_names.move(20, a-25)

        # Create opened file textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, a + 20)
        self.textbox.resize(wi,40)
 
        # Create a button in the window
        self.button = QPushButton('Calc. tfidf vector', self)
        self.button.move(wi-100, a + 80)
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    def tf_idf(sentence):
        return len(sentence)

    def open_file(self):
        fileName = QFileDialog.getOpenFileName(self, 'OpenFile')
        self.TrainedON.setText("Trained on : "+fileName[0])
        self.trained_tfidf = src.TFIDFtrain(fileName[0]) 
 
    @pyqtSlot()
    def on_click(self):
        sentence = self.textbox.text()
        tf_idf_vec = src.get_vector(sentence, self.trained_tfidf)
        print('tf_idf_vec: ', str(tf_idf_vec))
        QMessageBox.question(self, "Output", "tf_idf_vec: " + str(tf_idf_vec), QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

# this car got the excellence award
