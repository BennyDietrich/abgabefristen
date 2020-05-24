from datetime import *

class Fach:

    def __init__ (self, name: str, ab: str, nb: str, link: str, uhr: str):
        self.__name = name
        self.__ab = ab
        self.__nb = nb
        self.__link = link
        self.__uhr = uhr           
        self.refresh()

    def refresh(self):
        if self.__ab == "Heute":
            now = datetime.now()
            hour = int(self.__uhr[:2]) - now.hour
            minute = int(self.__uhr[3:]) - now.minute
            if minute < 0:
                minute += 60
                hour -= 1
            if minute < 10:
                minute = "0" + str(minute)
            if hour < 0:
                self.__ab = "Beendet"
            if hour < 10:
                hour = "0" + str(hour)
            if self.__ab != "Beendet":
                self.__ab = "Noch: {}:{} (h:m)".format(hour, minute)
        elif self.__ab == "Morgen":
             self.__ab = "Morgen: {} Uhr".format(self.__uhr)

    @property
    def name(self):
        return self.__name
    
    @property
    def ab(self):
        return self.__ab
   
    @ab.setter
    def ab(self, val):
        self.__ab = val

    @property
    def nb(self):
        return self.__nb
    
    @property
    def link(self):
        return self.__link

    @property
    def uhr(self):
        return self.__uhr
