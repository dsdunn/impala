from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')

from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.clock import Clock 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image 


class ButtonImage(Image):

  def build(self, source):
    self.source = source


class Control(BoxLayout):

  def log_control(self, str):
    print str

  def start_window(self, window):
    # turn gpio pin on mock implementation:
    self.event = Clock.schedule_interval(lambda dt: self.log_control(window), 0.1)

  def stop_window(self):
    Clock.unschedule(self.event)



class ImpalaApp(App): 
  def build(self):
    return Control()

if __name__ == '__main__':
  ImpalaApp().run()