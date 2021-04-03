
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from random import randint
from kivy.core.window import Window
Window.size = (550, 500)
Window.clearcolor = (randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255, 1)
Window.title = "Test"

class WeatherApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text='Weather')
        self.input_data = TextInput(hint_text='В каком месте вы хотите узнать погоду?: ', multiline=False)
        self.output_data = Label(text='В вашем городе:')
        self.input_data.bind(text=self.GetText)


    def GetText(self, *args):
        data = self.input_data.text




        return data


    def build(self):

        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.output_data)
        box.add_widget(self.input_data)



        return box

WeatherApp().run()