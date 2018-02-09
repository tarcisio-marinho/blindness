import pygame



def play(audio):

    pygame.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play(0)

    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)

if __name__ == "__main__":
    play("teste.wav")