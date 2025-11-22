import pygame, sys, json, math, time, gui, assetParser as assets

pygame.init()

class main():
    usrData = assets.usrData
    ## Window Vars

    WIDTH, HEIGHT = 1280, 720
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Commandus - Dev Testing")

    # add the clock
    clock = pygame.time.Clock()

    # self.keys[pygame.K_]
    keys = pygame.key.get_pressed()

    background_image = pygame.image.load("your_image.jpg").convert()
    background_image = pygame.transform.scale(background_image, (WIDTH,HEIGHT))

    # Running loop - updates the screen @ 60fps
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if assets.countryButton.is_clicked(event):
                print("Country button clicked!")
            if assets.techButton.is_clicked(event):
                print("Tech button clicked!")
            if assets.nuggetButton.is_clicked(event):
                print('Added 1 credits')
                assets.credits += 1
        # Fill screen
        screen.fill((30, 30, 30))
        screen.blit(background_image, (0, 0))

        # Set all the dynamic values to update
        assets.creditsText.numVar = assets.credits
        assets.mpText.numVar = assets.manpower

        # Render Assets - background -> foreground
        ## Bottom of screen
        assets.bottomBanner.draw(screen)

        ## Top of screen
        assets.topbanner.draw(screen)
        assets.countryButton.draw(screen)
        assets.techButton.draw(screen)
        assets.diplomaticButton.draw(screen)
        assets.creditsText.draw(screen)
        assets.mpText.draw(screen)

        # Update display
        pygame.display.flip()
        clock.tick(60)


pygame.quit()
sys.exit()