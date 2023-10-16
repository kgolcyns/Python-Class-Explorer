# More qt widgets from class explorer
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from class_explorer import SubclassDiagram as SD
from class_explorer import UMLDiagramer
#TODO: check over not seperate callable part for final errors,
#THEN TODO: have the seperate callable not print section if list is none
# then can returen the false speerate callable to no annotate
def p(items):
    """Quick Printer, prints lines"""
    for x in items: print(x)
#pushbutton = SD(QPushButton)
#pushbutton.run(QCommandLinkButton=20)
#
#dialog = SD(QDialog)
#dialog.run(QErrorMessage=20, QInputDialog=70, QFontDialog=40, QColorDialog=40)



## QAbstract Button and its children + association
#parent
p(UMLDiagramer(QAbstractButton, 65,None, False))

# associated
p(UMLDiagramer(QButtonGroup,17,None, False)) #35 20 17 16

# Children
p(UMLDiagramer(QPushButton, 18,None, False)) # 40 18 17
p(UMLDiagramer(QRadioButton, 18,None, False))
p(UMLDiagramer(QCheckBox, 18,None, False)) 
p(UMLDiagramer(QToolButton, 23)) 
# QPushButton -> child
p(UMLDiagramer(QCommandLinkButton, 20, None, False))


##