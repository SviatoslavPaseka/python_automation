from enum import Enum


class NutrientQuickAdd(Enum):
    FAT = ("fat", "Fat")
    CARBS = ("carbs", "Carbs")
    PROTEIN = ("protein", "Protein")

    def get_value(self):
        return self.value[0]

    def get_name_in_DOM_id(self):
        return self.value[1]
