from vpython import *
import numpy as np

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

        #xy_plane = box(pos = vector(0,0,0), size = vector(1000,1000,2), color = vector(0.35,0.35,0.35))
        origin = sphere(pos = vector(0,0,0), radius = 10, color = color.white)

        self.a1 = arrow(pos = vector(0,0,0), axis = vector(x1,y1,z1), shaftwidth = 3, color = color.white)
        self.a2 = arrow(pos = vector(0,0,0), axis = vector(x2,y2,z2), shaftwidth = 3, color = color.white)

        self.drone_1 = sphere(pos = vector(x1,y1,z1), radius = 10, color = color.magenta)
        self.drone_2 = sphere(pos = vector(x2,y2,z2), radius = 10, color = color.orange)

        self.skew1 = curve(pos = [(x1,y1,z1),(tpx,tpy,tpz)])
        self.skew2 = curve(pos = [(x2,y2,z2),(tpx,tpy,tpz)])

        self.trail1 = points(pos = [(x1,y1,z1)],radius = 2, color = color.magenta)
        self.trail2 = points(pos = [(x2,y2,z2)],radius = 2, color = color.orange)
        self.trail3 = points(ps = [(tpx,tpy,tpz)],radius = 2, color = color.white)
        
        self.drone1_stats = label(pos = vector(0,0,150), text = 'Drone_1 \n Lat: '+str(x1)+'\nLong: '+str(y1)+'\nAlt: '+str(z1))
        self.drone2_stats = label(pos = vector(-500,-500,0), text = 'Drone_2 \n Lat: '+str(x2)+'\nLong: '+str(y2)+'\nAlt: '+str(z2))


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

        self.drone1_stats.visible = 0
        self.drone2_stats.visible = 0
        self.drone1_stats = label(pos = vector(-500,-500,500), text = 'Drone_1 \n Lat: '+str(x1)+'\nLong: '+str(y1)+'\nAlt: '+str(z1))
        self.drone2_stats = label(pos = vector(-500,-500,0), text = 'Drone_2 \n Lat: '+str(x2)+'\nLong: '+str(y2)+'\nAlt: '+str(z2))
    
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

    sd = 12.5
    n = 50
    
    x = np.random.normal(x1,sd,n)
    y = np.random.normal(y1,sd,n)
    z = np.random.normal(z1,sd,n)

    g = np.random.normal(x2,sd,n)
    h = np.random.normal(y2,sd,n)
    j = np.random.normal(z2,sd,n)

    q = np.random.normal(tpx,sd,n)
    w = np.random.normal(tpy,sd,n)
    e = np.random.normal(tpz,sd,n)

    v = visualize(x1,y1,z1,x2,y2,z2,tpx,tpy,tpz)
    i=0
    while 1:
        rate(10)
        i=i+1
        v.update(x[i],y[i],z[i],g[i],h[i],j[i],q[i],w[i],0)
        if i == (n-1):
            i=0


