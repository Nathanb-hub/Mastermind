from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
import random


colors = ['Red','Blue','Yellow','Green','White','Black']
firstDot = Spinner(text='Choose color', values=colors,size_hint=(1, 1))
secondDot = Spinner(text='Choose color', values=colors,size_hint=(1, 1))
thirdDot = Spinner(text='Choose color', values=colors,size_hint=(1, 1))
lastDot = Spinner(text='Choose color', values=colors,size_hint=(1, 1))

class Main(App):
    def build(self):
        self.title= 'Mastermind'
        # les couleurs a obtenir pour gagner 
        firstColor = random.choice(colors)
        secondColor = random.choice(colors)
        thirdColor = random.choice(colors)
        lastColor = random.choice(colors)


        # pour contenir toutes les sections
        gamePage = BoxLayout(orientation='horizontal')
        #section pour donner les indices : bonne couleur au bon endroit ou juste bone couleur 
        commentSection = BoxLayout(orientation='vertical',size_hint=(0.3,1))
        indi = Label(text='Indices :',size_hint=(1,.4))
        firstInd = Label(text='Ici le premier indice',size_hint=(1,.2))
        seconInd = Label(text='Ici le deuxieme indice',size_hint=(1,.2))
        valid_btn = Button(text='Valider',size_hint=(1,.2))
        #valid.bind(on_press=checkColors)
        commentSection.add_widget(indi)
        commentSection.add_widget(firstInd)
        commentSection.add_widget(seconInd)
        commentSection.add_widget(valid_btn)
        

        # grille de jeu 
        gameSection = GridLayout(cols=4,rows=11,size_hint=(0.7,1))
        for i in range(1,41):
            btn = Button(text='',id=str(i))
            gameSection.add_widget(btn)
        gameSection.add_widget(firstDot)
        gameSection.add_widget(secondDot)
        gameSection.add_widget(thirdDot)
        gameSection.add_widget(lastDot)



        gamePage.add_widget(commentSection)
        gamePage.add_widget(gameSection)
        return gamePage
        # on ajoute toutes les sections dans la page de jeu avant de la return


        def checkColors(self):
            
            
            firstDot.text

Main().run()