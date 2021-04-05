
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout


Window.size = (1000, 1000)
Window.clearcolor = (10/255, 201/255, 1/255,1)
Window.title = "Weather_Now"

#class Info_Page(Widget):
   # def choose(self):
        # self.input_data.bind(text=self.GetText)
        # box.add_widget(self.input_data)
        #self.output_data = Label(text='В вашем городе:', font_size=24)
    #def GetText(self, *args):
    #data = self.input_data.text

    #return data






class WeatherApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text='Weather', font_size=50)
        self.input_data = TextInput(hint_text='В каком месте Вы хотите узнать погоду?: ', multiline=False, font_size=24)
        self.output_data = Label(text='В Вашем городе:', font_size=24)
        #self.input_data.bind(text=self.GetText)
        self.button = button = Button(text='Hello world', font_size=24, on_press = self.callback, background_color = [0,1,1,1])
            #Button(text="Выберите Ваш город", font_size=24, on_press = self.btn_press())
    #function of calling button
    def callback(self, instance):
        instance.text = ('Hello')




    def build(self):

        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.output_data)
        box.add_widget(self.button)
        #position of button
        #fl = FloatLayout(size = (100, 100))
        #fl.add_widget(Button(text='Hello world', font_size=24, on_press = self.callback, background_color = [0,1,1,1],
                             #size_hint = (.10,.50), pos = (10, 10)))
        #return fl




        return box

#Info_Page().choose()
WeatherApp().run()


