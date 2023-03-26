#! /usr/bin/env python
# -*- coding: utf-8 -*-


path = "./"


from tkinter import *
import random

def main(event):
    global wordstyle, description, entry, label, old, fails, stilmittel, out

    if len(todo) > 2:
        i = entry.get()
        entry.delete(0, 'end')

        if i == wordstyle:
            request = "Richtig\n\n"
            todo.remove(wordstyle)
        elif i != wordstyle:
            fails += 1
            request = "Falsch.\n {}: {}\n".format(wordstyle,description)
            todo.append(wordstyle)


        if len(todo)-1 == 1:
            if fails == 0:
                out = "{} Noch kein Fehler\nNoch eine Wiederholung\nHighscore: {} Fehler".format(request,leastfailnumber) #\nSchnellster Durchgang: {:1.2f}s".format(leastfailnumber,start-now)
            elif fails == 1:
                out = "{}Nur ein Fehler\nNoch eine Wiederholung\nHighscore: {} Fehler".format(request,leastfailnumber) #\nSchnellster Durchgang: {:1.2f}s".format(leastfailnumber,start-now)
            else:
                out = "{}{} Fehler\nNoch eine Wiederholung\nHighscore: {} Fehler".format(request,fails,leastfailnumber) #\nSchnellster Durchgang: {:1.2f}s".format(leastfailnumber,start-now)
        else:
            if fails == 0:
                out = "{}Noch kein Fehler\nNoch {} Wiederholungen\nHighscore: {} Fehler".format(request,len(todo)-1,leastfailnumber) #\nSchnellster Durchgang: {:1.2f}s".format(leastfailnumber,start-now)
            elif fails == 1:
                out = "{}Nur ein Fehler\nNoch {} Wiederholungen\nHighscore: {} Fehler".format(request,len(todo)-1,leastfailnumber) #\nSchnellster Durchgang: {:1.2f}s".format(leastfailnumber,start-now)
            else:
                out = "{}{} Fehler\nNoch {} Wiederholungen\nHighscore: {} Fehler".format(request,fails,len(todo)-1,leastfailnumber) #\nSchnellster Durchgang: {:1.2f}s".format(leastfailnumber,start-now)

        wordstyle = todo[random.randrange(len(todo))]
        while wordstyle == old and todo.count(wordstyle) >= len(todo): #take a new wordstyle, if the same wordstyle taken twice
            wordstyle = todo[random.randrange(len(todo))]
        old = wordstyle

        description = stilmittel[wordstyle]
        descriptionlabel.configure(text = description)
        label.configure(text = out)

    else:
        out = "FERTIG"
        if fails < leastfailnumber:
            info["leastfailnumber"] = str(fails)
            out += "\n\nNeue Bestleistung: Nur {} Fehler!".format(fails)
            i = open(path+"Info.txt","w")
            i.write("#Please do not change these infos\n\n")
            for x in info.keys():
                i.write("{}={}".format(x,info[x]))
            i.close()
        label.configure(text = out)
        descriptionlabel.configure(text = "Keine Stilmittel mehr zu lernen!")
        entry.delete(0, 'end')
        screen.after(3000, screen.quit)

#building the config-list#############################################################
info = {}
i = open(path+"Info.txt","r")
for line in i:
    if line[0] != "#" and len(line) > 4:
        if "=" in line:
            line = line.split("=")
            info[line[0]] = line[1]
        else:
            print("Info couldn't load.")
i.close()
leastfailnumber = int(info["leastfailnumber"])

#building the stilmittel-dictionary####################################################
stilmittel = {}
s = open(path+"/Stilmittel.txt","r")
for line in s:
    if line[0] != "#" and len(line) > 4:
        if ":" in line:
            line = line.split(":")

            line[1] = line[1].replace("***","\n")
            stilmittel[line[0]] = line[1]
        else:
            print("Stilmittel konten nicht geladen werden.")


s.close()

#buiding the todo-list of stilmittel##################################################
todo = []
for x in stilmittel:
    todo.append(x)



#Needed variables#####################################################################
old = ""
fails = 0
out = "\n\n{} Fehler\n{} Wiederholungen\nHighscore: {} Fehler".format(fails,len(todo)-1,leastfailnumber) #\nSchnellster Durchgang: {:1.2f}s".format(leastfailnumber,start-now)


#Build the screen#####################################################################

screen = Tk()
screen.title('Stilmittel lernen')
#description
wordstyle = todo[random.randrange(len(todo))]
description = stilmittel.get(wordstyle)
descriptionlabel = Label(screen)
descriptionlabel.config(font=('Helvetica', 15))
descriptionlabel.configure(text = description)

#input
entry = Entry(screen)
entry.config(font=('Helvetica', 15))
entry.bind("<Return>", main)
entry.focus_set()

#output
label = Label(screen)
label.config(font=('Helvetica', 15))
label.configure(text = out)


descriptionlabel.pack()
entry.pack()
label.pack()

print("Programm gestartet.")
screen.mainloop()
print("Programm abgeschlossen.")
