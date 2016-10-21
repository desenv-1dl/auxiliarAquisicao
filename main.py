# -*- coding: utf-8 -*-
from PyQt4.QtGui import QIcon, QPixmap, QAction
from qgis.gui import QgsMessageBar
from circle import Circle
from polygon import Polygon
class Main:
    def __init__(self, iface):
        self.iface = iface
        self.canvas = iface.mapCanvas()
                    
    def initGui(self):
        self.action1 = QAction(QIcon(QPixmap(["18 17 4 1",
                                    "           c None",
                                    "#          c #FF0000",
                                    ".          c #FF0000",
                                    "+          c #1210f3",
                                    "        +        ",
                                    "       +++       ",
                                    "      +++++      ",
                                    "     +++++++     ",
                                    "    +++++++++    ", 
                                    "   +++++++++++   ",
                                    "  +++++++++++++  ",
                                    " +++++++++++++++ ",
                                    "+++++++++++++++++",
                                    "+++++++++++++++++",
                                    "++             ++", 
                                    "++             ++",
                                    "++     +++     ++",
                                    "++    ++ ++    ++",
                                    "++    ++ ++    ++",
                                    "+++++++++++++++++",
                                    "+++++++++++++++++",])), u"Editor de Edificações", self.iface.mainWindow())
        self.action2 = QAction(QIcon(QPixmap(["17 13 2 1",
                                    "           c None",
                                    "+          c #FF0000",
                                    "    +++++++++    ", 
                                    "   +++++++++++   ",
                                    "  ++         ++  ",
                                    " ++           ++ ",
                                    "++             ++",
                                    "++             ++",
                                    "++             ++", 
                                    "++             ++",
                                    "++             ++",
                                    " ++            ++",
                                    "  ++         ++  ",
                                    "   +++++++++++   ",
                                    "    +++++++++    ",])), u"Editor de Edificações", self.iface.mainWindow())
        self.action1.setEnabled(True)
        self.action1.triggered.connect(lambda:self.run(Polygon))
        self.iface.digitizeToolBar().addAction(self.action1)
        self.action2.setEnabled(True)
        self.action2.triggered.connect(lambda:self.run(Circle))
        self.iface.digitizeToolBar().addAction(self.action2)
        
    def unload(self):
        pass  
      
    def run(self, func):
        layer = self.canvas.currentLayer()
        if layer in self.iface.editableLayers():
            if layer.geometryType() == 2:
                func(self.canvas, self.iface)
            else:
                self.iface.messageBar().pushMessage(u"Aviso", u"Ferramenta utilizada apenas em polígonos !",
                                                                    level=QgsMessageBar.INFO, duration=6)
        else:
            self.iface.messageBar().pushMessage(u"Aviso", u"Inicie a Edição da Feição!",
                                                                    level=QgsMessageBar.INFO, duration=6)
            