from enum import Enum


class NameMealDiary(Enum):
    BREAKFAST = "Breakfast"
    LUNCH = "Lunch"
    DINNER = "Dinner"
    SNACKS = "Snacks"

    def get_diary_name(self):
        return self.value
