
import pygame
from pygame.locals import *
from random import randint,choice

pygame.init()

win = pygame.display.set_mode((800,700))

pygame.display.set_caption("HangMan!")

letter=0
words=randint(3,10)
word=[]
if words==3:
	word=["ICE","OAK","BAT","SUN","CAN","RAT","DOG","CAT","GAS","PEN","FAN","RUG","MUG","JOY","PAN","SUM"]
elif words==4:
	word=["KIWI","LEAF","BALL","COAL","LION","BIRD","CODE","DICE","MICE","BOOK","MILL","SWAN","STAR","ROPE"]
elif words==5:
	word=["WATCH","TIGER","ONION","EVENT","GLASS","MONEY","SPACE","TRUCK","BREAD","TRAIN","RADIO","MOVIE","ENERGY","ANGRY","HAPPY"]
elif words==6:
	word=["ORANGE","GARLIC","GOBLIN","PENCIL","PYTHON","SCHOOL","POTATO","CIRCLE","MEMORY","TABLET","ENGINE","NATION"]
elif words==7:
	word=["PROGRAM","CRICKET","ARTICLE","PHYSICS","OMANSHU","HANGMAN","BLANKET","BAGGAGE","RAILWAY","METHANE","HISTORY","ENGLISH","MACHINE","SCIENCE","PRODUCT","CONCERT"]
elif words==8:
	word=["COMPUTER","CHILDREN","MEDICINE","QUESTION","PLATFORM","NOVEMBER","WIRELESS"]
elif words==9:
	word=["TELESCOPE","NEWSPAPER","TELEGRAPH","CONDUCTOR","GENERATOR","AEROPLANE","ANIMATION","HYPERLOOP","PETROLEUM","SPACESHIP","HEADPHONE","CHEMISTRY","GEOGRAPHY","PRESIDENT"]
elif words==10:
	word=["TELEVISION","RHINOCERES","METROPOLIS","TECHNOLOGY","MATHEMATIC","BACKGROUND"]
answer=choice(word)
wrong=0
score=0
x=100
clock = pygame.time.Clock()
bg=pygame.image.load("bgH.jpeg")
music=pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.play(-1)
bg2=pygame.transform.scale(bg,(800,700))

class Rectangle:
    def __init__(self, pos, color, size):
        self.pos = pos
        self.color = color
        self.size = size
    def draw(self):
        pygame.draw.rect(win, self.color, Rect(self.pos, self.size))

rectangles = []     

for count in range(words):
    random_color = (randint(0,255), randint(0,255), randint(0,255))
    random_pos = (randint(0,639), randint(0,479))
    random_size = (639-randint(random_pos[0], 639), 479-randint(random_pos[1],479))

    rectangles.append(Rectangle((x,650),random_color, (40,10)))
    x+=50
    
