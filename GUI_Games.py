import pygame
from BlackJack import *
import time


class BlackJack_Gui:

    def __init__(self):

        self.X1_Coordinates = 210

        self.Y1_Coordinates = 260

        self.X2_Coordinates = 393

        self.Y2_Coordinates = 105

        self.Card_Image = ""

        self.Screen = 0

        self.Background = pygame.image.load('Table_2.jpg')

    def Color_Back(self):

        Image = pygame.image.load("Red.png")

        self.Screen.blit(Image, (500, 500))

        pygame.display.flip()

    def Show_Player(self, x, y, Player_Turn):

        Font = pygame.font.Font('freesansbold.ttf', 32)

        Player_Turn_Show = Font.render("Player " + str(Player_Turn), True, (255, 255, 255))

        self.Screen.blit(Player_Turn_Show, (x, y))

        pygame.display.flip()

    def Show_Card(self, Player, X, Y):

        self.Card_Image = self.Get_Image(Player.Card, Player.Color)

        Image_Name = pygame.image.load(self.Card_Image)

        self.Screen.blit(Image_Name, (X, Y))

        pygame.display.flip()

    def Player_Show_Turn(self, Player):

        if Player != 4:
            Font1 = pygame.font.SysFont('Comic Sans MS', 25)

            textsurface = Font1.render("Player " + str(Player) + " turn", False, (255, 255, 255))

            self.Screen.blit(textsurface, (500, 500))

    def Get_Image(self, Card_Number, Card_Color):

        if Card_Number == 1:

            Image_Code = "A"

        elif Card_Number == 11:

            Image_Code = "J"

        elif Card_Number == 12:

            Image_Code = "Q"

        elif Card_Number == 13:

            Image_Code = "K"

        else:

            Image_Code = str(Card_Number)

        if Card_Color == 0:

            Image_Code = Image_Code + "H"

        elif Card_Color == 1:

            Image_Code = Image_Code + "D"

        elif Card_Color == 2:

            Image_Code = Image_Code + "S"

        else:

            Image_Code = Image_Code + "C"

        Image_Code = Image_Code + ".png"

        return Image_Code

    def BackGround_Display(self):

        pygame.init()

        self.Screen = pygame.display.set_mode([800, 600])

        self.Background = pygame.image.load('Table_2.jpg')

        pygame.display.set_caption("Blackjack")

        pygame.display.set_icon(pygame.image.load('Table_2.jpg'))

        self.Screen.fill((110, 0, 0))

        self.Screen.blit(self.Background, (0, 0))

        Back_Image = pygame.image.load("CB.png")

        self.Screen.blit(Back_Image, (338, 105))

    def Final_Move(self, Image_Name):

        Image = pygame.image.load(str(Image_Name))

        self.Screen.blit(Image, (0, 0))

    def Game_Loop(self):

        self.BackGround_Display()

        Player1 = Players()

        Player2 = Players()

        Player_Turn = 1

        Beginning_Game = 0

        First = 0

        Running = True

        while Running:

            pygame.display.flip()

            if Beginning_Game == 0:

                Player1.Get_Card()

                self.Show_Card(Player1, self.X1_Coordinates, self.Y1_Coordinates)

                self.X1_Coordinates += 50

                Player1.Get_Card()

                self.Show_Card(Player1, self.X1_Coordinates, self.Y1_Coordinates)

                self.X1_Coordinates += 50

                Player2.Get_Card()

                self.Show_Card(Player2, self.X2_Coordinates, self.Y2_Coordinates)

                self.X2_Coordinates -= 60

                if Player1.Card_Sum == 21:
                    self.Final_Move("Win1.png")

                    Player_Turn = 4

                Beginning_Game = 1

                if First == 1:
                    Player2.Get_Card()

                    Player2.Aces_Option()

                    self.Show_Card(Player2, self.X2_Coordinates, self.Y2_Coordinates)

                    self.X2_Coordinates -= 60

                    First = 0

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    Running = False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    Mouse_X, Mouse_Y = pygame.mouse.get_pos()

                    if 36 <= Mouse_X <= 129 and 471 <= Mouse_Y <= 562 and Player_Turn == 1:  # HIT

                        time.sleep(0.5)

                        Player1.Get_Card()

                        Player1.Aces_Option()

                        time.sleep(0.5)

                        self.Show_Card(Player1, self.X1_Coordinates, self.Y1_Coordinates)

                        self.X1_Coordinates += 50

                        if Player1.Hit_Stop() == 0:

                            Player_Turn = 4

                            time.sleep(2)

                            self.Final_Move("Busted1.png")

                        elif Player1.Hit_Stop() == 1:

                            time.sleep(2)

                            self.Color_Back()

                            Player2.Get_Card()

                            Player2.Aces_Option()

                            self.Show_Card(Player2, self.X2_Coordinates, self.Y2_Coordinates)

                            self.X2_Coordinates -= 60

                            while Player_Turn != 3:

                                time.sleep(2)

                                if Player2.Card_Sum > Player1.Card_Sum or Player2.Card_Sum >= 17:

                                    Player_Turn = 3

                                else:

                                    Player2.Get_Card()

                                    Player2.Aces_Option()

                                    self.Show_Card(Player2, self.X2_Coordinates, self.Y2_Coordinates)

                                    self.X2_Coordinates -= 60

                                time.sleep(2)

                            if Player2.Card_Sum > Player1.Card_Sum or Player2.Card_Sum >= 17:

                                Player_Turn = 3

                            else:

                                Player2.Get_Card()

                                Player2.Aces_Option()

                                self.Show_Card(Player2, self.X2_Coordinates, self.Y2_Coordinates)

                                self.X2_Coordinates -= 60

                    if 165 <= Mouse_X <= 257 and 470 <= Mouse_Y <= 561 and Player_Turn == 1:  # STAND

                        self.Color_Back()

                        Player2.Get_Card()

                        Player2.Aces_Option()

                        self.Show_Card(Player2, self.X2_Coordinates, self.Y2_Coordinates)

                        self.X2_Coordinates -= 60

                        while Player_Turn != 3:

                            time.sleep(2)

                            if Player2.Card_Sum > Player1.Card_Sum or Player2.Card_Sum >= 17:

                                Player_Turn = 3

                            else:

                                Player2.Get_Card()

                                Player2.Aces_Option()

                                self.Show_Card(Player2, self.X2_Coordinates, self.Y2_Coordinates)

                                self.X2_Coordinates -= 60

            if Player_Turn == 3:

                if Player1.Card_Sum > 21:

                    time.sleep(0.5)

                    self.Final_Move("Busted1.png")

                    Player_Turn = 4

                else:

                    Player_Turn = 4

                    if Player2.Card_Sum > 21:

                        time.sleep(0.5)

                        self.Final_Move("Win1.png")

                    else:

                        if Player1.Card_Sum > Player2.Card_Sum:

                            time.sleep(0.5)

                            self.Final_Move("Win1.png")

                        elif Player1.Card_Sum == Player2.Card_Sum:

                            time.sleep(0.5)

                            self.Final_Move("equal.png")

                            time.sleep(5)

                            self.X1_Coordinates = 210

                            self.Y1_Coordinates = 260

                            self.X2_Coordinates = 393

                            self.Y2_Coordinates = 105

                            self.Game_Loop()

                        else:

                            time.sleep(0.5)

                            self.Final_Move("Busted1.png")

            pygame.display.update()


BlackJack_Game = BlackJack_Gui()
BlackJack_Game.Game_Loop()
