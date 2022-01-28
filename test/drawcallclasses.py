from re import T
from uexceptions import *
from helperclasses import *

class udraw_Pixel():
    def __init__(self, position : uPoint, black : bool = True):
        if position != None and black != None: # Requirance check
            self.position = position #Point Class
            self.black = black
        else:
            raise uEXCEPTION_MRA(causing_class = self.__class__.__name__, depth = "Draw Call")

class udraw_Line():
    def __init__(self, start : uPoint, end : uPoint, black = True):
        if start != None and end != None:
            self.start = start
            self.end = end
            self.black = black
        else:
            raise uEXCEPTION_MRA(causing_class = self.__class__.__name__, depth = "Draw Call")

class udraw_Circle():
    def __init__(self, centerPoint : uPoint, radius : int):
        if centerPoint != None and radius != None:
            self.center = centerPoint
            self.radius = radius
        else:
            raise uEXCEPTION_MRA(causing_class = self.__class__.__name__, depth = "Draw Call")

class udraw_Rect():
    def __init__(self, thickness : int = 1, rounded: bool = False, rounding: int = 0, position: uPoint = None, width : int = None, height: int = None, pointA : uPoint = None, pointB : uPoint = None, color = "white"):
        if position == None or width == None or height == None and pointA != None and pointB != None:
            self.pointA = pointA
            self.pointB = pointB
        elif position != None and width != None and height != None:
            self.position = position
            self.width = width
            self.height = height
        else:
            raise uEXCEPTION_RAE(self.__class__.__name__)
        self.thickness = thickness
        self.rounded = rounded
        self.rounding = rounding
        self.color = "white"

class udraw_Oval():
    def __init__(self, pointA, pointB):
        if pointA != None and pointB != None:
            self.pointA = pointA
            self.pointB = pointB
