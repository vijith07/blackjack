import random as lol

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        lol.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
MAXCARDS=5
PCS=[[150+50*o,345-2*o] for o in range(MAXCARDS)]
DCS=[[150+50*o,0+2*o] for o in range(MAXCARDS)]
mousepos=(0,0)
class Button:

    def __init__(self,label,pos):
        self.label=label
        self.pos=pos
        self.colors=[[99,86,102],[54,47,56]]
    def draw(self,ren,font):
        pygame.draw.rect(ren,self.colors[0], pygame.Rect(self.pos[0]-5,self.pos[1]-5, 80, 30))
        text = font.render(self.label, True, (255, 255, 255))
        ren.blit(text,self.pos)

        
def show_cards(ren,val,suite,pos):
    surface = pygame.image.load(f'cards/{suite}/{val}.png')
    surface = pygame.transform.scale(surface, (100, 150))
    ren.blit(surface, pos)
def hidden(ren,pos):
    cover=lol.choice(['Emerald','Peter River','Pomegranate','Sun Flower'])
    surface = pygame.image.load(f'cards/Back Covers/{cover}.png')
    surface = pygame.transform.scale(surface, (100, 150))
    ren.blit(surface, pos)
class Game:
    def __init__(self):
        self.deck=Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.player_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand = Hand()
        self.dealer_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.player_chips = Chips()
        self.show_some(self.player_hand, self.dealer_hand,ren)
    def choice(self,buttonhit,buttonstay):
        global mousepos
        global playing
        while True:
         if mousepos[0]<(buttonhit.pos[0]-5+80) and  mousepos[1]<(buttonhit.pos[1]-5+20) and mousepos[0]> (buttonhit.pos[0]-5) and mousepos[1] > (buttonhit.pos[1]-5) :
                print(f"clickbutton{buttonhit.label}")
                mousepos=(0,0)
                self.hit(self.deck,self.player_hand)  # hit() function defined above

         elif mousepos[0]<(buttonstay.pos[0]-5+80) and  mousepos[1]<(buttonstay.pos[1]-5+20) and mousepos[0]> (buttonstay.pos[0]-5) and mousepos[1] > (buttonstay.pos[1]-5) :
             print(f"clickbutton{buttonstay.label}")
             mousepos=(0,0)
             print("Player stands. Dealer is playing.")
             playing = False
         break
    def show_some(self,player, dealer,ren):
        #hidden(ren,DCS[0])
        for index, card in enumerate(dealer.cards):
            if card.rank == 'Jack':
                val='J'
            if card.rank =='Queen':
                val='Q'
            if card.rank =='King':
                val='K'
            if card.rank == 'Ace':
                val='A'
            else:
                val=values[card.rank]
            show_cards(ren,val,card.suit,DCS[index])
        for index, card in enumerate(player.cards):
            if card.rank == 'Jack':
                val='J'
            if card.rank =='Queen':
                val='Q'
            if card.rank =='King':
                val='K'
            if card.rank == 'Ace':
                val='A'
            else:
                val=values[card.rank]
            show_cards(ren,val,card.suit,PCS[index])

    def show_all(self,player, dealer,ren):
        for index, card in enumerate(dealer.cards):
            if card.rank == 'Jack':
                val='J'
            if card.rank =='Queen':
                val='Q'
            if card.rank =='King':
                val='K'
            if card.rank == 'Ace':
                val='A'
            else:
                val=values[card.rank]
            show_cards(ren,val,card.suit,DCS[index])
        for index, card in enumerate(player.cards):
            if card.rank == 'Jack':
                val='J'
            if card.rank =='Queen':
                val='Q'
            if card.rank =='King':
                val='K'
            if card.rank == 'Ace':
                val='A'
            else:
                val=values[card.rank]
            show_cards(ren,val,card.suit,PCS[index])


    def player_busts(self,player, dealer, chips):
        global ren
        global font
        pygame.draw.rect(ren,[100,100,100], pygame.Rect(100,300,150,20))
        text = font.render("Player busts!", True, (255, 255, 255))
        ren.blit(text,(100,300))
        chips.lose_bet()


    def player_wins(self,player, dealer, chips):
        global ren
        global font
        pygame.draw.rect(ren,[100,100,100], pygame.Rect(100,300,150,20))
        text = font.render("UnForTuNATEly yoU wIn!", True, (255, 255, 255))
        ren.blit(text,(100,300))
        chips.win_bet()


    def dealer_busts(self,player, dealer, chips):
        global ren
        global font
        pygame.draw.rect(ren,[100,100,100], pygame.Rect(100,300,150,20))
        text = font.render("DeALeR busts!", True, (255, 255, 255))
        ren.blit(text,(100,300))
        chips.win_bet()


    def dealer_wins(self,player, dealer, chips):
        global ren
        global font
        pygame.draw.rect(ren,[100,100,100], pygame.Rect(100,300,150,20))
        text = font.render("FKIN LOSER!", True, (255, 255, 255))
        ren.blit(text,(100,300))
        chips.lose_bet()


    def push(self,player, dealer):
        global ren
        global font
        pygame.draw.rect(ren,[100,100,100], pygame.Rect(100,300,400,20))
        text = font.render("TIE. Atleast you didnt become a beggar", True, (255, 255, 255))
        ren.blit(text,(100,300))

    def take_bet(self,chips,ren,font):
            global bettaken
            global mousepos
            pygame.draw.rect(ren,[100,100,100], pygame.Rect(100,100,150,20))
            text = font.render("Enter the Bet :", True, (255, 255, 255))
            ren.blit(text,(100,100))
            pygame.draw.rect(ren,[100,100,100], pygame.Rect(270,100,100,20))
            bet=font.render("10 coins", True, (100, 255, 255))
            ren.blit(bet,(270,100))
            pygame.draw.rect(ren,[100,100,100], pygame.Rect(270,150,100,20))
            bet=font.render("25 coins", True, (100, 255, 255))
            ren.blit(bet,(270,150))
            pygame.draw.rect(ren,[100,100,100], pygame.Rect(270,200,100,20))
            bet=font.render("50 coins", True, (100, 255, 255))
            ren.blit(bet,(270,200))
            pygame.draw.rect(ren,[100,100,100], pygame.Rect(270,250,100,20))
            bet=font.render("100 coins", True, (100, 255, 255))
            ren.blit(bet,(270,250))
            pygame.display.update()
            if mousepos[0]<(270+100) and  mousepos[1]<(100+20) and mousepos[0]> (270) and mousepos[1] > (100) :
               chips.bet=10
               mousepos=(0,0)
               bettaken=True
            elif mousepos[0]<(270+100) and  mousepos[1]<(150+20) and mousepos[0]> (270) and mousepos[1] > (150) :
               chips.bet=25
               mousepos=(0,0)
               bettaken=True
            elif mousepos[0]<(270+100) and  mousepos[1]<(200+20) and mousepos[0]> (270) and mousepos[1] > (200) :
               chips.bet=50
               mousepos=(0,0)
               bettaken=True
            elif mousepos[0]<(270+100) and  mousepos[1]<(250+20) and mousepos[0]> (270) and mousepos[1] > (250) :
               chips.bet=100
               mousepos=(0,0)
               bettaken=True

    def hit(self,deck,hand):
        hand.add_card(self.deck.deal())
        hand.adjust_for_ace()
