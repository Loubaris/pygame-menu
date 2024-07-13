import pygame
from random import randrange
from time import sleep
from audioplayer import AudioPlayer
pygame.init()



pygame.display.set_caption("Dreamland Battles")
screen = pygame.display.set_mode((1000, 600))

print("LANCEMENT DE DREAMLAND BATTLES")

# CHARGEMENT DES IMAGES

background = pygame.image.load("assets/images/menubg.png").convert_alpha()
background = pygame.transform.scale(background, (1000, 600))

transition = pygame.image.load("assets/images/transition.png").convert_alpha()
transition = pygame.transform.scale(transition, (1000, 605))


# MAIN MENU BUTTON 

mainmenubutton = pygame.image.load("assets/images/buttons/mainmenu.png").convert_alpha()
mainmenubutton = pygame.transform.scale(mainmenubutton, (130, 20))
mainmenubuttonhover = pygame.image.load("assets/images/buttons/mainmenuhover.png").convert_alpha()
mainmenubuttonhover = pygame.transform.scale(mainmenubuttonhover, (130, 20))

# CREDITS BUTTON

creditsbutton = pygame.image.load("assets/images/buttons/credits.png").convert_alpha()
creditsbutton = pygame.transform.scale(creditsbutton, (100, 20))
creditsbuttonhover = pygame.image.load("assets/images/buttons/creditshover.png").convert_alpha()
creditsbuttonhover = pygame.transform.scale(creditsbuttonhover, (110, 20))

# SETTINGS BUTTON

settingsbutton = pygame.image.load("assets/images/buttons/settings.png").convert_alpha()
settingsbutton = pygame.transform.scale(settingsbutton, (100, 20))
settingsbuttonhover = pygame.image.load("assets/images/buttons/settingshover.png").convert_alpha()
settingsbuttonhover = pygame.transform.scale(settingsbuttonhover, (110, 20))

# TUTORIAL BUTTON

tutorialbutton = pygame.image.load("assets/images/buttons/tutorial.png").convert_alpha()
tutorialbutton = pygame.transform.scale(tutorialbutton, (100, 20))
tutorialbuttonhover = pygame.image.load("assets/images/buttons/tutorialhover.png").convert_alpha()
tutorialbuttonhover = pygame.transform.scale(tutorialbuttonhover, (110, 20))

# TUTORIAL BUTTON

playbutton = pygame.image.load("assets/images/buttons/play.png").convert_alpha()
playbutton = pygame.transform.scale(playbutton, (60, 15))
playbuttonhover = pygame.image.load("assets/images/buttons/playhover.png").convert_alpha()
playbuttonhover = pygame.transform.scale(playbuttonhover, (110, 20))


# SETTINGS PAGE


settingsbg = pygame.image.load("assets/images/settings/settingsbg.png").convert_alpha()
settingsbg = pygame.transform.scale(settingsbg, (1000, 605))
settingsbg.set_alpha(100)

sliderbar = pygame.image.load("assets/images/settings/sliderbar.png").convert_alpha()
sliderbar = pygame.transform.scale(sliderbar, (500, 15))


sliderset = pygame.image.load("assets/images/settings/sliderset.png").convert_alpha()
sliderset = pygame.transform.scale(sliderset, (22, 38))

toggle_on = pygame.image.load("assets/images/settings/toggle_on.png").convert_alpha()
toggle_on = pygame.transform.scale(toggle_on, (25, 42))

toggle_off = pygame.image.load("assets/images/settings/toggle_off.png").convert_alpha()
toggle_off = pygame.transform.scale(toggle_off, (25, 42))


descsettings = pygame.image.load("assets/images/settings/descsettings.png").convert_alpha()
descsettings = pygame.transform.scale(descsettings, (400, 300))


controlsettings = pygame.image.load("assets/images/settings/controls.png").convert_alpha()
controlsettings = pygame.transform.scale(controlsettings, (400, 300))

# LOGO

dreamland = pygame.image.load("assets/images/dreamland.png").convert_alpha()
dreamland = pygame.transform.scale(dreamland, (460, 80))

running = True

# CHARGEMENT DES SONS


mainmenusound = AudioPlayer("assets/sounds/menu.wav")

btnclick = AudioPlayer("assets/sounds/click.wav")

playbtnsound = AudioPlayer("assets/sounds/playbtn.mp3")

slidesound = AudioPlayer("assets/sounds/slide.wav")

onsound = AudioPlayer("assets/sounds/on.mp3")
offsound = AudioPlayer("assets/sounds/off.mp3")














# Initialisation des variables de l'engine
menuone = 1
menutwo = 0
menutwoclickable = 0
mouvement = 0
mnbtnhover = 0
ctsbtnhover = 0
stsbtnhover = 0
tttbtnhover = 0
plybtnhover = 0

settingspage = 0
settingspagebackgroundoff = 0


