import random

class Players:

    def __init__(self):

        self.Frequency = {}

        for i in range (1, 52):

            self.Frequency[i] = 0

        self.Card = 0

        self.Color = 0

        self.Card_Sum = 0

        self.Number_Aces = 0

    def Get_Card(self):

        New_Card = random.randrange(0, 51)

        while self.Frequency[New_Card + 1] != 0 :

            New_Card = random.randrange(0, 51)

        self.Frequency[New_Card + 1] = 1

        self.Card = New_Card % 13 + 1

        self.Color = int(New_Card / 13)

        if self.Card == 1:

            self.Number_Aces += 1

            self.Card_Sum += 11


        elif self.Card > 1 and self.Card < 11:

            self.Card_Sum += self.Card

        elif self.Card > 10:

            self.Card_Sum += 10

    def Hit_Stop(self):

        if self.Card_Sum > 21:

            return 0

        elif self.Card_Sum == 21:

            return 1

        return 2

    def Aces_Option(self):

        if self.Card_Sum > 21 and self.Number_Aces > 0:

            self.Card_Sum -= 10

            self.Number_Aces -= 1


