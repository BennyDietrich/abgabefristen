import calendar
from datetime import date
from Subject import *

def day_name(day: int):
    return {
        0 : "Montag",
        1 : "Dienstag",
        2 : "Mittwoch",
        3 : "Donnerstag",
        4 : "Freitag",
        5 : "Samstag",
        6 : "Sonntag"
    }[day]

def next_subject(day: int):
    """For a value d (0 - 3) the function creates a Subject object and
       returns it.
    """
    if day == 0:
        temp_subject = Subject("Programmieren in C++", day_diff(1), day_diff(1),
         "https://ad-wiki.informatik.uni-freiburg.de/teaching/ProgrammierenCplusplusSS2020",
         "12:00")
    elif day == 1:
        temp_subject = Subject("Algo und Data", day_diff(2), day_diff(0),
        "http://ac.informatik.uni-freiburg.de/teaching/ss_20/ad-lecture.php",
        "16:00")
    elif day == 2:
        temp_subject = Subject("Technische Informatik", day_diff(4), day_diff(4),
        "https://ira.informatik.uni-freiburg.de/src/teach_main.php?id=223",
        "17:00")
    elif day == 3:
        temp_subject = Subject("Mathe II", day_diff(5), day_diff(4),
        "https://ilias.uni-freiburg.de/ilias.php?ref_id=1531150&cmdClass=ilrepositorygui&cmdNode=ye&baseClass=ilrepositorygui",
        "23:00")
    else:
        print("ERROR")
    return temp_subject

def day_diff(day: int):
    """Computes the difference (in days) between a given day (0-6 -> Mo-So)
       and the currente day.
       Example: Today is Friday(4) and we want to know how many
                days are left till next Monday(0).
                today = 4
                day = 0
                day < today -> (7-today + day) = 3
    """
    today = date.today().weekday()
    dayname = day_name(day)
    if day - today == 0:
        return "Heute"
    elif day - today == 1:
        return "Morgen"
    elif day > today:
        return "{} in {} Tagen".format(dayname, str(day-today))
    else:
        return  "{} in {} Tagen".format(dayname, str(7-today+day))

def sub_list():
    """Computes which is the first subject in the list by comparing today
       with the possible subject dates and then sets a starting point.
       After finding the first subject the while loop generates a list
       of Subject objects in the needed order and returns the list.
    """
    today = date.today().weekday()
    if today > 5:
        start = 0
    elif today > 4:
        start = 3
    elif today > 2:
        start = 2
    else:
        start = 1
    counter = 4
    temp_list = []
    while counter > 0:
        temp_list.append(next_subject(start))
        if start == 3:
            start = 0
        else:
             start += 1
        counter -= 1
    return temp_list

def refresh(sub_list: list):
    for i in sub_list:
        i.refresh()
    return
