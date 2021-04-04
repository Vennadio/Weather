
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from random import randint
from kivy.core.window import Window


Window.size = (1000, 1000)
Window.clearcolor = (10/255, 201/255, 1/255,1)
Window.title = "Weather_Now"

class WeatherApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text='Weather', font_size=24)
        self.input_data = TextInput(hint_text='В каком месте вы хотите узнать погоду?: ', multiline=False, font_size=24)
        self.output_data = Label(text='В вашем городе:', font_size=24)
        self.input_data.bind(text=self.GetText)

    def update_label(self, instance):
        self.lbl.text = str(instance.text)

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


