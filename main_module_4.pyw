import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtTest,QtCore
from Modulo4.modulo4_lexico import Lex
from Modulo4.modulo4_syntactic import Syntactic
class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('Modulo4/window.ui',self)
        self.pushButton.clicked.connect(self.process) 
        self.setWindowTitle('Compiler')
        self._tokens = list()

    def process(self):
        file = open('Modulo4/debug.txt', 'w')
        file.write(self.textEdit.toPlainText())
        file.close()
        self.analyzer = Lex()
        self._tokens = self.analyzer._tokens
        print(self._tokens)
        syntactic = Syntactic(len(self._tokens)-1)
        for token in self._tokens:
            syntactic.compare(token[0],token[1])

        print(syntactic.tree)
          

app = QApplication(sys.argv)
ventana = Window()
ventana.show()
app.exec_()