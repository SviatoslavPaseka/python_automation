from enum import Enum


class ButtonsInMoreMenu(Enum):
    QUICK_ADD = ("quick_add", "Quick Add")
    REMINDERS = ("reminders", "Reminders")

    def get_button_id(self):
        return self.value[0]

    def get_name_of_button(self):
        return self.value[1]
    