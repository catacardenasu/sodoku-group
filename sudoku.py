import pygame

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((513, 680))
        pygame.display.set_caption("Sudoku")
        background_image = pygame.image.load("sudoku_pic.webp")
        background_image = pygame.transform.scale(background_image, (513, 680))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        screen.blit(background_image, (0, 0))
        pygame.display.flip()

        def in_progress():
            pygame.init()
            screen = pygame.display.set_mode((513, 680))
            running = True
            clock = pygame.time.Clock()
            while True:
                # Process player inputs.
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        raise SystemExit
                screen.fill("purple")

                pygame.display.flip()
                clock.tick(60)

    finally:
        raise SystemExit

if __name__ == '__main__':
    main()


