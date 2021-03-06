import sys
from PySide.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Find and Replace")
        self.setGeometry(100, 100, 270, 200)

        self.findLabel = QLabel("Search for :", self)
        self.findLabel.setStyleSheet("font-size: 15px;")
        self.findLabel.move(10, 10)

        self.findText = QTextEdit(self)
        self.findText.setStyleSheet("font-size: 15px;")
        self.findText.move(10, 30)
        self.findText.resize(250, 25)

        self.findLabel = QLabel("Repalce all :", self)
        self.findLabel.setStyleSheet("font-size: 15px;")
        self.findLabel.move(10, 70)

        self.replaceText = QTextEdit(self)
        self.replaceText.setStyleSheet("font-size: 15px;")
        self.replaceText.move(10, 85)
        self.replaceText.resize(250, 25)

        self.fountLabel = QLabel("", self)
        self.fountLabel.setStyleSheet("font-size: 15px;")
        self.fountLabel.move(10, 120)
        self.fountLabel.resize(200, 30)

        self.Button1 = QPushButton('Find', self)
        self.Button1.resize(40, 30)
        self.Button1.move(80, 150)

        self.Button2 = QPushButton('Replace All', self)
        self.Button2.resize(75, 30)
        self.Button2.move(120, 150)

        self.Button3 = QPushButton('Close', self)
        self.Button3.resize(60, 30)
        self.Button3.move(195, 150)
        self.Button3.clicked.connect(self.hideForm)

    def hideForm(self):
        self.hide();


class MainWindow(QMainWindow):
    def __init__(self, fileName=None):
        QMainWindow.__init__(self)
        self.setWindowTitle("A Simple Text Editor")
        self.setWindowIcon(QIcon('appicon.png'))
        self.setGeometry(100, 100, 800, 600)
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.fileName = None
        self.filters = "Text files (*.txt)"

    def SetupComponents(self):
        self.myStatusBar = QStatusBar()
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage('Ready', 10000)
        self.CreateActions()
        self.CreateMenus()
        self.CreateToolBar()
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.editMenu.addAction(self.cutAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addAction(self.findAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.undoAction)
        self.editMenu.addAction(self.redoAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.selectAllAction)
        self.formatMenu.addAction(self.fontAction)
        self.helpMenu.addAction(self.aboutAction)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.aboutQtAction)
        self.mainToolBar.addAction(self.newAction)
        self.mainToolBar.addAction(self.openAction)
        self.mainToolBar.addAction(self.saveAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.cutAction)
        self.mainToolBar.addAction(self.copyAction)
        self.mainToolBar.addAction(self.pasteAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.undoAction)
        self.mainToolBar.addAction(self.redoAction)

    def newFile(self):
        self.textEdit.setText('')
        self.fileName = None

    def openFile(self):
        self.fileName, self.filterName = QFileDialog.getOpenFileName(self)
        self.textEdit.setText(open(self.fileName).read())

    def saveFile(self):
        if self.fileName == None or self.fileName == '':
            self.fileName, self.filterName = QFileDialog.getSaveFileName(self, filter=self.filters)
        if(self.fileName != ''):
            file = open(self.fileName, 'w')
            file.write(self.textEdit.toPlainText())
            self.statusBar().showMessage("File saved", 2000)

    def exitFile(self):
        self.close()

    def fontChange(self):
        (font, ok) = QFontDialog.getFont(QFont("Helvetica[Cronyx]", 10), self)
        if ok:
            self.textEdit.setCurrentFont(font)

    def aboutHelp(self):
        QMessageBox.about(self, "About Simple Text Editor A Simple Text Editor where you can edit and save files")

    def CreateActions(self):
        self.newAction = QAction( QIcon('new.png'), '&New', self, shortcut=QKeySequence.New, statusTip="Create a New File", triggered=self.newFile)
        self.openAction = QAction( QIcon('open.png'), 'O&pen', self, shortcut=QKeySequence.Open, statusTip="Open an existing file", triggered=self.openFile)
        self.saveAction = QAction( QIcon('save.png'), '&Save', self, shortcut=QKeySequence.Save, statusTip="Save the current file to disk", triggered=self.saveFile)
        self.exitAction = QAction( QIcon('exit.png'), 'E&xit', self, shortcut="Ctrl+Q", statusTip="Exit the Application", triggered=self.exitFile)
        self.cutAction = QAction( QIcon('cut.png'), 'C&ut', self, shortcut=QKeySequence.Cut, statusTip="Cut the current selection to clipboard", triggered=self.textEdit.cut)
        self.copyAction = QAction( QIcon('copy.png'), 'C&opy', self, shortcut=QKeySequence.Copy, statusTip="Copy the current selection to clipboard", triggered=self.textEdit.copy)
        self.pasteAction = QAction( QIcon('paste.png'), '&Paste', self, shortcut=QKeySequence.Paste, statusTip="Paste the clipboard's content in current location", triggered=self.textEdit.paste)
        self.findAction = QAction( QIcon('cut.png'), '&Find', self, shortcut=QKeySequence.Find, statusTip="Search and Replace Word", triggered=self.findAndReplace)
        self.selectAllAction = QAction( QIcon('selectAll.png'), 'Select All', self, statusTip="Select All", triggered=self.textEdit.selectAll)
        self.redoAction = QAction( QIcon('redo.png'),'Redo', self, shortcut=QKeySequence.Redo, statusTip="Redo previous action", triggered=self.textEdit.redo)
        self.undoAction = QAction( QIcon('undo.png'),'Undo', self, shortcut=QKeySequence.Undo, statusTip="Undo previous action", triggered=self.textEdit.undo)
        self.fontAction = QAction( 'F&ont', self, statusTip = "Modify font properties", triggered = self.fontChange)
        self.aboutAction = QAction( QIcon('about.png'), 'A&bout', self, statusTip="Displays info about text editor", triggered=self.aboutHelp)
        self.aboutQtAction = QAction("About &Qt", self, statusTip="Show the Qt library's About box", triggered=qApp.aboutQt)

    def CreateMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.formatMenu = self.menuBar().addMenu("F&ormat")
        self.helpMenu = self.menuBar().addMenu("&Help")

    def CreateToolBar(self):
        self.mainToolBar = self.addToolBar('Main')

    def findAndReplace(self):
        formFind = Form(self)
        formFind.show()

        def countWord():
            formFind.fountLabel.setText("Jumlah kata : {}".format(self.textEdit.toPlainText().count(formFind.findText.toPlainText())))

        def replaceWord():
            formFind.fountLabel.setText("Jumlah kata di ganti : {}".format(self.textEdit.toPlainText().count(formFind.findText.toPlainText())))
            return self.textEdit.setText(self.textEdit.toPlainText().replace(formFind.findText.toPlainText(), formFind.replaceText.toPlainText()))

        formFind.Button1.clicked.connect(countWord)
        formFind.Button2.clicked.connect(replaceWord)


if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.SetupComponents()
        mainWindow.show()

        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
