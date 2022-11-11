"""

created by Ibrahim Elsheikh
at 6:19 in 5/4/2022


"""

from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from datetime import datetime

FONT_DOWNSCALE = 0.0007
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700

INTERVAL = 500  # 1000 msec


def circle(r, R, G, B):
    glColor3d(R, G, B)  # set my color, 3=RGB d=double(0.0>1.0)
    glBegin(GL_POLYGON)  # connect them as lines and close the loop
    resolution = 1

    for ang in range(0, 360, resolution):
        x = r * cos(ang * pi / 180)  # pi / 180 from angle to rad
        y = r * sin(ang * pi / 180)  # pi / 180 from angle to rad
        glVertex2d(x, y)
    glEnd()
    # glutSwapBuffers()


def clock_line(r1, r2, angle):
    # angle is angle between two lines // should be integer

    glLineWidth(1)

    for ang in range(0, 360, angle):
        x1 = r1 * cos(ang * pi / 180)
        y1 = r1 * sin(ang * pi / 180)
        x2 = r2 * cos(ang * pi / 180)
        y2 = r2 * sin(ang * pi / 180)
        glColor3d(.73, .76, .95)
        glBegin(GL_LINES)
        glVertex2d(x1, y1)
        glVertex2d(x2, y2)
        glEnd()
        # glutSwapBuffers()


def pointer():
    now = datetime.now()
    current_time_hour = int(now.strftime("%H"))

    if current_time_hour >= 12:
        current_time_hour = current_time_hour - 12

    current_time_min = now.strftime("%M")
    current_time_sec = now.strftime("%S")

    ang_sec = -int(current_time_sec) * 6
    ang_min = -int(current_time_min) * 6
    ang_hour = -int(current_time_hour) * 30

    ##############################################
    # sec poniter
    ##############################################
    glLoadIdentity()
    glLineWidth(1)
    glColor3d(.37, .49, .85)
    glRotatef(ang_sec, 0, 0, 1)
    glBegin(GL_LINES)
    glVertex2d(0, 0)  # 2 = coordL , d = float point NOT DIMENSION
    glVertex2d(0, 0.85)
    glEnd()

    ###############################################
    # min Pointer
    ###############################################

    glLoadIdentity()
    glLineWidth(5)
    glColor3d(.95, .68, .16)
    glRotate(ang_min, 0, 0, 1)
    glBegin(GL_LINES)
    glVertex2d(0, 0)  # 2 = coord   L , d = float point NOT DIMENSION
    glVertex2d(0, .75)
    glEnd()

    ###############################################
    # hour Pointer
    ###############################################
    glLoadIdentity()
    glLineWidth(8)
    glColor3d(.75, .42, .25)
    glRotate(ang_hour, 0, 0, 1)
    glBegin(GL_LINES)
    glVertex2d(0, 0)  # 2 = coordL , d = float point NOT DIMENSION
    glVertex2d(0, 0.80)

    glEnd()
    glutSwapBuffers()


def draw_text(string, x, y):
    glLineWidth(1)
    glColor(1, 1, 1)
    glPushMatrix()
    glTranslate(x - .03, y - 0.03, 0)
    glScale(FONT_DOWNSCALE, FONT_DOWNSCALE,
            1)  # when writing text and see nothing downscale it to a very small value .001 and draw at center
    string = string.encode()  # conversion from Unicode string to byte string
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)
    glPopMatrix()


def initGL():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)

    glOrtho(-1, 1, -1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, 0, 0, 0, 0, -1, 0, 1, 0)


def draw():
    initGL()
    glClearColor(0.0, 0.0, 0.0, 1)

    circle(.98, 0.37, 0.56, 0.85)  # No REvision need
    circle(.95, 0, 0, 0)  # No Need  REvision need
    r4 = 0.83
    for ang in range(450, 90, -30):
        x = r4 * cos(ang * pi / 180)
        y = r4 * sin(ang * pi / 180)
        draw_text(str(int(ang / 30 - 3)), -x, y)

    clock_line(0.93, 0.86, 30)

    clock_line(0.93, 0.90, 6)
    clock_line(0.93, 0.92, 1)

    pointer()


def clock_timer(v):
    draw()
    glutTimerFunc(INTERVAL, clock_timer, 1)
    print("Hello HRU")


def mainfunc():
    glutInit()
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)  # Set the window's initial width & height #
    glutInitWindowPosition(300, 50)  # position
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"Wall clock")
    initGL()
    glutDisplayFunc(draw)
    glutTimerFunc(INTERVAL, clock_timer, 1)
    glutMainLoop()


mainfunc()

print(" Hi Every one ")
