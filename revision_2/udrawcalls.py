from textwrap import fill
from helperclasses import *
from uexceptions import *

class udraw_Pixel():
    def __init__(
                self, 
                position : uPoint,
                highlight : bool = True
                ):
        if position != None: # Requirance check
            self.position = position #Point Class
            self.highlight = highlight
        else:
            raise uDRAWEXCEPTION(widget = self.__class__.__name__, message = "")

class udraw_Line():
    def __init__(
            self,
            pointA : uPoint = None,
            pointB: uPoint = None,
            highlight: bool = True
            ):
        if pointA == None or pointB == None:
            raise uDRAWEXCEPTION(widget=self.__class__.__name__, message = "Draw needs both start and endpoint")
        self.pointA = pointA
        self.pointB = pointB
        self.highlight = highlight

class udraw_Rectangle():
    def __init__(
            self, 
            pointA : uPoint = None,
            pointB : uPoint = None,
            border_is_highlight : bool = True,
            thickness : int = 1,
            rounding : int = 0,
            round_oct : bool = True,
            filled : bool = False,
            fill_match_border : bool = False,
            is_debug : bool = False
            ):
        if pointA == None or pointB == None:
            raise uDRAWEXCEPTION(widget = self.__class__.__name__, message = "Draw needs both start and endpoint")
        self.pointA = pointA
        self.pointB = pointB
        self.border_is_highlight = border_is_highlight
        self.thickness = thickness
        self.rounding = rounding
        self.round_oct = round_oct
        self.filled = filled
        self.fill_border = fill_match_border
        self.is_debug = is_debug

    def out(self):
        return f"udraw_Rectangle @" + self.pointA.out() + self.pointB.out() + "border_is_highlight: " + str(self.border_is_highlight) + ", thickness: " + str(self.thickness) + ", rounding: " + str(self.rounding) + ", round_oct: " + str(self.round_oct) + ", filled: " + str(self.filled) + ", fill_match_border: " + str(self.fill_border) + ", is_debug: " + str(self.is_debug)
class udraw_Circle():
    def __init__(
            self,
            point : uPoint = None,
            radius : int = 1,
            highlight : bool = True
            ):
        if point == None:
            raise uDRAWEXCEPTION(widget = self.__class__.__name__, message = "Draw needs a centerpoint.")
        self.point = point,
        self.radius = radius
        self.highlight = highlight


