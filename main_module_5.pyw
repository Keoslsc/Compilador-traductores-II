import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtTest,QtCore
from Modulo5.modulo5_lexico import Lex
from Modulo5.modulo5_syntactic import Syntactic
from Modulo5.modulo5_semantic import Semantic
class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('Modulo5/window.ui',self)
        self.pushButton.clicked.connect(self.process) 
        self.setWindowTitle('Compiler')
        self._tokens = list()

    def process(self):
        file = open('Modulo5/debug.txt', 'w')
        file.write(self.textEdit.toPlainText())
        file.close()
        self.analyzer = Lex()
        self._tokens = self.analyzer._tokens
        print(self._tokens)
        syntactic = Syntactic(len(self._tokens)-1)
        for token in self._tokens:
            syntactic.compare(token[0],token[1])
        semantic = Semantic(syntactic.tree)
        semantic.createTables()
        semantic.checkErrors()
          

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()