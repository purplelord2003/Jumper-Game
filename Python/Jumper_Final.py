import pygame
from random import randint, choice
from sys import exit
import os

# class that inherits from another class
class Player(pygame.sprite.Sprite):
    screen_down = 1
    def __init__(self):
        super().__init__()
        # loading of player images
        self.player_walk = []
        for file_name in os.listdir('graphics/'):
            if file_name.startswith('p1_walk'):
                path = os.path.join('graphics', file_name)
                image = pygame.image.load(path).convert_alpha()
                self.player_walk.append(image)
        
        # loading of audio
        self.jump_sound = pygame.mixer.Sound('audio/audio_jump.mp3')
        self.jump_sound.set_volume(0.2)

        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/p1_jump.png').convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (260, 500))
        self.gravity = 0
        self.standing_on_ground = True
        self.standing_on_obstacle = False
        self.moving = False
        self.jump_counter = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 4
            self.moving = True
        if keys[pygame.K_RIGHT]:
            self.rect.x += 4
            self.moving = True
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.moving = False

    def jump(self):
        if (self.standing_on_ground or self.standing_on_obstacle) and self.jump_counter == 0:
            self.gravity = -20
            self.jump_sound.play()
            self.jump_counter = 1
        elif self.jump_counter == 1:
            self.gravity = -20
            self.jump_sound.play()
            self.jump_counter = 2
    
    def update_jump_counter(self):
        if self.standing_on_ground or self.standing_on_obstacle:
            self.jump_counter = 0
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += (self.gravity + screen_down)

        if self.rect.bottom >= ground_rect.y:
            self.rect.bottom = ground_rect.y
            self.standing_on_ground = True
            self.gravity = 0
        else:
            self.standing_on_ground = False
    
    def animation_state(self):
        if self.standing_on_ground or self.standing_on_obstacle:
            if self.moving == True:
                self.player_index += 0.5
            else:
                self.player_index = 0

            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
        else:
            self.image = self.player_jump

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.update_jump_counter()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    screendown = 1
    def __init__(self, type):
        super().__init__()
        self.type = type
        if type == 'ice':
            self.image = pygame.image.load('graphics/ice.png').convert_alpha()

        elif type == 'lava':
            self.image = pygame.image.load('graphics/lava.png').convert_alpha()

        else:
            self.image = pygame.image.load('graphics/platform.png').convert_alpha()

        if type == 'default1':
            self.rect = self.image.get_rect(bottomleft = (randint(0, 504), 350))
            
        elif type == 'default2':
            self.rect = self.image.get_rect(bottomleft = (randint(0, 504), 200))
        
        elif type == 'default3':
            self.rect = self.image.get_rect(bottomleft = (randint(0, 504), 50))
    
        elif type == 'default4':
            self.rect = self.image.get_rect(bottomleft = (randint(0, 504), -100))

        elif type == 'lava':
            self.rect = self.image.get_rect(bottomleft = (randint(0, 204), -101))
        
        elif type == 'platform_when_lava':
            self.rect = self.image.get_rect(bottomleft = (randint(300, 504), -101))

        else:
            self.rect = self.image.get_rect(bottomleft = (randint(0, 504), -100))
        
        self.ice_direction = 'right'

    
    def destroy(self):
        if self.rect.y >= 800:
            self.kill()

    def update(self):
        self.rect.y += screen_down
        if self.type == 'ice':
            if self.ice_direction == 'right':
                self.rect.x += 3
                if self.rect.right >= 600:
                    self.ice_direction = 'left'
            else:
                self.rect.x -= 3
                if self.rect.left <= 0:
                    self.ice_direction = 'right'
            
        self.destroy()

def collision_sprite():
    player.sprite.standing_on_obstacle = False
    collision_list = pygame.sprite.spritecollide(player.sprite, obstacle_group, False)
    if collision_list:
        for i in collision_list:
            if i.type == 'lava':
                return False
            else:
                if player.sprite.rect.clipline((i.rect.left + 10, i.rect.bottom), (i.rect.right - 5, i.rect.bottom)) and player.sprite.gravity <= 0:
                    player.sprite.rect.top = i.rect.bottom

                if player.sprite.rect.clipline((i.rect.left + 10, i.rect.top), (i.rect.right - 5, i.rect.top)) and player.sprite.gravity >= 0:
                    player.sprite.rect.bottom = i.rect.top
                    player.sprite.standing_on_obstacle = True
                    player.sprite.gravity = 0
                    if i.type == 'ice':
                        if i.ice_direction == 'right':
                            player.sprite.rect.x += 3
                        else:
                            player.sprite.rect.x -= 3

                if player.sprite.rect.clipline((i.rect.left - 10, i.rect.top + 5), (i.rect.left - 10, i.rect.bottom - 5)):
                    player.sprite.rect.right = i.rect.left

                if player.sprite.rect.clipline((i.rect.right + 5, i.rect.top + 5), (i.rect.right + 5, i.rect.bottom - 5)):
                    player.sprite.rect.left = i.rect.right 

                return True
    return True

