from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk
import pygame
from pygame.locals import  *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("music.wav")
pygame.mixer.music.play(-1)

def showList():
    myText = "Drogi Swiety Mikolaju,\nTo ja, Polski Elon Musk ktory mieszka w Francji (Wedlug widzow Synapse).\n W tym roku bylem grzeczny :tf:, poznalem duzo wspanialych przyjaciol (Paste example here : ).\nOgolnie mowiac, jestem bardzo mila i emocjonalnie stabilnie osoba ktora dba i troszczy sie o swoich przyjaciol\nRozprzestrzeniam moja pozytywna energie poprzez discorda ale i rowniez moj kanal na twitchu.\nMam nadzieje ze i Tobie w tym roku sie powodzilo. \nNa koniec, chcialbym ci zyczyc powodzenia z dostarczeniem prezentow to wszystkich grzecznych dzieci.\nKoloMenek"
    newWindow = Toplevel(window, width=800,height=400)
    Label(newWindow,text=myText).pack(padx=5, pady=5)

def zapytaniePrezenty():
    myText = "Komputer do grania w ligunie :"
    myText2 = "Albo\nMieszkanie w centrum Paryza z widokiem na wieze Eiffle :"
    myText3 = "Albo jednak gdyby te prezenty bylyby odrobinke za drogie, bardzo ucieszy mnie :\nRanga Grzeczny Przedszkolak na serwerze discord mojej ulubionej streamerki UwU"
    if askyesno("Lista prezentow","Czy chcesz zobaczyc liste prezentow ?"):
        newWindow = Toplevel(window, width=800,height=400)
        Label(newWindow,text=myText).pack(padx=5, pady=5)
        var = StringVar()
        var2 = StringVar()
        var.set("https://www.x-kom.pl/lista/m3n9t9gqu")
        Entry(newWindow,textvariable=var, state="readonly",width=50, readonlybackground="white", fg="black").pack()
        Label(newWindow,text=myText2).pack(padx=5, pady=5)
        var2.set("https://proprietes.lefigaro.fr/annonces/appartement-paris-ile+de+france-france/31595037/")
        Entry(newWindow,textvariable=var2, state="readonly",width=50, readonlybackground="white", fg="black").pack()
        Label(newWindow,text=myText3).pack(padx=5, pady=5)
    else:
        showerror("Lista prezentow","Jak to ? :( ")
        showerror("Lista prezentow","Sadge :'( ")
        showerror("Lista prezentow","A moze jeszcze raz zapytam")
        zapytaniePrezenty()

def pauseUnpause():
    isOn = pygame.mixer.music.get_busy()
    if isOn:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

window = Tk()
window.title("List do mikolaja - KoloMenek")
window.resizable(width=False, height=False)
canvas = Canvas(window, width=800, height=400, bg='ivory')
img = (Image.open("art.png"))
resized = img.resize((800, 400), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized)
canvas.create_image(0,0, anchor=NW, image=new_image)
canvas.pack(side=LEFT, padx=5, pady=5)
Button(window, text='Zobacz list', command=showList).pack(side=TOP, padx=5, pady=5)
Button(text='Lista prezentow', command=zapytaniePrezenty).pack(side=TOP, padx=5, pady=5)
Button(window, text='Wlacz / Wylacz muzyke', command=pauseUnpause).pack(side=TOP, padx=5, pady=5)
window.mainloop()
