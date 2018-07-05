import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.properties import ListProperty

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Yo Name, boy.'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='passwheeeerd?'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        timer = Timer(text='time off baby')
        timer_button = TimerButton()
        timer_button.bind(pressed=timer.start_timer)
        self.add_widget(timer_button)
        self.add_widget(timer)
        self.ev = TimerDispatcher()
        self.ev.bind(on_timer_button=timer.start_timer)


class Timer(Label):
    def __init__(self, **kwargs):
        super(Label, self).__init__(**kwargs)

    def start_timer(self, value, *args):
        print('how did you get here?', value)


class TimerButton(Widget):
    pressed = ListProperty([0,0])


    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            return True
        return super(TimerButton, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        print('pressed at {pos}'.format(pos=pos))



class TimerDispatcher(EventDispatcher):
    def __init__(self, **kwargs):
        self.register_event_type('on_timer_button')
        super(TimerDispatcher, self).__init__(**kwargs)

    def start_timer(self, value):
        self.dispatch('on_timer_button', value)

    def on_timer_button(self, *args):
        print('On timer button, button, button')



class MyApp(App):


    def my_callback(dt):
        print('My callback is called !')

    Clock.schedule_once(my_callback, 1)

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()