from kivy.app import App
from kivy.uix.widget import Widget
import os
import sys
import _ctypes
import ctypes



#from jnius import autoclass
#Context = autoclass('android.content.Context')
#Activity = autoclass('android.app.Activity')
#activity = autoclass('org.renpy.android.PythonActivity')
#appinfo =  Activity.getApplicationInfo()
#print appinfo
#print appinfo.dataDir
#print activity.getApplicationInfo().dataDir

#I/python  (20115): posix
#I/python  (20115): linux3
#I/python  (20115): armv7l-64


print '#####################'
print os.name
print sys.platform
print os.uname()[4] + '-64'

import freetype


from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(), random(), random())
        with self.canvas:
            Color(*color)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class TestImportsApp(App):

    def build(self):
        return MyPaintWidget()


#if __name__ == '__main__':
TestImportsApp().run()
