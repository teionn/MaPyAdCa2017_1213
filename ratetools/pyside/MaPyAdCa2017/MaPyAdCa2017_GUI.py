# -*- coding: utf-8 -*-
#コーディング: utf-8
#------------------------------------------------------------------------------
import maya.cmds as cmds
import maya.OpenMaya as OpenMaya

import sys
#------------------------------------------------------------------------------
#Qt.pyを導入している場合
"""
from Qt.QtWidgets import *
from Qt.QtGui import *
from Qt.QtCore import *
"""

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

#GUIの読み込み uiフォルダを作成して from ui import ~ としても良いかと
try :
    import MaPyAdCa2017_GUI_pyside2 as qtGUI ;reload(qtGUI)
except:
    import MaPyAdCa2017_GUI_pyside as qtGUI ;reload(qtGUI)
#------------------------------------------------------------------------------
"""
from ratetools.pyside.MaPyAdCa2017 import MaPyAdCa2017_GUI;reload(MaPyAdCa2017_GUI)
MaPyAdCa2017_GUI.main()
"""

class GUI(QMainWindow):
    ptr = OpenMayaUI.MQtUtil.mainWindow()
    parent = shiboken.wrapInstance(long(ptr), QWidget)

    #settings
    titleName="MaPyAdCa2017_Tool"

    def __init__(self,parent=None):
        super(GUI, self).__init__(self.parent)

        self.ui = qtGUI.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle(self.titleName)

        #button
        #ボタンが押された時(シグナル)の処理(アクション)をコネクションする
        self.ui.pushButton.clicked.connect(self.addList)
        self.ui.pushButton_2.clicked.connect(self.printList)

        #listWidget
        self.ui.listWidget.itemDoubleClicked.connect(self.doubleClickedList)
        #複数選択できるようにする QtDesigner側でも設定できます。(今回はQtDesigner側で設定)
        #self.ui.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)


    def addList(self):#リストを空にしてアウトライナ上で選択しているアイテムをリストに追加する。
        getList=cmds.ls(sl=True)
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(getList)

    def printList(self):#リスト内の選択しているアイテムをプリントする。
        getList=self.ui.listWidget.selectedItems()
        print [x.text() for x in getList]

    def doubleClickedList(self):#ダブルクリックしたらリスト内の選択しているアイテムをアウトライナ上で選択する。
        getList=self.ui.listWidget.selectedItems()
        cmds.select([x.text() for x in getList],r=True)

def main():
    global MaPyAdCa2017_ToolWindow

    try:MaPyAdCa2017_ToolWindow.close()
    except:pass

    app = QApplication.instance()
    MaPyAdCa2017_ToolWindow = GUI()
    MaPyAdCa2017_ToolWindow.show()

    app.exec_()

#main()
