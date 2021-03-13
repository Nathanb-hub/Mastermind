from kivy.app import App
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import random

red = [1, 0, 0, 1]  
green = [0, 1, 0, 1]  
blue = [0, 0, 1, 1]  
purple = [1, 0, 1, 1]  
yellow = [1,1,0,1]
white = [1,1,1,1]
black = [0,0,0,0]

colors = ['Red','Blue','Yellow','Green','White','Black']
firstDot = Spinner(text='Choose color', values=colors,size_hint=(1, 1))
secondDot = Spinner(text='Choose color', values=colors,size_hint=(1, 1))
thirdDot = Spinner(text='Choose color', values=colors,size_hint=(1, 1))
lastDot = Spinner(text='Choose color', values=colors,size_hint=(1, 1))

sm = ScreenManager()


class Main(App):
    def getInfos(self,instance):
        inputs = [firstDot.text,secondDot.text,thirdDot.text,lastDot.text]
        for i in range(len(inputs)):
            # section to give informations to player
            if (inputs[i]  == self.winningCombination[i]): # right color at the right place
                self.infoButtons[i].background_color=[0,1,0,1]
            elif(inputs[i]  in self.winningCombination and self.winningCombination[i] != inputs[i]):#right color at the wrong place
                self.infoButtons[i].background_color= yellow 
            elif(inputs[i] not in self.winningCombination): #wrong color
                self.infoButtons[i].background_color= [1,0,0,1]
        self.adjustGridColors()
            # if current_color=='Red':
            #     current_color = [1,0,0,1]
            # elif current_color=='Blue':
            #     current_color = [0,0,1,1]
            # elif current_color=='Green':
            #     current_color = [0,1,0,1]
            # elif current_color=='White':
            #     current_color = [1,1,1,1]
            # elif current_color=='Black':
            #     current_color = [0,0,0,0]
            # else :
            #     pass
    def adjustGridColors(self):
        inputs = [firstDot.text,secondDot.text,thirdDot.text,lastDot.text]
        chunks = (inputs,4)
        # for i in range(len(self.gridButtons)):
        #     if (round ==1):
        #         pass#self.gridButtons[i].background_color = 
            
        
        # #section to adjust the color of the grid        



    def build(self):
        self.title= 'Mastermind'
        self.infoButtons = []
        self.gridButtons = []
        self.menuScreen = Screen(name="menu")
        self.scoresScreen = Screen(name="scores")
        self.gameScreen = Screen(name="game")
        # les couleurs a obtenir pour gagner 
        self.winningCombination =[random.choice(colors),random.choice(colors),random.choice(colors),random.choice(colors)] 
        print(self.winningCombination)

        # on cree la page de menu
        Menu = BoxLayout(orientation='horizontal')
        lmargin = Label(text='',size_hint=(0.2,1))
        
        content = BoxLayout(orientation='vertical',size_hint=(0.8,1))
        play_Btn = Button(text='Jouer',id='play',size_hint=(1,0.4)) #on_press=self.screenChanger
        score_Btn = Button(text='Scores',id='score',size_hint=(1,0.4))  #on_press=self.screenChanger,
        content.add_widget(play_Btn)
        content.add_widget(score_Btn)
        rmargin = Label(text='',size_hint=(0.2,1))

        
        
        Menu.add_widget(lmargin)
        Menu.add_widget(content)
        Menu.add_widget(rmargin)

        self.menuScreen.add_widget(Menu)
        




        # pour contenir toutes les sections
        gamePage = BoxLayout(orientation='vertical')
        #section pour le titre 
        header  = BoxLayout(orientation ="horizontal",size_hint=(1,0.15))
        b1 = Button(text='Menu',background_color=[1, 0, 1, 1],size_hint=(0.1,1))
        header_label = Label(text="Mastermind",font_size="25sp",size_hint=(0.8,1))
        b2 = Button(text='Scores',background_color=[1, 0, 1, 1],size_hint=(0.1,1))
        header.add_widget(b1)
        header.add_widget(header_label)
        header.add_widget(b2)
        

        #Section pour le jeu : decomposée en 3 parties 
        gameSection = BoxLayout(orientation='horizontal',size_hint=(1,0.75))

        leftMargin = BoxLayout(orientation='vertical',size_hint=(0.1,1))
        l_label = Label(text="",size_hint=(1,0.9))
        leftMargin.add_widget(l_label)
        

        # grille de jeu 
        gameGrid = GridLayout(cols=4,rows=11,size_hint=(0.7,1))
        for i in range(1,41):
            btn = Button(text='')
            self.gridButtons.append(btn)   
            gameGrid.add_widget(btn)
        gameGrid.add_widget(firstDot)
        gameGrid.add_widget(secondDot)
        gameGrid.add_widget(thirdDot)
        gameGrid.add_widget(lastDot)

        rightMargin = BoxLayout(orientation='vertical',size_hint=(0.1,1))
        r_label = Label(text="",size_hint=(1,0.9))
        but1 = Button(text='Submit',background_color=[0, 1, 0, 1],size_hint=(1,0.1))
        but1.bind(on_press=self.getInfos)
        rightMargin.add_widget(r_label)
        rightMargin.add_widget(but1)

        gameSection.add_widget(leftMargin)
        gameSection.add_widget(gameGrid)
        gameSection.add_widget(rightMargin)

        # pied de page 
        footer = BoxLayout(orientation ="horizontal",size_hint=(1,0.10))
        footer_content = BoxLayout(orientation="vertical")
        lab1 = Label(text="",size_hint=(1,0.2))
        infoGrid = GridLayout(cols=4,rows=1,size_hint=(1,0.6))
        for i in range(0,4):
            btn = Button(text='') 
            self.infoButtons.append(btn)  
            infoGrid.add_widget(btn)
        lab2 = Label(text="",size_hint=(1,0.2))
        footer_content.add_widget(lab1)
        footer_content.add_widget(infoGrid)
        footer_content.add_widget(lab2)
        footer.add_widget(footer_content)

    


        gamePage.add_widget(header)
        gamePage.add_widget(gameSection)
        gamePage.add_widget(footer)
        self.gameScreen.add_widget(gamePage)
        sm.add_widget(self.menuScreen)
        sm.add_widget(self.gameScreen)
        #sm.add_widget(self.scoreScreen)
        return sm
        # on ajoute toutes les sections dans la page de jeu avant de la return




Main().run()