from BlackJack import *

import pygame

class HOL_GUI:

    def __init__(self):

        self.Score = 0

        self.Strikes = 0

        self.Option = ""

        self.BackGround = pygame.image.load("Table.png")

        self.Screen = 0

    def Get_Card_Image(self, Player):

        if Player.Card == 1:

            Image_Code = "A"

        elif Player.Card < 11:

            Image_Code = str(Player.Card)

        elif Player.Card == 11:

            Image_Code = "J"

        elif Player.Card == 12:

            Image_Code = "Q"

        else:

            Image_Code = "K"

        if Player.Color == 0:

            Image_Code = Image_Code + "H"

        elif Player.Color == 1:

            Image_Code = Image_Code + "S"

        elif Player.Color == 2:

            Image_Code = Image_Code + "D"

        else:

            Image_Code = Image_Code + "C"

        Image_Code = Image_Code + ".png"

        return Image_Code

    def Background_Display(self):

        pygame.init()

        self.Screen = pygame.display.set_mode([800, 600])

        self.Screen.blit(self.BackGround, (0, 0))

    def Game_Loop(self):

        self.Background_Display()

        pygame.display.flip()

        Running = True

        while Running:

            for Event in pygame.event.get():

                if Event.type == pygame.QUIT:

                    Running = False

                if Event.type == pygame.MOUSEBUTTONDOWN:

                    X_Pos, Y_Pos = pygame.mouse.get_pos()

                    print (X_Pos, Y_Pos)

                    #if 70 <= X_Pos <= 366 and 366 <= Y_Pos <= 506:          #HIGHER



                    #elif 449 <= X_Pos <= 686 and 366 <= Y_Pos <= 505:       #LOWER

Masa = HOL_GUI()

Masa.Game_Loop()
