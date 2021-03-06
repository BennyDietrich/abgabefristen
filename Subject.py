from datetime import *

class Subject:
    """Subject objects provide:
            - Name of the Subject
            - Day of submission
            - Daytime of submission
            - Day when the next paper will be published
            - Link to the main page of the subject"""
    def __init__ (self, name: str, submit: str, time: str, next_paper: str, link: str):
        self.__name = name
        self.__submit = submit
        self.__time = time
        self.__next_paper = next_paper
        self.__link = link
        self.refresh()

    def refresh(self):
        """Checks if the subject has to be submitted within the next two Days.
           If submit > 24h: 'Morgen: __time Uhr'
           IF submit < 24h: countdown in hh:mm format
        """
        if self.__submit == "Heute":
            now = datetime.now()
            hour = int(self.__time[:2]) - now.hour
            minute = int(self.__time[3:]) - now.minute
            if minute < 0:
                minute += 60
                hour -= 1
            if minute < 10:
                minute = "0" + str(minute)
            if hour < 0:
                self.__submit = "Beendet"
            if hour < 10:
                hour = "0" + str(hour)
            if self.__submit != "Beendet":
                self.__submit = "Noch: {}:{} (h:m)".format(hour, minute)
        elif self.__submit == "Morgen":
             self.__submit = "Morgen: {} Uhr".format(self.__time)

    @property
    def name(self):
        return self.__name

    @property
    def submit(self):
        return self.__submit

    @submit.setter
    def submit(self, val):
        self.__submit = val

    @property
    def next_paper(self):
        return self.__next_paper

    @property
    def link(self):
        return self.__link

    @property
    def uhr(self):
        return self.__time
