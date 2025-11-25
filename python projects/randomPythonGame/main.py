import pygame, sys, json, math, time, gui, assetParser as assets, units

pygame.init()

def drawGui(screen):
    # Set all the dynamic values to update
    assets.creditsText.numVar = assets.credits
    assets.mpText.numVar = assets.manpower

    # Render Assets - background -> foreground
    
    # Banners
    assets.bottomBanner.draw(screen)
    assets.topBanner.draw(screen)

    # Buttons
    assets.countryButton.draw(screen)
    assets.techButton.draw(screen)
    assets.diplomaticButton.draw(screen)

    # Text Elements
    assets.creditsText.draw(screen)
    assets.mpText.draw(screen)

    # Unit create buttons
    assets.infantryButton.draw(screen)
    assets.tankButton.draw(screen)
    assets.artilleryButton.draw(screen)
    assets.aircraftButton.draw(screen)
    assets.navalButton.draw(screen)

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
            if assets.diplomaticButton.is_clicked(event):
                print("Diplomacy button clicked!")

            ## Handles unit creation
            if assets.infantryButton.is_clicked(event):
                units.unitHandler().creationUnit('infantry')
            if assets.tankButton.is_clicked(event):
                units.unitHandler().creationUnit('tank')
            if assets.artilleryButton.is_clicked(event):
                units.unitHandler().creationUnit('artillery')
            if assets.aircraftButton.is_clicked(event):
                units.unitHandler().creationUnit('aircraft')
            if assets.navalButton.is_clicked(event):
                units.unitHandler().creationUnit('naval') 
        # Fill screen
        screen.fill((30, 30, 30))
        screen.blit(background_image, (0, 0))

        # Draw GUI
        drawGui(screen)

        # Update display
        pygame.display.flip()
        clock.tick(60)


pygame.quit()
sys.exit()