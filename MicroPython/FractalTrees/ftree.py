# notify
print('LOAD: ftree.py')

import os,sys,time
import math

class FTree:

    # variables
    canvas_width  = 128
    canvas_height = 64

    # make random tree
    def rtree(self,sx,sy):

        angle2  = 10 + self.randint(45) # branch angle
        length1 = 8 + self.randint(8) # start length of trunk
        length2 = (68 + self.randint(16))/100 # decimal reduction factor 
        width1  = 1 # not implemented
        width2  = 1 # not implemented
        left2right = self.randint(1) # draw left to right

        print('RTREE:',[angle2,length1,length2,width1,width2,left2right])

        yield from self.trunk(sx,sy,90,angle2,length1,length2,width1,width2,left2right)

    # start a tree (angle1 ignored)
    def trunk(self,sx,sy,angle1,angle2,length1,length2,width1,width2,left2right):

        yield from self.draw_branch(sx,sy,sx,sy+length1,width1)
        yield from self.branch(sx,sy+length1,90,angle2,length1,length2,width1,width2,left2right)

    # recursive branch function
    def branch(self,sx,sy,angle1,angle2,length1,length2,width1,width2,left2right):

        # sx,sy = branch start coordinates
        # angle1 = the angle of the incoming branch
        # angle2 = the deviation from angle1 of the outgoing branches (true angle)
        # length1 = the length of the incoming branch
        # length2 = the deviation from length1 of outgoing branches (decimal multiplier)
        # width1 = the width of the incoming branch
        # width2 = the deviation from width1 of outgoing branches (decimal multiplier)

        if length1 >= 1: # stop recursion

            l3 = min(length1-1,self.rint(length1*length2)) # actual lenght, at least 1 less to prevent infinite loop
            w3 = self.rint(width1*width2) # actual width

            la = angle1+angle2
            ra = angle1-angle2
            
            lx,ly = self.math_polar(la,l3)
            rx,ry = self.math_polar(ra,l3)

            if left2right:

                yield from self.draw_branch(sx,sy,sx+lx,sy+ly,w3) # this branch left
                yield from self.branch(sx+lx,sy+ly,la,angle2,l3,length2,w3,width2,left2right) # sub branches

                yield from self.draw_branch(sx,sy,sx+rx,sy+ry,w3) # this branch right
                yield from self.branch(sx+rx,sy+ry,ra,angle2,l3,length2,w3,width2,left2right) # sub branches

            else:

                yield from self.draw_branch(sx,sy,sx+rx,sy+ry,w3) # this branch right
                yield from self.branch(sx+rx,sy+ry,ra,angle2,l3,length2,w3,width2,left2right) # sub branches

                yield from self.draw_branch(sx,sy,sx+lx,sy+ly,w3) # this branch left
                yield from self.branch(sx+lx,sy+ly,la,angle2,l3,length2,w3,width2,left2right) # sub branches


    def draw_branch(self,x1,y1,x2,y2,w):

        # draw a line

        xdiff = x2-x1
        ydiff = y2-y1

        if (xdiff or ydiff) and w:

            if abs(xdiff) >= abs(ydiff):
                steps = abs(xdiff)
                xwidth = False
            else:
                steps = abs(ydiff)
                xwidth = True

            xstep = xdiff/steps
            ystep = ydiff/steps

            for s in range(steps):
                X = self.rint(x1+(s*xstep))
                Y = self.rint(y1+(s*ystep))
                #print((X,Y))
                #if 0 < X < self.canvas_width and 0 < Y < self.canvas_height:
                if X >= 0 and X <= self.canvas_width and Y >= 0 and Y <= self.canvas_height:
                    yield X,Y

            if w > 1:
                # width not implemented
                pass

    def math_polar(self,angle,distance):

        # 2D (x,y) deviation from origin based on an angle and distance
        # angle is in degrees from -180 to 180
        # distance is positive

        # added: fix angle to limits
        if -180 <= angle <= 180:
            pass
        else:
            angle = angle%360 - 360

        distance = abs(distance)
        #radians = math.radians(max(-180,min(180,angle)))
        radians = math.radians(angle)

        return (self.rint(math.cos(radians)*distance),
                self.rint(math.sin(radians)*distance))   

    def rint(self,n):
        return int(round(n,0))

    def randint(self,maximum):

        # the random.randint() returns the same value after start
        # this does better at returning mixed values

        return int(ord(os.urandom(1))*min(256,maximum+1)/256)

# testing below here

##    def ascii(self,points,width=128,height=64,char='X',xchar=' ',border=True):
##
##        if border:
##            print('-'*(width+2))
##
##        for y in range(height,-1,-1):
##            
##            line = ''
##
##            if border:
##                line += '|'
##
##            for x in range(width+1):
##                if (x,y) in points:
##                    line += char
##                else:
##                    line += xchar
##
##            if border:
##                line += '|'
##
##            print(line)
##
##        if border:
##            print('-'*(width+2))

##ft = FTree()
### branch(sx,sy,angle1,angle2,length1,length2,width1,width2)
####points = [c for c in ft.branch(32,0,
####                               90,0.25,
####                               8,0.75,
####                               4,0.75)]
##
##while 1:
####    points = []
####    for c in ft.tree(64,0,
####                     90,20,
####                     16,0.75,
####                     4,0.66):
####        points.append(c)
####    #    time.sleep(0.05)
##    points = [x for x in ft.rtree(64,0)]
##    ft.ascii(points,ft.canvas_width,ft.canvas_height)
##    time.sleep(1)





















