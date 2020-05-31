import pygame
import random
import os

# Setup constants
width = 300
height = 600

player_width = 24

class Player(pygame.sprite.Sprite):
    def __init__(self, starting_pos, surface):
        pygame.sprite.Sprite.__init__(self)

        self.image = surface
        self.pos = starting_pos

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def move(self, direction):
        if direction == 'left':
            new_x = self.pos[0]-10
            if new_x < 0:
                new_x = 0
            self.pos = (new_x, self.pos[1])
        if direction == 'right':
            new_x = self.pos[0]+10
            if new_x + player_width > width:
                new_x = width - player_width
            self.pos = (new_x, self.pos[1])


class Stracciatella(pygame.sprite.Sprite):
    def __init__(self, surface):
        pygame.sprite.Sprite.__init__(self)

        self.image = surface
        self.pos = (random.randrange(width-32), 0)

    def draw(self, screen):
        self.pos = (self.pos[0], self.pos[1]+4)
        screen.blit(self.image, self.pos)

class IceGroup(pygame.sprite.Group):
    def __init__(self, *sprites):
        pygame.sprite.Group.__init__(self, *sprites)

    def draw(self, screen):
        for cream in self.sprites():
            cream.draw(screen)

def main():
    pygame.init()

    # Game setup
    logo = pygame.image.load(os.path.join('images', 'bee-logo.png'))
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Bee Game')
    screen = pygame.display.set_mode((width,height))

    # Add and display background
    background = pygame.image.load(os.path.join('images', 'background.png'))
    screen.blit(background, (0,0))
    pygame.display.update()

    # Setup player
    bee = pygame.image.load(os.path.join('images', 'bee.png')).convert_alpha()
    start_pos = (width/2 - player_width/2,height-32)
    player = Player(start_pos, bee)

    # Setup ice-creams
    ice_cream = pygame.image.load(os.path.join('images', 'stracciatella.png')).convert_alpha()
    ice1 = Stracciatella(ice_cream)
    ice_group = IceGroup(ice1)

    # Setup counter for ice-cream spawning
    counter = 0

    running = True
    while running:
        for event in pygame.event.get():
            # If the player quits the game
            if event.type == pygame.QUIT:
                running = False

        # Check key presses
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            player.move('left')
        elif pressed[pygame.K_RIGHT]:
            player.move('right')

        # Do this every loop
        screen.blit(background, (0,0))
        ice_group.draw(screen)
        player.draw(screen)
        pygame.display.update()

        # Count the loops and spawn ice_cream
        counter += 1
        if counter == 20:
            ice_group.add(Stracciatella(ice_cream))
            counter = 0
        pygame.time.wait(10)

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