def display():
	win.fill((0,0,255))
	win.blit(bg2,(0,0))
	pygame.draw.circle(win,(255,255,255), (30,25), 20,2)
	pygame.draw.circle(win,(255,255,255), (80,25), 20,2)
	pygame.draw.circle(win,(255,255,255), (130,25), 20,2)
	pygame.draw.circle(win,(255,255,255), (180,25), 20,2)
	pygame.draw.circle(win,(255,255,255), (230,25), 20,2)
	pygame.draw.circle(win,(255,255,255), (280,25), 20,2)
	pygame.draw.circle(win,(255,255,255), (330,25), 20,2)
	pygame.draw.circle(win,(255,255,255), (380,25), 20,2)
	pygame.draw.circle(win,(255,255,255), (430,25), 20,2)
	pygame.draw.circle(win,(255,255,255), (480,25), 20,2)
	pygame.draw.circle(win,(255,255,255), (530,25), 20,2)
	pygame.draw.circle(win,(255,255,255), (580,25), 20,2)
	pygame.draw.circle(win,(255,255,255), (630,25), 20,2)
	pygame.draw.circle(win,(255,255,255), (680,25), 20,2)
	pygame.draw.circle(win,(255,255,255), (730,25), 20,2)
	pygame.draw.circle(win,(255,255,255), (50,70), 20,2)
	pygame.draw.circle(win,(255,255,255), (100,70), 20,2)
	pygame.draw.circle(win,(255,255,255), (150,70), 20,2)
	pygame.draw.circle(win,(255,255,255), (200,70), 20,2)
	pygame.draw.circle(win,(255,255,255), (250,70), 20,2)
	pygame.draw.circle(win,(255,255,255), (300,70), 20,2)
	pygame.draw.circle(win,(255,255,255), (350,70), 20,2)
	pygame.draw.circle(win,(255,255,255), (400,70), 20,2)
	pygame.draw.circle(win,(255,255,255), (450,70), 20,2)
	pygame.draw.circle(win,(255,255,255), (500,70), 20,2)
	pygame.draw.circle(win,(255,255,255), (550,70), 20,2)

	textA=fontA.render('A',1,(0,220,220))
	textB=fontB.render('B',1,(0,220,220))
	textC=fontC.render('C',1,(0,220,220))
	textD=fontD.render('D',1,(0,220,220))
	textE=fontE.render('E',1,(0,220,220))
	textF=fontF.render('F',1,(0,220,220))
	textG=fontG.render('G',1,(0,220,220))
	textH=fontH.render('H',1,(0,220,220))
	textI=fontI.render('I',1,(0,220,220))
	textJ=fontJ.render('J',1,(0,220,220))
	textK=fontK.render('K',1,(0,220,220))
	textL=fontL.render('L',1,(0,220,220))
	textM=fontM.render('M',1,(0,220,220))
	textN=fontN.render('N',1,(0,220,220))
	textO=fontO.render('O',1,(0,220,220))
	textP=fontP.render('P',1,(0,220,220))
	textQ=fontQ.render('Q',1,(0,220,220))
	textR=fontR.render('R',1,(0,220,220))
	textS=fontS.render('S',1,(0,220,220))
	textT=fontT.render('T',1,(0,220,220))
	textU=fontU.render('U',1,(0,220,220))
	textV=fontV.render('V',1,(0,220,220))
	textW=fontW.render('W',1,(0,220,220))
	textX=fontX.render('X',1,(0,220,220))
	textY=fontY.render('Y',1,(0,220,220))
	textZ=fontZ.render('Z',1,(0,220,220))
	text4=font4.render(f"Score:: {score}",1,(255,0,0))
	global guess
	text7=font7.render(guess,1,(255,0,0))
	text2=font2.render("Made By OMANSHU",1,(143,0,255))
	text5=font5.render("DELETE",1,(255,165,0))
	win.blit(text4,(50,120))
	win.blit(text5,(683,145))
	win.blit(text2,(600,650))
	win.blit(text7,(100,600))
	win.blit(textA,(16,12))
	win.blit(textB,(66,12))
	win.blit(textC,(116,12))
	win.blit(textD,(166,12))
	win.blit(textE,(216,12))
	win.blit(textF,(266,12))
	win.blit(textG,(316,12))
	win.blit(textH,(366,12))
	win.blit(textI,(422,12))
	win.blit(textJ,(466,12))
	win.blit(textK,(516,12))
	win.blit(textL,(570,12))
	win.blit(textM,(616,12))
	win.blit(textN,(670,12))
	win.blit(textO,(716,12))
	win.blit(textP,(40,57))
	win.blit(textQ,(90,57))
	win.blit(textR,(140,57))
	win.blit(textS,(190,57))
	win.blit(textT,(240,57))
	win.blit(textU,(290,57))
	win.blit(textV,(340,57))
	win.blit(textW,(385,57))
	win.blit(textX,(440,57))
	win.blit(textY,(490,57))
	win.blit(textZ,(540,57))
	pygame.draw.rect(win,(0,0,255),(680,120,100,70))
	win.blit(text5,(683,145))
	pygame.draw.rect(win,(150,155,255),(0,0,800,700),2)
	if wrong>=1:
	    pygame.draw.rect(win,(0,255,0),(180,530,120,10))
	if wrong>=2:
	    pygame.draw.rect(win,(0,255,0),(240,180,10,350))
	if wrong>=3:
	    pygame.draw.rect(win,(0,255,0),(200,200,300,10))
	if wrong>=4:
	    pygame.draw.rect(win,(0,255,0),(450,200,10,100))
	if wrong>=5:
	    pygame.draw.circle(win,(0,255,0), (450,340), 40,2)
	if wrong>=6:
	    pygame.draw.circle(win,(0,0,0), (450,342), 35)
	if wrong>=7:
	    pygame.draw.rect(win,(0,0,0),(450,360,7,110))
	if wrong>=8:
	    pygame.draw.line(win, (0, 0, 0), (450,380), (400, 450),6)
	if wrong>=9:
	    pygame.draw.line(win,(0,0,0),(455,380),(500,450),6)
	if wrong>=10:
	    pygame.draw.line(win,(0,0,0),(450,460),(400,520),6)
	if wrong>=11:
	    pygame.draw.line(win,(0,0,0),(455,460),(500,520),6)
	    win.fill((0,0,255))
	    text1=font1.render("Game Over!",1,(143,0,255))
	    text4=font4.render(f"Score:: {score}",1,(255,0,0))
	    text3=font3.render(f"Answer:: {answer}",1,(0,255,0))
	    win.blit(text3,(470,300))
	    win.blit(text1,(400,350))
	    win.blit(text4,(470,450))
	win.lock()
	for rectangle in rectangles:
	   rectangle.draw()
	win.unlock()
	pygame.display.update()

	