import pygame
pygame.init()
font=pygame.font.Font(pygame.font.get_default_font(), 20)
clock=pygame.time.Clock()
ren=pygame.display.set_mode((500,500))
pygame.display.set_caption("BlackJack")
isRunning=True
bHit=Button("Hit",(250,250))
bStay=Button("Stay",(340,250))
game=Game()
bettaken=False
while (isRunning):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            button = pygame.mouse.get_pressed()
            if button == (1,0,0):
                    mousepos=pygame.mouse.get_pos()

                    
    ren.fill([90,20,90])
    if not bettaken:
        game.take_bet(game.player_chips,ren,font)
    else:
        game.show_some(game.player_hand,game.dealer_hand,ren)
        bHit.draw(ren,font)
        bStay.draw(ren,font)
        game.choice(bHit,bStay)
        if playing:
            if game.player_hand.value > 21:
                    game.player_busts(game.player_hand, game.dealer_hand, game.player_chips)
            elif game.player_hand.value == 21:
                print("21")
        else :
            if game.player_hand.value <= 21:
                while game.dealer_hand.value < 17:
                    game.hit(game.deck, game.dealer_hand)
            game.show_all(game.player_hand,game.dealer_hand,ren)
            if game.dealer_hand.value > 21:
                game.dealer_busts(game.player_hand, game.dealer_hand, game.player_chips)

            elif game.dealer_hand.value > game.player_hand.value:
                game.dealer_wins(game.player_hand, game.dealer_hand, game.player_chips)

            elif game.dealer_hand.value < game.player_hand.value:
                game.player_wins(game.player_hand, game.dealer_hand, game.player_chips)

            else:
                game.push(game.player_hand, game.dealer_hand)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