def display_score(max_score):
    height_jumped = (ground_rect.top - player.sprite.rect.bottom) / 100
    if height_jumped > max_score:
        max_score = height_jumped
    score_surf = font.render(f'Score: {int(max_score)} m', False, '#FF2400')
    score_rect = score_surf.get_rect(topleft = (10, 10))
    
    screen.blit(score_surf, score_rect)
    return max_score


pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Jumper')
clock = pygame.time.Clock()
font = pygame.font.Font('fonts/nasalization-rg.otf', 30)
game_active = False 
screen_down = 1
max_score = 0
start_time = 0

# Music
intro_music = pygame.mixer.Sound('audio/intro.wav')
intro_music.set_volume(0.05)
stage1_music = pygame.mixer.Sound('audio/Stage 1.wav')
stage1_music.set_volume(0.2)
stage2_music = pygame.mixer.Sound('audio/Stage 2.wav')
stage2_music.set_volume(0.2)
stage3_music = pygame.mixer.Sound('audio/Stage 3.wav')
stage3_music.set_volume(0.2)
death_music = pygame.mixer.Sound('audio/death.mp3')
death_music.set_volume(0.4)

#Groups
player = pygame.sprite.GroupSingle()
obstacle_group = pygame.sprite.Group()

sky_surf = pygame.image.load('graphics/sky.jpg').convert_alpha()

ground_surf = pygame.image.load('graphics/ground.png').convert_alpha()
ground_rect = ground_surf.get_rect(topleft = (0, 500))

# Intro Page
player_intro = pygame.image.load('graphics/p1_jump.png').convert_alpha()
player_intro = pygame.transform.scale2x(player_intro)
player_intro_rect = player_intro.get_rect(center = (300, 300))
titlefont = pygame.font.Font('fonts/nasalization-rg.otf', 50)
gamename = titlefont.render('Jumper', False, (135, 45, 6))
gamename_rect = gamename.get_rect(center = (300, 100))
textfont = pygame.font.Font('fonts/nasalization-rg.otf', 40)
gametext = textfont.render('Press space to jump!', False, (135, 45, 6))
gametext_rect = gametext.get_rect(center = (300, 500))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 0)

speed_timer = pygame.USEREVENT + 2
pygame.time.set_timer(speed_timer, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.sprite.jump()

            if event.type == obstacle_timer:
                obstacle_chosen = choice(['platform', 'ice', 'lava'])
                if obstacle_chosen == 'lava':
                    obstacle_group.add(Obstacle('lava'))
                    obstacle_group.add(Obstacle('platform_when_lava'))
                else:
                    obstacle_group.add(Obstacle(obstacle_chosen))

            if event.type == speed_timer:
                screen_down += 1
                Obstacle.screendown += 1
                Player.screen_down += 1
                pygame.event.post(pygame.event.Event(obstacle_timer))
                pygame.time.set_timer(obstacle_timer, int(2500/screen_down))
                if screen_down == 2:
                    stage1_music.stop()
                    stage2_music.play(loops = -1)
                if screen_down == 3:
                    stage2_music.stop()
                    stage3_music.play(loops = -1)
                
            
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                ground_rect = ground_surf.get_rect(topleft = (0, 500))
                pygame.time.set_timer(obstacle_timer, 2500)
                pygame.time.set_timer(speed_timer, 9900)
                game_active = True
                player.add(Player())
                max_score = 0.01
                screen_down = 1
                intro_music.stop()
                stage1_music.play()
              
    if game_active:
        # Background
        screen.blit(sky_surf, (-300, 0))
        
        # Score
        max_score = display_score(max_score)

        # Player dies
        if not collision_sprite() or player.sprite.rect.top > 600:
            pygame.mixer.stop()
            death_music.play()
            if (pygame.time.delay(3000) == 3000):
                obstacle_group.empty()
                player.empty()
                game_active = False
                pygame.event.clear()
            
        player.draw(screen)
        player.update()

        if len(obstacle_group.sprites()) == 0:
            obstacle_group.add(Obstacle('default1'))
            obstacle_group.add(Obstacle('default2'))
            obstacle_group.add(Obstacle('default3'))
            obstacle_group.add(Obstacle('default4'))

        obstacle_group.draw(screen)
        obstacle_group.update()

        # Ground
        screen.blit(ground_surf, ground_rect)
        ground_rect.y += screen_down

    else:
        screen.fill('#53D5FD')
        screen.blit(player_intro, player_intro_rect)
        screen.blit(gamename, gamename_rect)
        intro_music.play(loops = -1)

        if max_score == 0:
            screen.blit(gametext, gametext_rect)
        else:
            scoretext = textfont.render(f'You jumped {int(max_score)} meters!', False, (135, 45, 6))
            scoretext_rect = scoretext.get_rect(center = (300, 500))
            screen.blit(scoretext, scoretext_rect)

    pygame.display.update()
    clock.tick(60)