animone = 0
mnmnx = -10
mnmny = 600
mntwobtn = -110
animbtntwo = 0
animbtnone = 0
transitiony = -605
transparencelogo = 0
transpaanim = 0
transpaanimtwo = 0

mouseclicked = 0

# Settings
settingsbgy = -605
set1x = 489
set2x = 400
set3x = 581
setxpos = set1x
optionssettings = 1
slidechanged = 1

soption1 = True
soption2 = True
soption3 = True

ingame = 0
startinggame = 0
enteringgame = 0
enteringgamelspart = 0
# PERSONNAGE

skill = 0


while running:	

	xmouse, ymouse = pygame.mouse.get_pos()
	screen.blit(background, (1, 1))
	
	# ANIMATIONS
		# MENU BUTTON
	dreamland.set_alpha(transparencelogo)
	if transpaanim == 0:
		if transparencelogo < 255:
			transparencelogo+=1.8
			
		else:
			transparencelogo = 255
			transpaanim = 1
	if animone!=2:
		if mnmnx <= 20:
			mnmnx+=0.2
		elif mnmnx > 20:
			mnmnx = 20
		if mnmny >= 550:
			mnmny-=0.26
		elif mnmny < 550:
			mnmny = 550
			animone=2
			# STARTING MENU SOUND
			mainmenusound.play()

	# MENU 2 BUTTONS ANIMATION


	#INTRO
	# Main menu partie 1

	if menuone == 1:
		screen.blit(dreamland, (470, 50))
		if mnbtnhover == 0:
			screen.blit(mainmenubutton, (mnmnx, mnmny))
		elif mnbtnhover == 1:
			screen.blit(mainmenubuttonhover, (mnmnx, 550))

	if animbtnone == 1:
		if mnmnx >= -110:
			mnmnx-=1
			mnbtnhover = 0
		else:
			animbtnone = 0
			menuone = 0
			menutwo = 1
			menutwoclickable = 1


	# MAIN Menu partie 2

	if menutwo == 1:
		screen.blit(dreamland, (470, 50))
		if animbtntwo == 0:
			if mntwobtn <= 20:
				mntwobtn+=1
			else:
				animbtntwo = 1
		if ctsbtnhover == 0:
			screen.blit(creditsbutton, (mntwobtn, 550))
		elif ctsbtnhover == 1:
			screen.blit(creditsbuttonhover, (mntwobtn, 550))

		if stsbtnhover == 0:
			screen.blit(settingsbutton, (mntwobtn, 500))
		elif stsbtnhover == 1:
			screen.blit(settingsbuttonhover, (mntwobtn, 500))
		
		if tttbtnhover == 0:
			screen.blit(tutorialbutton, (mntwobtn, 450))
		elif tttbtnhover == 1:
			screen.blit(tutorialbuttonhover, (mntwobtn, 450))

		if plybtnhover == 0:
			screen.blit(playbutton, (mntwobtn, 400))
		elif plybtnhover == 1:
			screen.blit(playbuttonhover, (mntwobtn, 400))


	screen.blit(settingsbg, (0, settingsbgy))

	# SETTINGS PAGE
		# ANIMATION
	if settingspage == 1:
		if settingsbgy < -2:
			settingsbgy+=6
		elif settingsbgy >= -2:
			menutwoclickable = 0
			stsbtnhover = 0
			# SLIDE BAR DES OPTIONS SETTINGS
			screen.blit(sliderbar, (250, 45))
			if slidechanged != optionssettings:
				slidesound.play()
				slidechanged = optionssettings
			if ymouse >= 5 and ymouse <= 80:
				if xmouse >= 250 and xmouse <= 750:
					if mouseclicked == 1:
						screen.blit(sliderset, (xmouse-5, 5))
					if xmouse >= 435 and xmouse <= 545:
						if mouseclicked == 1:
							screen.blit(sliderset, (xmouse-5, 5))
							setxpos = set1x
							optionssettings = 1
							
					if xmouse >= 250 and xmouse <= 435:
						if mouseclicked == 1:
							screen.blit(sliderset, (xmouse-5, 5))
							setxpos = set2x
							optionssettings = 2
							
					if xmouse >= 545 and xmouse <= 750:
						if mouseclicked == 1:
							screen.blit(sliderset, (xmouse-5, 5))
							setxpos = set3x
							optionssettings = 3
							
				else:


					# BORDS

					if xmouse <= 250:
						if mouseclicked == 1:
							screen.blit(sliderset, (250, 5))
							setxpos = set2x
					elif xmouse >= 750:
						if mouseclicked == 1:
							screen.blit(sliderset, (735, 5))
							setxpos	= set3x

			if mouseclicked == 0:
				screen.blit(sliderset, (setxpos, 5))

			if optionssettings == 2:
				screen.blit(controlsettings, (250, 150))

			if optionssettings == 1:
				screen.blit(descsettings, (250, 150))
				if soption1 == True:
					screen.blit(toggle_on, (680, 180))
				elif soption1 == False:
					screen.blit(toggle_off, (680, 180))
				if soption2 == True:
					screen.blit(toggle_on, (680, 290))
				elif soption2 == False:
					screen.blit(toggle_off, (680, 290))
				if soption3 == True:
					screen.blit(toggle_on, (680, 400))
				elif soption3 == False:
					screen.blit(toggle_off, (680, 400))


				if xmouse >= 680 and xmouse <= 705:
					if ymouse >= 180 and ymouse <= 180+42:
						if mouseclicked == 1:
							if soption1 == True:
								soption1 = False
								mouseclicked = 0
								offsound.play()
							elif soption1 == False:
								soption1 = True
								mouseclicked = 0
								onsound.play()

					elif ymouse >= 290 and ymouse <= 290+42:
						if mouseclicked == 1:
							if soption2 == True:
								soption2 = False
								mouseclicked = 0
								offsound.play()
							elif soption2 == False:
								soption2 = True
								mouseclicked = 0
								onsound.play()

					elif ymouse >= 400 and ymouse <= 400+42:
						if mouseclicked == 1:
							if soption3 == True:
								soption3 = False
								mouseclicked = 0
								offsound.play()
							elif soption3 == False:
								soption3 = True
								mouseclicked = 0
								onsound.play()

	screen.blit(transition, (0, transitiony))

	if settingspagebackgroundoff == 1:
		if settingspage == 1:
			settingspage = 0
		if settingsbgy > -600:
			settingsbgy-=6
		elif settingsbgy <= -600:
			menutwoclickable = 1
			menutwo = 1
			settingspagebackgroundoff = 0

	# DÉBUT DU JEU

	if startinggame == 1:

		if transitiony < -2:
			transitiony+=5
		elif transitiony >= -2:
			mainmenusound.stop()
			startinggame = 0
			enteringgame = 1
			transparencelogo = 0

		menuone = 0
		menutwo = 0

	if enteringgame == 1:
		dreamland.set_alpha(transparencelogo)
		screen.blit(dreamland, (250, 250))
		if transpaanimtwo == 0:
			if transparencelogo <= 255:
				transparencelogo+=0.3
			elif transparencelogo >= 255 and transparencelogo <= 255.3:
				transparencelogo+=0.3
			elif transparencelogo > 255.3 and transparencelogo <= 580:
				transparencelogo+=0.3
			elif transparencelogo >= 580:
				transparencelogo = 255
				transpaanimtwo = 1
				enteringgame = 0
				enteringgamelspart = 1





