import pygame
import random  # Import the random module

class Bullet(object):
    def __init__(self):
        self.img = pygame.image.load("/Users/arsayusufhidayat/Desktop/Desktop - apple’s MacBook Air/robotic/pygame/bullet.png")
        self.img = pygame.transform.scale(self.img, (50, 50))  # Resize the bullet image to 50x50
        self.x = 0
        self.y = 0
        self.x_change = -40  # Increase speed to make the bullet fire faster
        self.cooldown = 0  # Add a cooldown timer for rapid fire
        self.state = "ready"  # "ready" means you can't see the bullet on the screen

    def fire_bullet(self, x, y):
        self.state = "fire"
        self.x = x
        self.y = y

    def move(self):
        if self.state == "fire":
            self.x += self.x_change
            if self.x < 0:  # Reset bullet if it goes off-screen
                self.state = "ready"

    def draw_bullet(self, screen):
        if self.state == "fire":
            screen.blit(self.img, (self.x, self.y))

class Alien(object):
    def __init__(self):
        self.img = pygame.image.load("/Users/arsayusufhidayat/Desktop/Desktop - apple’s MacBook Air/robotic/pygame/alien.jpeg")
        self.img = pygame.transform.scale(self.img, (50, 50))  # Resize the alien image to 50x50
        self.x = 368
        self.y = 50
        self.x_change = 5
        self.y_change = random.choice([-2, 2])  # Random initial vertical movement

    def draw_alien(self, screen, x, y):  # Pass 'screen' as an argument
        screen.blit(self.img, (x, y))

    def move(self):
        self.y += self.y_change
        # Reverse direction if the alien hits the screen boundaries
        if self.y <= 0 or self.y >= 550:  # Assuming screen height is 600
            self.y_change *= -1

class PLayer(object):
    def __init__(self):
        self.img = pygame.image.load("/Users/arsayusufhidayat/Desktop/Desktop - apple’s MacBook Air/robotic/pygame/player.png")
        self.img = pygame.transform.scale(self.img, (123, 74))  # Resize the player image to 123x74
        self.x = 600
        self.y = 10
        self.x_change = 0
        self.y_change = 0
        self.lives = 3

    def draw_player(self, screen, x, y):  # Pass 'screen' as an argument
        screen.blit(self.img, (x, y))

    def move(self):
        self.y += self.y_change

def main_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.y_change = -5  # Move up
                elif event.key == pygame.K_DOWN:
                    player.y_change = 5  # Move down
                elif event.key == pygame.K_SPACE and bullet.state == "ready":
                    bullet.fire_bullet(player.x + 36, player.y)  # Fire bullet from the player's position
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    player.y_change = 0  # Stop moving

        player.move()  # Update player's position
        alien.move()  # Update alien's position
        bullet.move()  # Update bullet's position

        screen.fill((55, 166, 82))  # Fill the screen with green
        screen.blit(background, (0, 0))  # Draw the background image

        # Draw the player
        player.draw_player(screen, player.x, player.y)  # Pass 'screen' to the method
        # Draw the alien
        alien.draw_alien(screen, alien.x, alien.y)  # Pass 'screen' to the method
        # Draw the bullet
        bullet.draw_bullet(screen)

        pygame.display.flip()
        clock.tick(60)  # Limit the frame rate to 60 FPS

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("uhh game")
clock = pygame.time.Clock()

# Background
background = pygame.image.load("/Users/arsayusufhidayat/Desktop/Desktop - apple’s MacBook Air/robotic/pygame/background.JPG")
background = pygame.transform.scale(background, (800, 600))  # Scale the background to fit the screen

pygame.mixer.init()
pygame.mixer.music.load("/Users/arsayusufhidayat/Desktop/Desktop - apple’s MacBook Air/robotic/pygame/songost.mp3")
pygame.mixer.music.play(-1)  # Play the music on loop (-1 means infinite loop)

# Create instances of PLayer, Alien, and Bullet
player = PLayer()
alien = Alien()
bullet = Bullet()

# Run the main loop
main_loop()
pygame.quit()