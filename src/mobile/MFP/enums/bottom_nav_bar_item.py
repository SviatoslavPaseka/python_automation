from enum import Enum
from src.mobile.MFP.common.dashboard_page_base import DashboardPageBase
from src.mobile.MFP.common.diary_page_base import DiaryPageBase


class BottomNavBarItem(Enum):
    DASHBOARD = ("Dashboard", DashboardPageBase)
    DIARY = ("Diary", DiaryPageBase)
    NEWSFEED = ("newsfeed", None)
    PLANS = ("plans", None)
    MORE = ("more", None)

    def get_button_name(self):
        return self.value[0]

    def get_base_class(self):
        return self.value[1]