# QUITTER LE JEU

	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

		if event.type == pygame.KEYDOWN:
				if ingame == 1:
					if event.key == pygame.K_UP:
						print("K UP")

					if event.key == pygame.K_DOWN:
						print("K DOWN")
							
					elif event.key == pygame.K_w:
						print("AVANCER")

					elif event.key == pygame.K_s:
						print("RECULER")

					elif event.key == pygame.K_SPACE:
						print("SPACE")

				if event.key == pygame.K_ESCAPE:
					print("ESCAPE")
					if settingspage == 1:
						settingspagebackgroundoff = 1

		# MENU -----------------

			# MAIN MENU BUTTON
		if menuone == 1:
			if xmouse >= 20 and xmouse <= 150:
				if ymouse >= 550 and ymouse <= 570:
					mnbtnhover = 1
			else:
				mnbtnhover = 0
		if menutwo == 1:
			if menutwoclickable == 1:
				if xmouse >= 20 and xmouse <= 150:
					if ymouse >= 550 and ymouse <= 570:
						ctsbtnhover = 1
					else:
						ctsbtnhover = 0
					if ymouse >= 500 and ymouse <= 520:
						stsbtnhover = 1
					else:
						stsbtnhover = 0
					if ymouse >= 450 and ymouse <= 470:
						tttbtnhover = 1
					else:
						tttbtnhover = 0
					if ymouse >= 400 and ymouse <= 420:
						plybtnhover = 1
					else:
						plybtnhover = 0

		if event.type == pygame.MOUSEBUTTONUP:
			mouseclicked = 0
			# MENU ------------------
			if menuone == 1:
				if xmouse >= 20 and xmouse <= 150:
					if ymouse >= 550 and ymouse <= 570:
						btnclick.play()
						animbtnone = 1
			if menutwo == 1:
				if menutwoclickable == 1:
					if xmouse >= 20 and xmouse <= 150:
						if ymouse >= 550 and ymouse <= 570:
							btnclick.play()
							print("CREDITS")
						elif ymouse >= 500 and ymouse <= 520:
							btnclick.play()
							print("SETTINGS")
							settingspage = 1
						elif ymouse >= 450 and ymouse <= 470:
							btnclick.play()
							print("TUTORIAL")
						elif ymouse >= 400 and ymouse <= 420:
							playbtnsound.play()
							startinggame = 1

		if event.type == pygame.MOUSEBUTTONDOWN:
			mouseclicked = 1




		elif event.type == pygame.KEYUP:
			print("STOP MOUVEMENT")
			mouvement = 0


		