fontA=pygame.font.SysFont("comicsans",45,True)
fontB=pygame.font.SysFont("comicsans",45,True)
fontC=pygame.font.SysFont("comicsans",45,True)
fontD=pygame.font.SysFont("comicsans",45,True)
fontE=pygame.font.SysFont("comicsans",45,True)
fontF=pygame.font.SysFont("comicsans",45,True)
fontG=pygame.font.SysFont("comicsans",45,True)
fontH=pygame.font.SysFont("comicsans",45,True)
fontI=pygame.font.SysFont("comicsans",45,True)
fontJ=pygame.font.SysFont("comicsans",45,True)
fontK=pygame.font.SysFont("comicsans",45,True)
fontL=pygame.font.SysFont("comicsans",45,True)
fontM=pygame.font.SysFont("comicsans",45,True)
fontN=pygame.font.SysFont("comicsans",45,True)
fontO=pygame.font.SysFont("comicsans",45,True)
fontP=pygame.font.SysFont("comicsans",45,True)
fontQ=pygame.font.SysFont("comicsans",45,True)
fontR=pygame.font.SysFont("comicsans",45,True)
fontS=pygame.font.SysFont("comicsans",45,True)
fontT=pygame.font.SysFont("comicsans",45,True)
fontU=pygame.font.SysFont("comicsans",45,True)
fontV=pygame.font.SysFont("comicsans",45,True)
fontW=pygame.font.SysFont("comicsans",45,True)
fontX=pygame.font.SysFont("comicsans",45,True)
fontY=pygame.font.SysFont("comicsans",45,True)
fontZ=pygame.font.SysFont("comicsans",45,True)
font7=pygame.font.SysFont("comicsans",80,True)
font2=pygame.font.SysFont("comicsans",20,True,True)
font5=pygame.font.SysFont("comicsans",30,True)
font4=pygame.font.SysFont("comicsans",60,True)
font1=pygame.font.SysFont("comicsans",100,True)
font3=pygame.font.SysFont("comicsans",60,True)

