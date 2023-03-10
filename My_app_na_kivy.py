from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.pickers import MDDatePicker
from datetime import datetime
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

from kivymd.uix.list import ILeftBodyTouch, TwoLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox

from kivy.storage.jsonstore import JsonStore
from random import randint

from kivy.utils import platform

if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    ...
class TaskItem(TwoLineAvatarIconListItem):
    def __init__(self, key, **kwargs):
        super().__init__(**kwargs)
        self.key = key
    def delete_task(self, the_task_item):
        self.parent.remove_widget(the_task_item)
        app.db.delete(self.key)
    def chek_task(self, check, list_item):
        if check.active == True:
            app.db.put(self.key,task = self.text, date=self.secondary_text, done=True)
        else:
            app.db.put(self.key,task = self.text, date=self.secondary_text, done=False)

class TaskListScreen(Screen):
    ...


class NewTaskScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = str(datetime.now().strftime('%d/%m/%Y'))
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
        self.read_tasks()
        return sm
        
    def read_tasks(self):
        '''Read tasks from JSON file'''
        self.db = JsonStore("DB.json")
        #self.db.put(1, task="??????????????", date="11/2/2023", done = False)
        self.tasks = []
        self.keys = self.db.keys()
        for i in self.keys:
            if self.db.exists(i):
                self.tasks.append(self.db.get(i))
                new_task = TaskItem(key = i, text=self.tasks[-1]['task'], secondary_text=self.tasks[-1]['date'])
                if self.tasks[-1]['done'] == True:
                    new_task.ids.check.active = True
                self.screen.ids.task_list.add_widget(new_task)
    
    def add_task(self, text, date):
        if text != "":
            new_key = randint(0,10000)
            while self.db.exists(new_key):
                new_key = randint(0,10000)

            new_task = TaskItem(key = new_key, text=text , secondary_text=date)
            self.screen.ids.task_list.add_widget(new_task)
            self.db.put(new_key,task = text, date=date, done=False)
            self.screen.manager.transition.direction = "down"
            self.screen.manager.transition.duration = 0.7
            self.screen.manager.current = "main_screen"
        else:
            self.dialog = MDDialog(
            text="???????????????? ?????????????? ???????????????? ????????????!!!",
            buttons=[
                 MDRaisedButton(text="??????????????????",  on_release=lambda _: self.dialog.dismiss())
                ],
            )
            self.dialog.open()

app = ToDoApp()
app.run()

