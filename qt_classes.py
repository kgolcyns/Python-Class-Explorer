# pyqt_classes.py
# Runs class_explorer for inputted classes
from PyQt5.QtWidgets import *
from class_explorer import SubclassDiagram as SD
# QWidget

qwidget = SD(QWidget)
qwidget.run(QAbstractButton=60, QFrame=60, QAbstractSlider=50,
            QAbstractSpinBox=50, QDialog=30, QComboBox=65, QDesktopWidget=40,
            QDialogButtonBox=55, QDockWidget=45, QFocusFrame=16, QGroupBox=40,
            QKeySequenceEdit=20, QLineEdit=75, QMainWindow=75, QMdiSubWindow=45,
            QMenu=65,QMenuBar=35, QOpenGLWidget=45, QProgressBar=60,
            QRubberBand=18, QSizeGrip=12, QSplashScreen=18, QSplitterHandle=23,
            QStatusBar=25, QTabBar=75, QTabWidget=75, QToolBar=65, QWizardPage=45)

#qabstractbutton = SD(QAbstractButton)
#qabstractbutton.run()
#
#qpushbutton = SD(QPushButton)
#qpushbutton.run()
#
#qframe = SD(QFrame)
#qframe.run()
#
#qabstractscrollarea = SD(QAbstractScrollArea)
#qabstractscrollarea.run()
#
#qtextedit = SD(QTextEdit)
#qtextedit.run()


## --Completed Formatting:
##qabstractitemview = SD(QAbstractItemView)
##qabstractitemview.run(QColumnView=25, QListView=75, QTableView=75, QTreeView = 75)
##
##qlistview = SD(QListView)
##qlistview.run(QUndoView=16)
##
##qtableview = SD(QTableView)
##qtableview.run()
##
##qtreeview = SD(QTreeView)
##qtreeview.run()
