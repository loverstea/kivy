from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime

from kivymd.uix.list import ILeftBodyTouch, TwoLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox

class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    ...
class TaskItem(TwoLineAvatarIconListItem):
    ...
class TaskListScreen(Screen):
    ...


class NewTaskScreen(Screen):
    def back(self):
        self.manager.current = "main_screen"
        self.manager.transition.direction = "down"
        self.manager.transition.duration = 0.6
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()
    def on_save(self, instance, value, date_range):
        date = value.strftime('%d/%m/%Y')
        self.ids.date_text.text = str(date)
    
class ToDoApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        Builder.load_file('graf.kv')

        self.screen = TaskListScreen(name="main_screen")
        sm = ScreenManager()
        sm.add_widget(self.screen)
        sm.add_widget(NewTaskScreen(name="second_screen"))
        return sm
    def add_task(self):
        new_task = TaskItem(text= text ,secondary_text=date )
        self.screen.ids.task_list.add_widget(new_task)
        self.screen.manager.transition.duration = 0.6
        self.screen.manager.transition.direction = "down"
        self.screen.manager.current = "main_screen"
        

app = ToDoApp()
app.run()
