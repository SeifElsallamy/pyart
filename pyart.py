#from Tkinter import *
from random import randint 
from PIL import Image, ImageDraw
import datetime

basename = "img"
suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
filename = "_".join([basename, suffix])+".jpg" # e.g. 'mylogfile_120508_171442'

height_input=500
width_input=500
image = Image.new("RGB", (width_input, height_input), "white")
draw = ImageDraw.Draw(image)
colors = []
colorsY = []

def randfact():
    randlist = [0,1,5,10,50,100,500,1000,5000,10000]
    return randlist[randint(0,len(randlist)-1)]

def randfact2():
    return randint(0,2)

def randfact3():
    n = randint(0,20)
    if n == 0:
        return randint(1,500)
    elif n == 1:
        return randint(1,20)
    else:
        return 1

    
def color(rand1 , rand2):
    global colors
    n = randint(0,rand1)
    p = randint(0,rand2)
    if ((len(colors)) and  (n != 1)) :
        c = colors[randint(0,len(colors)-1)]
    else:
        r = lambda: randint(0,255)
        c = ('#%02X%02X%02X' % (r(),r(),r()))
        
        colors.append(c)

        if p != 0 and len(colors):
            colors.pop(randint(0,len(colors)-1))
    return c

points = []
# The higher N the higher relations
# The higher P the higher spread

def point(l,w, rand1 , rand2, rand3 , rand4, rand5):
    global points
    n = randint(0,rand1)
    p = randint(0,rand2)
    if len(points) and n != 0:
        point = points[randint(0 ,len(points)-1)]
        x1 = point[0]
        y1 = point[1]
    
    else:
        x1 = randint(0,l)
        y1 = randint(0,w)

    n = randint(0,rand3)

    if n == 0:
        x2 = x1

    elif n == 1:
        x2 = x1 - randint(0,rand5)

    else:
        x2 = x1 + randint(0,rand5)

    n = randint(0,rand4)
    
    if n == 0:
        y2 = y1

    elif n == 1:
        y2 = y1 - randint(0,rand5)

    else:
        y2 = y1 + randint(0,rand5)
    point = [x1,y1,x2,y2]
    points.append([x2,y2,x1,y1])
    if len(points) and p != 0:
        points.pop(randint(0,len(points)-1))

    return point 
    
    

#master = Tk()
#master.title("Points")
#w = Canvas(master,width=width_input,height=height_input)
#w.configure(background="white")
#w.pack(expand=YES, fill=BOTH)

for wtvr in range(randint(1,3)):
    n=randint(0,3)
    if n:
        colors=[]
        points=[]
    randc1=randfact()
    randc2=randfact()
    rand1=randfact()
    rand2=randfact()
    rand3=randfact2()
    rand4=randfact2()
    rand5=randfact3()
    rand6=randfact3()
    rand7=randfact3()
    rand8=randfact3()

    nn = randint(0,20) 
    if nn == 0:
        for ii in range(width_input):
            for i in range(width_input):
                x1, y1 = i, ii
                x2, y2 = i+1, ii
                #w.create_line(x1, y1, x2, y2, fill=color(randc1,randc2))
                draw.line((x1, y1, x2, y2), fill=color(randc1,randc2))
        

    elif nn == 1:
        if n == 0:
            for ii in range(width_input):
                for i in range(width_input):
                    x1, y1 = ii, i
                    x2, y2 = ii, i+1
                    #w.create_line(x1, y1, x2, y2, fill=color(randc1,randc2))
                    draw.line((x1, y1, x2, y2), fill=color(randc1,randc2))
                    
    elif nn == 2:
        if n == 0:
            for ii in range(width_input):
                for i in range(width_input):
                    if i == 250:
                        x1, y1 = i+1, ii
                        x2, y2 = ii, i+1
                        #w.create_line(x1, y1, x2, y2, fill=color(randc1,randc2))
                        draw.line((x1, y1, x2, y2), fill=color(randc1,randc2))
                    else:
                        x1, y1 = i-1, ii
                        x2, y2 = ii, i-1
                        #w.create_line(x1, y1, x2, y2, fill=color(randc1,randc2))
                        draw.line((x1, y1, x2, y2), fill=color(randc1,randc2))


    else:
        u = randint(0,15)
        for i in range(100000):
            p=point(width_input,width_input, rand1 , rand2, rand3, rand4, rand5)
            x1, y1 = p[0], p[1]
            x2, y2 = p[2], p[3]
            
            if u == 0:
                #w.create_oval(x1, y1, x2, y2, fill=color(randc1,randc2), outline=color(randc1,randc2))
                draw.ellipse((x1, y1, x2, y2), fill=color(randc1), outline=color(randc2))
            elif u == 1:
                #w.create_oval(x1, y1, x2, y2, outline=color(randc1,randc2))
                draw.ellipse((x1, y1, x2, y2), outline=color(randc1,randc2))
            elif u == 2:
                #w.create_rectangle(x1, y1, x2, y2, fill=color(randc1,randc2), outline=color(randc1,randc2))
                draw.rectangle((x1, y1, x2, y2), fill=color(randc1, randc2), outline=color(randc1,randc2))
            elif u == 3:
                #w.create_rectangle(x1, y1, x2, y2, outline=color(randc1,randc2))
                draw.rectangle((x1, y1, x2, y2), outline=color(randc1,randc2))
            else:
                #w.create_line(x1, y1, x2, y2, fill=color(randc1,randc2))
                draw.line((x1, y1, x2, y2), fill=color(randc1,randc2))
print "Image saved as "+filename
image.show()
image.save(filename)


#mainloop()

#master.mainloop()

#w.update()
#w.postscript(file="file_name.ps", colormode='color')

#master.mainloop()


