import calendar
from datetime import date 
from Fach import *

def day_name(d):
    return {
        0 : "Montag",
        1 : "Dienstag",
        2 : "Mittwoch",
        3 : "Donnerstag",
        4 : "Freitag",
        5 : "Samstag",
        6 : "Sonntag"
    }[d]

def table_printer(d):
    if d == 0:
        temp_fach = Fach("Programmieren in C++", day_calc(1), day_calc(1),
         "https://ad-wiki.informatik.uni-freiburg.de/teaching/ProgrammierenCplusplusSS2020", "12:00")
    elif d == 1:
        temp_fach = Fach("Algo und Data", day_calc(2,), day_calc(0),
        "http://ac.informatik.uni-freiburg.de/teaching/ss_20/ad-lecture.php", "16:00")
    elif d == 2:
        temp_fach = Fach("Technische Informatik", day_calc(4), day_calc(4), 
        "https://ira.informatik.uni-freiburg.de/src/teach_main.php?id=223", "17:00")
    elif d == 3:
        temp_fach = Fach("Mathe II", day_calc(5), day_calc(4),
        "https://ilias.uni-freiburg.de/ilias.php?ref_id=1531150&cmdClass=ilrepositorygui&cmdNode=ye&baseClass=ilrepositorygui", "23:00")
    else:
        print("ERROR")
    return temp_fach

def day_calc(d): 
    t = date.today().weekday()
    dayname = day_name(d)
    if d - t == 0:
        return "Heute"
    elif d - t == 1:
        return "Morgen"
    elif d > t:
        return "{} in {} Tagen".format(dayname, str(d-t))
    else:
        return  "{} in {} Tagen".format(dayname, str(7-t+d))   

def next_calc():
    print("\n")
    start = 0
    t = date.today().weekday()
    if t > 5:
        start = 0
    elif t > 4:
        start = 3
    elif t > 2:
        start = 2
    else:
        start = 1
    counter = 4
    temp_list = []
    while counter > 0:
        temp_list.append(table_printer(start))
        if start == 3:
            start = 0
        else:
             start += 1
        counter -= 1
    return temp_list
