import sys, pygame
pygame.init()

size = width, height = 1080, 760
black = 0, 0, 0

screen = pygame.display.set_mode(size)

y = 350

castle = pygame.image.load("Base1.5.png")
castlerect = castle.get_rect()
castlerect.x = 500
castlerect.y = y

mob = pygame.image.load("Monstre1.5.png")
mobrect = mob.get_rect()
mobrect.x = 0
mobrect.y = 425

fast = pygame.image.load("fast1.png")
fastrect = fast.get_rect()
fastrect.x = 1080
fastrect.y = 350

explosion = pygame.image.load("explosion1.5.png")
explosionrect = explosion.get_rect()
explosionrect.x = 500
explosionrect.y = 350

tower = pygame.image.load("tower.png")
towerrect = tower.get_rect()
towerrect.y = 350
tower_vis = False


alive = True

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            # pos = [234, 500]
            pos = pygame.mouse.get_pos()
            towerrect.x = pos[0]
            tower_vis = True
        

    

    if not alive:
        continue
    screen.fill(black)
    screen.blit(castle, castlerect)

    if tower_vis == True:
        screen.blit(tower,towerrect)

    mobs_list = [mobrect, fastrect]
    collision = pygame.Rect.collidelist(castlerect, mobs_list)
    
    if collision == -1 :

        
        mobrect = mobrect.move([1, 0])
        fastrect = fastrect.move([-1, 0])
        screen.blit(mob, mobrect)
        screen.blit(fast,fastrect)
        
    else :
        
        screen.blit(explosion, explosionrect)
        alive = False

   
   
    pygame.display.flip()