import pygame
pygame.init()

# Colours
White = (255, 255, 255)
Black = (0, 0, 0)
Grey = (200, 200, 200)
DarkGrey = (150, 150, 150)
DarkBG = (10, 10, 50)
SemiDarkBG = (20, 20, 75)
LightBG = (25, 25, 120)
colourClear = (0,0,0,0)

# Font
font = pygame.font.SysFont(None, 36)

def draw_shadow(screen, rect, offset=(4, 4), shadow_color=(0, 0, 0, 120), radius=0):
    shadow_rect = pygame.Rect(rect.x + offset[0], rect.y + offset[1], rect.width, rect.height)

    # Draw on an alpha surface so you can have transparent shadows
    shadow_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    pygame.draw.rect(shadow_surface, shadow_color, shadow_surface.get_rect(), border_radius=radius)

    screen.blit(shadow_surface, shadow_rect.topleft)


class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            draw_shadow(screen, self.rect, offset=(4, 4), shadow_color=(0, 0, 0, 100))
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            draw_shadow(screen, self.rect, offset=(4, 4), shadow_color=(0, 0, 0, 50))
            pygame.draw.rect(screen, self.color, self.rect)

        # Draw text
        text_surface = font.render(self.text, True, White)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class Banner:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    
    def draw(self, screen):
        draw_shadow(screen, self.rect, offset=(4, 4), shadow_color=(0, 0, 0, 100))
        pygame.draw.rect(screen, self.color, self.rect)

class TextEl:
    def __init__(self, x, y, width, height, text, numVar):
        self.rect = pygame.Rect(x, y, width, height)
        self.numVar = int(numVar)
        self.originNum = self.numVar
        self.text = text ## adds the number to the end of the string
        self.fullText = self.text + str(self.numVar)

    def draw(self, screen):
        pygame.draw.rect(screen, DarkBG, self.rect)

        if self.originNum != self.numVar:
            self.originNum = self.numVar
            self.fullText = self.text + str(self.numVar) ## adds the number to the end of the string

        # Draw text
        text_surface = font.render(self.fullText, True, White)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)