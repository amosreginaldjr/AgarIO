from screeninfo import get_monitors #get monitor size #make sure to 'pip install screeninfo'
import pygame
import random

#user monitor/screen size:
for monitor in get_monitors():
    print("Width: {}, Height: {}".format(monitor.width, monitor.height))
user_screen_width = monitor.width
user_screen_height = monitor.height


    

screen_width = 800
screen_height = 600
print(pygame.display)
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height)) #(width,height)
#screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN, 0) #(width,height) #FULLSCREEN
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('AgarIO') #program window name

class Color:
    def __init__(self):
        try: self.color = str(("#" + (hex(random.randrange(1118481,16777215))[2:]) ))
        except: self.color = str(("#" + (hex(random.randrange(1118481,10000000))[2:]) ))
        #else: self.color = str(("#" + (hex(random.randrange(1118481,10000000))[2:]) ))
        #finally: print("ERROR CODE: C_FAILED")

    def get_color(self): 
        if len(self.color) < 7:
            #print(len(self.color),end="::::::")
            return (self.color + "0")
        return self.color
color = Color()
color_background = Color()
color_player = Color()
color_food = Color()

class Player: 
    def __init__(self):
        self.player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.player_radius = 10
        self.player_default_speed = 5
        self.player_modifyable_speed = self.player_default_speed
        
    def get_player_pos(self):
        return self.player_pos
    
    def spawn_player(self):
        return pygame.draw.circle(screen, color_player.get_color(), player.get_player_pos(), self.player_radius)
player = Player()

class Food:
    def __init__(self):
        food_spawn_max_width = random.randrange(0,screen.get_width())
        food_spawn_max_height = random.randrange(0,screen.get_height())
        self.food_pos = pygame.Vector2(food_spawn_max_width, food_spawn_max_height)
        self.food_color = color_food.get_color()
        
    def spawn_food(self):
        return pygame.draw.circle(screen, self.food_color, self.food_pos, 10)
foodp = Food().food_pos
food = [Food(),Food(),Food(),Food()]

class Score:
    def __init__(self):
        self.score = 0

    def increase_score(self):
        print(self.score)
        self.score += 1
        return self.score
score = Score()

######
main_menu_image = pygame.image.load("Assets/MainMenu.jpg").convert_alpha()
background_image = pygame.image.load("Assets/background.jpeg").convert_alpha()


#Main Menu Buttons:
PLAY = pygame.draw.rect(screen, "green", (75, 150, 25, 25))  #PLAY (window, color, (x, y, width, height))
#pygame.draw.rect(screen, "green", (75, 335, 25, 25))  #NULL
TOGGLE_FS = pygame.draw.rect(screen, "green", (475, 145, 25, 25)) #TOGGLE FS
QUIT = pygame.draw.rect(screen, "green", (470, 335, 25, 25)) #QUIT


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#main menu:
    screen.blit(main_menu_image, (-230,-50))
    
#####################LEFT HERE
    if pygame.event.EventType == pygame.K_5:
        pygame.QUIT
        running = False
       
   
    
    #screen = pygame.display.set_mode((screen_width, screen_height)) #(width,height) #makes resizable screen
#game:
    #screen.blit(background_image, (0,0))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.player_pos.y -= player.player_modifyable_speed
    if keys[pygame.K_s]:
        player.player_pos.y += player.player_modifyable_speed
    if keys[pygame.K_a]:
        player.player_pos.x -= player.player_modifyable_speed
    if keys[pygame.K_d]:
        player.player_pos.x += player.player_modifyable_speed
     
    #pygame.draw.circle(screen, color_player.get_color(), player.get_player_pos(), 20)
    #player.spawn_player()
   
    for i in range(0,4):
        if food[i].spawn_food().colliderect(player.spawn_player()): #spawns food and player
            #food[i].spawn_food()
            food[i].food_pos = (random.randrange(0,screen.get_width()), 
                                random.randrange(0,screen.get_height())) #gives food new position
            player.player_radius += 5 #increases player radius
            food[i].food_color = str(("#" + (hex(random.randrange(1118481,16777215))[2:]) )) #changes food color 
            score.increase_score()
            screen_width += 10
            screen_height += 10
         ####
        if food[i].spawn_food().right >= screen_width or food[i].spawn_food().left >= screen_width  or  food[i].spawn_food().top >= screen_height or food[i].spawn_food().bottom >= screen_height:
           food[i].food_pos = (random.randrange(0,screen.get_width()), random.randrange(0,screen.get_height()))
       
    
    if keys[pygame.K_SPACE] and player.player_radius > 10:
        player.player_radius -= .5
        player.player_modifyable_speed += .5
        screen_width -= 1
        screen_height -= 1
    if keys[pygame.K_SPACE] == 0 or player.player_radius < 11:
        player.player_modifyable_speed = player.player_default_speed
        

    pygame.display.flip()
    clock.tick(60)
pygame.quit()

