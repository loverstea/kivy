from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class TaskListScreen(Screen):
    ...


class NewTaskScreen(Screen):
    ...
class Example(MDApp):
    data = {
        'Python': 'language-python',
        'PHP': 'language-php',
        'C++': 'language-cpp',
    }
class ToDoApp(MDApp):
    data = {
            'Python': 'language-python',
            'PHP': 'language-php',
            'C++': 'language-cpp',
        }

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        Builder.load_file('graf.kv')


        sm = ScreenManager()
        sm.add_widget(TaskListScreen(name="main_screen"))
        sm.add_widget(NewTaskScreen(name="second_screen"))
        return sm
app = ToDoApp()
app.run()
