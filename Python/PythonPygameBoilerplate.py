import pygame # MAKE SURE PYGAME IS INSTALLED

# CLIENT
HEIGHT, WIDTH = 600, 600 # Display size (height x width)
FPS = 60 # Change fps

# DISPLAY
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game in Pygame")


def main():

    # CODE HERE (RUNS ONCE AT START)

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # CODE HERE (UPDATED EVERY FRAME)

        draw_window()

def draw_window():
    # CODE TO UPDATE DISPLAY
    pygame.display.update()

if __name__ == "__main__":
    main()