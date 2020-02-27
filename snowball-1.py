from graphics import *

#Describes the graphic window
win = GraphWin("Snowball", 400, 400)
win.setBackground('#4da6ff')   # setting the sky color using html hex string

# describe the mountain background
moutain1 = Polygon(Point(0, 399), Point(210, 50), Point(399, 399))
moutain1.setFill('#e6f3ff')
moutain1.setOutline('#a6a6a6')
moutain1.setWidth(2)
moutain1.draw(win)

moutain2 = Polygon(Point(0, 399), Point(0, 100), Point(270, 399))
moutain2.setFill('#e6f3ff')
moutain2.setOutline('#a6a6a6')
moutain2.setWidth(2)
moutain2.draw(win)

#describes the sun
sun = Circle(Point(399, 20), 40)
sun.setFill('yellow')
sun.setOutline('yellow')
sun.setWidth(4)
sun.draw(win)

# describe the trees
trunk1 = Rectangle(Point(143, 180), Point(157, 200))
trunk1.setFill('sienna')
trunk1.setWidth(0)
trunk1.draw(win)

foliage1a = Polygon(Point(130, 180), Point(170, 180), Point(150, 160))
foliage1a.setFill('green')
foliage1a.setOutline('green')
foliage1a.setWidth(2)
foliage1a.draw(win)

foliage1b = foliage1a.clone()
foliage1b.move(0, -15)
foliage1b.draw(win)

foliage1c = foliage1a.clone()
foliage1c.move(0, -30)
foliage1c.draw(win)

trunk2 = trunk1.clone()
trunk2.move (100, 50)
trunk2.draw(win)

foliage2a = Polygon(Point(230, 230), Point(270, 230), Point(250, 210))
foliage2a.setFill('green')
foliage2a.setOutline('green')
foliage2a.setWidth(2)
foliage2a.draw(win)

foliage2b = foliage2a.clone()
foliage2b.move(0, -15)
foliage2b.draw(win)

foliage2c = foliage2a.clone()
foliage2c.move(0, -30)
foliage2c.draw(win)

trunk3 = trunk1.clone()
trunk3.move (165, 150)
trunk3.draw(win)

foliage3a = Polygon(Point(295, 330), Point(335, 330), Point(315, 310))
foliage3a.setFill('green')
foliage3a.setOutline('green')
foliage3a.setWidth(2)
foliage3a.draw(win)

foliage3b = foliage3a.clone()
foliage3b.move(0, -15)
foliage3b.draw(win)

foliage3c = foliage3a.clone()
foliage3c.move(0, -30)
foliage3c.draw(win)

trunk4 = trunk1.clone()
trunk4.move (-110, 80)
trunk4.draw(win)

foliage4a = Polygon(Point(20, 260), Point(60, 260), Point(40, 240))
foliage4a.setFill('green')
foliage4a.setOutline('green')
foliage4a.setWidth(2)
foliage4a.draw(win)

foliage4b = foliage4a.clone()
foliage4b.move(0, -15)
foliage4b.draw(win)

foliage4c = foliage4a.clone()
foliage4c.move(0, -30)
foliage4c.draw(win)

trunk5 = trunk1.clone()
trunk5.move (-30, 160)
trunk5.draw(win)

foliage4a = Polygon(Point(100, 340), Point(140, 340), Point(120, 320))
foliage4a.setFill('green')
foliage4a.setOutline('green')
foliage4a.setWidth(2)
foliage4a.draw(win)

foliage4b = foliage4a.clone()
foliage4b.move(0, -15)
foliage4b.draw(win)

foliage4c = foliage4a.clone()
foliage4c.move(0, -30)
foliage4c.draw(win)

#snowball getting bigger using time.sleep 
snowball1 = Circle(Point(10, 99), 20)
snowball1.setFill('white')
snowball1.draw(win)
time.sleep(1)
snowball1.undraw()

snowball2 = Circle(Point(50, 139), 23)
snowball2.setFill('white')
snowball2.draw(win)
time.sleep(1)
snowball2.undraw()

snowball3 = Circle(Point(90, 179), 26)
snowball3.setFill('white')
snowball3.draw(win)
time.sleep(1)
snowball3.undraw()

snowball4 = Circle(Point(130, 219), 29)
snowball4.setFill('white')
snowball4.draw(win)
time.sleep(1)
snowball4.undraw()

snowball5 = Circle(Point(170, 259), 32)
snowball5.setFill('white')
snowball5.draw(win)
time.sleep(1)
snowball5.undraw()

snowball6 = Circle(Point(210, 299), 35)
snowball6.setFill('white')
snowball6.draw(win)
time.sleep(1)
snowball6.undraw()

snowball7 = Circle(Point(250, 339), 38)
snowball7.setFill('white')
snowball7.draw(win)
time.sleep(1)
snowball7.undraw()

snowball8 = Circle(Point(290, 379), 41)
snowball8.setFill('white')
snowball8.draw(win)
time.sleep(1)
snowball8.undraw()

snowball9 = Circle(Point(330, 419), 44)
snowball9.setFill('white')
snowball9.draw(win)
time.sleep(1)
snowball9.undraw()


win.getMouse()