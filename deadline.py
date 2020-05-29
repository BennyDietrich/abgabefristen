import calendar
from datetime import date
from Subject import *


def gen_sub_list():
    """ Basicly the main function of deadline. Run this function to get a list
        of Subject objects for all the subjects in custom_subjects.txt.
    """
    day = date.today().weekday()
    sub_week = read_sub_file()
    counter = 7
    return_list = []
    while counter > 0:
        for subject in sub_week[day]:
            return_list.append(subject)
        if day == 6:
            day = 0
        else:
            day += 1
        counter -= 1
    return return_list


def read_sub_file():
    """Reads the custom_subjects.txt and generates a list of Subject objects of
       all subjects mentioned in the file.
    """
    sub_week = [[], # Monday
                [], # Tuesday
                [], # Wednesday
                [], # Thursday
                [], # Friday
                [], # Saturday
                []] # Sunday
    with open("custom_subjects.txt") as file:
        lines = file.readlines()
    day = 0
    for line in lines:
        if line[0].isdigit():
            day = int(line[0])
        elif line[0] == '$':
            line_array = (line.replace("$","")
                          .replace("<", "")
                          .replace(">", "")
                          .split("_"))
            sub_week[day].append(Subject(line_array[0], # name
                                         day_diff(day), # submit
                                         line_array[1], # time
                                         day_diff(int(line_array[2])), # next_paper
                                         line_array[3])) # link
    return sub_week


def day_diff(day: int):
    """Computes the difference (in days) between a given day (0-6 -> Mon-Sun)
       and the currente day and provides a informative string.
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
