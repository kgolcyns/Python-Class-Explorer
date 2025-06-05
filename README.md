# Python-Class-Explorer
Easy diagram overview of subclasses of a class.

## Example Printing Subclasses of QWidget from PyQt5
```python
from class_explorer import SubclassDiagram as SD
from PyQt5.QtWidgets import *

# Initilize with class, then provide subclasses with column width.
qwidget = SD(QWidget)
qwidget.run(QAbstractButton=60, QFrame=60, QAbstractSlider=50,
            QAbstractSpinBox=50, QDialog=30, QComboBox=65, QDesktopWidget=40,
            QDialogButtonBox=55, QDockWidget=45, QFocusFrame=16, QGroupBox=40,
            QKeySequenceEdit=20, QLineEdit=75, QMainWindow=75, QMdiSubWindow=45,
            QMenu=65,QMenuBar=35, QOpenGLWidget=45, QProgressBar=60,
            QRubberBand=18, QSizeGrip=12, QSplashScreen=18, QSplitterHandle=23,
            QStatusBar=25, QTabBar=75, QTabWidget=75, QToolBar=65, QWizardPage=45)
```
