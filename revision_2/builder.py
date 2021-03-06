from low_level_nodes import *
import miscvalues as miscv
import systemvalues as sysv
import graphics

class DISPLAY():
    def __init__(self, head):
        sysv.global_addL("darkmode_enabled", self)
        miscv.global_addL("debug_draw_constraints", self)
        sysv.global_addL("node_requests_redraw", self)
        self.head = head
        self.ready = self.head.assign_depth(0)
        self.ready = self.head.constrainmod()
        self.ready = self.head.output()
        self.wallpaper = GraphWin("WallPaper", head.constraints.pointB.x, head.constraints.pointB.y)
        self.wallpaper.setBackground(miscv.dark_color if sysv.darkmode_enabled else miscv.light_color)
        self.redraw_all()
        self.enter_update_loop()

    def notify(self, name, value):
        if name == "darkmode_enabled":
            self.wallpaper.setBackground(miscv.dark_color if value else miscv.light_color)
            self.redraw_all()
        elif name == "debug_draw_constraints":
            self.redraw_all()
        elif name == "node_requests_redraw":
            self.redraw_all()
        
    def redraw_all(self):
        self.last_draw_calls = self.head.draw()
        for single_call in self.last_draw_calls:
            print(single_call.out())
        calls = self.last_draw_calls
        highlight_color = miscv.light_color if sysv.darkmode_enabled else miscv.dark_color
        background_color = miscv.dark_color if sysv.darkmode_enabled else miscv.light_color
        for call in calls:
            if call.__class__.__name__ == "udraw_Rectangle":
                obj = Rectangle(call.pointA.to_point(), call.pointB.to_point())
                obj.setOutline(highlight_color if call.border_is_highlight else background_color)
                if call.is_debug:
                    obj.setOutline("red")
                if call.filled:
                    obj.setFill(highlight_color if ((call.border_is_highlight and call.fill_border) or (call.border_is_highlight and not call.fill_border)) else background_color)
                obj.setWidth(call.thickness)
                obj.draw(self.wallpaper)
        
        
                

    def enter_update_loop(self):
        while True:
            input()
            sysv.global_edit("darkmode_enabled", "foo")

tree = uHEAD(
    props = {
    "width":880,
    "height":528,
    },
    child=uPBOX())
 

wallpaper = DISPLAY(
    head = tree
)

    
