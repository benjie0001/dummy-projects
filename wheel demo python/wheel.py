from graphics import*
#class do define methods that draw the wheel
class Wheel(object):
    def __init__(self, center, wheel_radius, tire_radius):
        self.tire_circle=Circle(center, tire_radius)
        self.wheel_circle=Circle(center,wheel_radius)

    def draw(self,win):
        self.tire_circle.draw(win)
        self.wheel_circle.draw(win)

    def move (self, dx, dy):
        self.tire_circle.move(dx,dy)
        self.wheel_circle.move(dx,dy)

    def set_color(self, wheel_color, tire_color):
        self.tire_circle.setFill(tire_color)
        self.wheel_circle.setFill(wheel_color)

    def undraw (self):
        self.tire_circle.undraw()
        self.wheel_circle.undraw()

    def get_size(self):
        return self.tire_circle.getRadius()

    def get_centre(self):
        return self.tire_circle.getCenter()

    def animate(self, win ,dx, dy,n):
        if n>0:
            self.move(dx, dy)
            win.after(100, self.animate,win, dx,dy, n-1)
            
def main():
    win=GraphWin("Wheel", 700,500)
    win.setBackground(color_rgb(200, 40,40))
    pt=Point(200,200)
    wh= Wheel(pt, 100,150)
    wh.draw(win)
    wh.move(10,10)
    wh.set_color(color_rgb(50,50,50),color_rgb(30,30,30))
    wh.get_size()
    wh.get_centre()
    wh.animate(win,10,10,10)
    

    win.getMouse()
    win.close()
    
main()