k=100
guess=""			
run=True
while run:
    #clock.tick(50)
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type==pygame.MOUSEBUTTONDOWN:
        	mx,my=pygame.mouse.get_pos()
        	if mx<40 and my<30 and mx>10 and my>10 and letter<=words:
        		if 'A' in answer:
        		    guess+='A'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<100 and my<30 and mx>40 and my>10 and letter<=words:
        		if 'B' in answer:
        		    guess+='B'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<160 and my<30 and mx>100 and my>10 and letter<=words:
        		if 'C' in answer:
        		    guess+='C'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<220 and my<30 and mx>160 and my>10 and letter<=words:
        		if 'D' in answer:
        		    guess+='D'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<280 and my<30 and mx>220 and my>10 and letter<=words:
        		if 'E' in answer:
        		    guess+='E'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<320 and my<30 and mx>280 and my>10 and letter<=words:
        		if 'F' in answer:
        		    guess+='F'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<360 and my<30 and mx>320 and my>10 and letter<=words:
        		if 'G' in answer:
        		    guess+='G'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<415 and my<30 and mx>360 and my>10 and letter<=words:
        		if 'H' in answer:
        		    guess+='H'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<460 and my<30 and mx>415 and my>10 and letter<=words:
        		if 'I' in answer:
        		    guess+='I'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<500 and my<30 and mx>460 and my>10 and letter<=words:
        		if 'J' in answer:
        		    guess+='J'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<540 and my<30 and mx>500 and my>10 and letter<=words:
        		if 'K' in answer:
        		    guess+='K'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<600 and my<30 and mx>540 and my>10 and letter<=words:
        		if 'L' in answer:
        		    guess+='L'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<650 and my<30 and mx>600 and my>10 and letter<=words:
        		if 'M' in answer:
        		    guess+='M'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<700 and my<30 and mx>650 and my>10 and letter<=words:
        		if 'N'in answer:
        		    guess+='N'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<750 and my<30 and mx>700 and my>10 and letter<=words:
        		if 'O' in answer:
        		     guess+='O'
        		     pygame.display.update()
        		     letter+=1
        		     k+=50
        		else:
        		 	wrong+=1
        	if mx<80 and my<100 and mx>30 and my>50 and letter<=words:
        		if 'P' in answer:
        		    guess+='P'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<125 and my<100 and mx>80 and my>50 and letter<=words:
        		if 'Q' in answer:
        		    guess+='Q'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<170 and my<100 and mx>125 and my>50 and letter<=words:
        		if 'R'in answer:
        		    guess+='R'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<225 and my<100 and mx>170 and my>50 and letter<=words:
        		if 'S'in answer:
        		    guess+='S'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<275 and my<100 and mx>225 and my>50 and letter<=words:
        		if 'T' in answer:
        		    guess+='T'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<335 and my<100 and mx>275 and my>50 and letter<=words:
        		if 'U'in answer:
        		    guess+='U'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<370 and my<100 and mx>335 and my>50 and letter<=words:
        		if 'V'in answer:
        		    guess+='V'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<420 and my<100 and mx>370 and my>50 and letter<=words:
        		if 'W' in answer:
        		    guess+='W'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<480 and my<100 and mx>420 and my>50 and letter<=words:
        		if 'X'in answer:
        		    guess+='X'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<530 and my<100 and mx>480 and my>50 and letter<=words:
        		if 'Y'in answer:
        		    guess+='Y'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	if mx<580 and my<100 and mx>530 and my>50 and letter<=words:
        		if 'Z'in answer:
        		    guess+='Z'
        		    pygame.display.update()
        		    letter+=1
        		    k+=50
        		else:
        			wrong+=1
        	#680,120,100,70
        	if mx<780 and my<190 and mx>680 and my>120 and letter>0:
        		guess=guess.rstrip(guess[-1])
        		letter-=1
        	if guess==answer:
        		letter=0
        		wrong=0
        		score+=1
        		words=randint(3,10)
        		answer=choice(word)
        		x=100
        		guess=""
        		rectangles = []
        		for count in range(words):
        			random_color = (randint(0,255), randint(0,255), randint(0,255))
        			rectangles.append(Rectangle((x,650),random_color, (40,10)))
        			x+=50		
    display()            
pygame.quit()
