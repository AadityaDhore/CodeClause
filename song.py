import pygame
pygame.init()
window = pygame.display.set_mode((300, 300))
pygame.mixer.music.load('faded.mp3')
pygame.mixer.music.play()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
# Stop the music and quit the program
pygame.mixer
