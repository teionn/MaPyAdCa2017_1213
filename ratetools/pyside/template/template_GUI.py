# -*- coding: utf-8 -*-
#コーディング: utf-8
#------------------------------------------------------------------------------
import maya.cmds as cmds
import maya.OpenMaya as OpenMaya

import sys
#------------------------------------------------------------------------------
#Qt.pyを導入している場合
"""from Qt.QtWidgets import *
from Qt.QtGui import *
from Qt.QtCore import *"""

#Qt.pyを導入していない場合
try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
except:
    from PySide.QtCore import *
    from PySide.QtGui import *

#shibokenの読み込み
try :
    import shiboken2 as shiboken
except:
    import shiboken

#OpenMayaUIの読み込み 人によっては as omUI と書く場合も
import maya.OpenMayaUI as OpenMayaUI

#GUIの読み込み
try :
    import template_GUI_pyside2 as qtGUI ;reload(qtGUI)
except:
    import template_GUI_pyside as qtGUI ;reload(qtGUI)
#------------------------------------------------------------------------------
"""
from ratetools.pyside.template import template_GUI;reload(template_GUI)
template_GUI.main()
"""

class GUI(QMainWindow):
    ptr = OpenMayaUI.MQtUtil.mainWindow()
    parent = shiboken.wrapInstance(long(ptr), QWidget)

    #settings
    titleName="testTool"

    def __init__(self,parent=None):
        super(GUI, self).__init__(self.parent)

        self.ui = qtGUI.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle(self.titleName)


def main():
    global testToolWindow

    try:testToolWindow.close()
    except:pass

    app = QApplication.instance()
    testToolWindow = GUI()
    testToolWindow.show()

    app.exec_()

#main()
