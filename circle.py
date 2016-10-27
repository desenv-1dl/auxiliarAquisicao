import os

from PyQt4 import QtGui, uic
from PyQt4.QtCore import pyqtSignal, pyqtSlot, SIGNAL
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from math import *
from PyQt4.Qt import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QShortcut, QKeySequence
from PyQt4.QtCore import QSettings
from geometricaAquisition import GeometricaAcquisition

class Circle(GeometricaAcquisition):
    def __init__(self, canvas, iface):
        super(Circle, self).__init__(canvas, iface)
        self.canvas = canvas
        self.iface = iface
        self.rubberBand = None
        self.initVariable()
        
    def initVariable(self):
        if self.rubberBand:
            self.rubberBand.reset(True)
            self.rubberBand = None
        self.startPoint = None
        self.endPoint = None
        self.qntPoint = 0
        self.geometry = []
        
    def showCircle(self, startPoint, endPoint):
        nPoints = 50
        x = startPoint.x()
        y = startPoint.y()
        r = sqrt((endPoint.x() - startPoint.x())**2 + (endPoint.y() - startPoint.y())**2)
        self.rubberBand.reset(QGis.Polygon)
        for itheta in range(nPoints+1):
            theta = itheta*(2.0*pi/nPoints)
            self.rubberBand.addPoint(QgsPoint(x+r*cos(theta), y+r*sin(theta)))

    def endGeometry(self):
        self.geometry = self.rubberBand.asGeometry()
        print self.geometry
        self.createGeometry(self.geometry)
  
    def canvasReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if not self.startPoint:
                self.startPoint = QgsPoint(event.mapPoint())
                self.rubberBand = self.getRubberBand()
        if event.button() == Qt.RightButton:
            self.endGeometry()
               
    def canvasMoveEvent(self, event):
        if self.startPoint:
            self.endPoint = QgsPoint(event.mapPoint())
            self.showCircle(self.startPoint, self.endPoint)
            
            
            
            
            
            
            
            
            
            
            
            