import blacjac as bj
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
        global mousepos
        if mousepos[0]<(self.pos[0]-5+80) and  mousepos[1]<(self.pos[1]-5+20) and mousepos[0]> (self.pos[0]-5) and mousepos[1] > (self.pos[1]-5) :
            print(f"clickbutton{self.label}")
            mousepos=(0,0)
        pygame.draw.rect(ren,self.colors[0], pygame.Rect(self.pos[0]-5,self.pos[1]-5, 80, 30))
        text = font.render(self.label, True, (255, 255, 255))
        ren.blit(text,self.pos)
def show_cards(ren,val,suite,pos):
    surface = pygame.image.load(f'cards/{suite}/{val}.png')
    surface = pygame.transform.scale(surface, (100, 150))
    ren.blit(surface, pos)
import pygame
pygame.init()
font=pygame.font.Font(pygame.font.get_default_font(), 20)
clock=pygame.time.Clock()
ren=pygame.display.set_mode((500,500))
pygame.display.set_caption("BlackJack")
isRunning=True
bHit=Button("Hit",(250,250))
bStay=Button("Stay",(340,250))
while (isRunning):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            button = pygame.mouse.get_pressed()
            if button == (1,0,0):
                    mousepos=pygame.mouse.get_pos()


    ren.fill([90,20,90])

    show_cards(ren,'K','Hearts',PCS[0])
    show_cards(ren, 'J', "Spades",PCS[1])
    show_cards(ren,'K','Hearts',DCS[0])
    show_cards(ren, 'J', "Spades",DCS[1])
    bHit.draw(ren,font)
    bStay.draw(ren,font)
    pygame.display.update()
    #clock.tick(60)

pygame.quit()
