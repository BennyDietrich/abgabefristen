from tkinter import *
from deadline import gen_sub_list
import webbrowser

root = Tk()
root.title( "Abgabefristen - Informatik")

fach = Label(root, text="Fach:", font= ('bold'), width =20, anchor = "w")
abga = Label(root, text="Abgabe:", font= ('bold'), width =16, anchor = "w")
naeb = Label(root, text = "Neues Blatt:",font= ('bold'), width =16, anchor = "w")

fach.grid(row = 0, column = 0)
abga.grid(row = 0, column = 1)
naeb.grid(row = 0, column = 2)

def callback(url):
    webbrowser.open_new(url)

def sorter():
    sorted_list = gen_sub_list()

    fach_1 = Label(root, text=sorted_list[0].name, width =25, anchor = "w", fg="blue", cursor="hand2")
    fach_2 = Label(root, text=sorted_list[1].name, width =25, anchor = "w", fg="blue", cursor="hand2")
    fach_3 = Label(root, text=sorted_list[2].name, width =25, anchor = "w", fg="blue", cursor="hand2")
    fach_4 = Label(root, text=sorted_list[3].name, width =25, anchor = "w", fg="blue", cursor="hand2")
    fach_5 = Label(root, text=sorted_list[4].name, width =25, anchor = "w", fg="blue", cursor="hand2")

    fach_1.bind("<Button-1>", lambda e: callback(sorted_list[0].link))
    fach_2.bind("<Button-1>", lambda e: callback(sorted_list[1].link))
    fach_3.bind("<Button-1>", lambda e: callback(sorted_list[2].link))
    fach_4.bind("<Button-1>", lambda e: callback(sorted_list[3].link))
    fach_5.bind("<Button-1>", lambda e: callback(sorted_list[4].link))

    abgb_1 = Label(root, text=sorted_list[0].submit, width =20, anchor = "w")
    abgb_2 = Label(root, text=sorted_list[1].submit, width =20, anchor = "w")
    abgb_3 = Label(root, text=sorted_list[2].submit, width =20, anchor = "w")
    abgb_4 = Label(root, text=sorted_list[3].submit, width =20, anchor = "w")
    abgb_5 = Label(root, text=sorted_list[4].submit, width =20, anchor = "w")

    naeb_1 = Label(root, text=sorted_list[0].next_paper, width =20, anchor = "w")
    naeb_2 = Label(root, text=sorted_list[1].next_paper, width =20, anchor = "w")
    naeb_3 = Label(root, text=sorted_list[2].next_paper, width =20, anchor = "w")
    naeb_4 = Label(root, text=sorted_list[3].next_paper, width =20, anchor = "w")
    naeb_5 = Label(root, text=sorted_list[4].next_paper, width =20, anchor = "w")


    fach_1.grid(row = 1, column = 0)
    fach_2.grid(row = 2, column = 0)
    fach_3.grid(row = 3, column = 0)
    fach_4.grid(row = 4, column = 0)
    fach_5.grid(row = 5, column = 0)

    abgb_1.grid(row = 1, column = 1)
    abgb_2.grid(row = 2, column = 1)
    abgb_3.grid(row = 3, column = 1)
    abgb_4.grid(row = 4, column = 1)
    abgb_5.grid(row = 5, column = 1)

    naeb_1.grid(row = 1, column = 2)
    naeb_2.grid(row = 2, column = 2)
    naeb_3.grid(row = 3, column = 2)
    naeb_4.grid(row = 4, column = 2)
    naeb_5.grid(row = 5, column = 2)

    root.after(10000, sorter)

sorter()



root.mainloop()
