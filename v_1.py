from vpython import *
class visualize():

    def __init__(self, x1,y1,z1,x2,y2,z2,tpx,tpy,tpz):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.tpx = tpx
        self.tpy = tpy
        self.tpz = tpz

        screen = canvas(x=0, y=0,width=1325,height=750,center=vector(5,0,0), background=vector(0,0,0))
        screen.forward = vector(-1,0,0)
        screen.up = vector(0,0,1)

        axis_x = arrow(pos = vector(0,0,0), axis = vector(500,0,0), shaftwidth = 5, color = color.red)
        axis_y = arrow(pos = vector(0,0,0), axis = vector(0,500,0), shaftwidth = 5, color = color.green)
        axis_z = arrow(pos = vector(0,0,0), axis = vector(0,0,500), shaftwidth = 5, color = color.blue)

        xy_plane = box(pos = vector(0,0,0), size = vector(1000,1000,2), color = vector(0.35,0.35,0.35))
        origin = sphere(pos = vector(0,0,0), radius = 10, color = color.white)

        self.a1 = arrow(pos = vector(0,0,0), axis = vector(x1,y1,z1), shaftwidth = 3, color = color.white)
        self.a2 = arrow(pos = vector(0,0,0), axis = vector(x2,y2,z2), shaftwidth = 3, color = color.white)

        self.drone_1 = sphere(pos = vector(x1,y1,z1), radius = 10, color = color.magenta)
        self.drone_2 = sphere(pos = vector(x2,y2,z2), radius = 10, color = color.orange)

        self.skew1 = curve(pos = [(x1,y1,z1),(tpx,tpy,tpz)])
        self.skew2 = curve(pos = [(x2,y2,z2),(tpx,tpy,tpz)])

        self.trail1 = curve(pos = [(x1,y1,z1)])
        self.trail2 = curve(pos = [(x2,y2,z2)])

    def update(self, x1,y1,z1,x2,y2,z2,tpx,tpy,tpz):
        self.a1.axis = vector(x1,y1,z1)
        self.a2.axis = vector(x2,y2,z2)

        self.drone_1.pos = vector(x1,y1,z1)
        self.drone_2.pos = vector(x2,y2,z2)

        self.skew1.visible = 0
        self.skew2.visible = 0
        self.skew1 = curve(pos = [(x1,y1,z1),(tpx,tpy,tpz)])
        self.skew2 = curve(pos = [(x2,y2,z2),(tpx,tpy,tpz)])
        
        self.trail1.append((x1,y1,z1))
        self.trail2.append((x2,y2,z2))
        self.trail3.append((tpx,tpy,tpz))
    
if __name__ == '__main__':

    x1 = 100
    y1 = 100
    z1 = 100
    x2 = 100
    y2 = 300
    z2 = 100
    tpx = 200
    tpy = 200
    tpz = 0
    
    v = visualize(x1,y1,z1,x2,y2,z2,tpx,tpy,tpz)
    
    while 1:
        rate(100)

        x1 += 1
        y2 += 1
        tpx += 2
        if tpx > 400:
            tpx = 0
        if y2 > 400:
            y2 = 0
        if x1 > 400:
            x1 = 0
        
        v.update(x1,y1,z1,x2,y2,z2,tpx,tpy,tpz)
    


