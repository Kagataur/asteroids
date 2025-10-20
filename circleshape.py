import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        pass

    def update(self, dt):
       pass

    def rotate(self, dt):
       pass
        
    def collide(self, other_circle):
        d = pygame.Vector2.distance_to(self.position, other_circle.position)
        return d < (self.radius + other_circle.radius)