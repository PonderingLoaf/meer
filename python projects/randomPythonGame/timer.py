import pygame

class RTSTimer:
    def __init__(self):
        self.game_time = 0  # milliseconds of in-game time
        self.paused = False
        self.speed = 1.0    # game speed, 1.0 = normal

    def update(self, dt):
        if not self.paused:
            self.game_time += int(dt * self.speed)

    def get_seconds(self):
        return self.game_time // 1000

    def get_formatted(self):
        total_seconds = self.get_seconds()
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes:02}:{seconds:02}"