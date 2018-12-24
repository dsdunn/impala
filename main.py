from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '480')

from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button



class Control(BoxLayout):
  def logId(self, str):
    print str

class ImpalaApp(App): 
  def build(self):
    return Control()

if __name__ == '__main__':
  ImpalaApp().run()