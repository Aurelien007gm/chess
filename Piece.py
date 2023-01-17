import pygame
class Piece(pygame.sprite.Sprite):
    
    def __init__(self,i,x,y):
        
        poffset = 50
        qoffset = 30
        size = 80
        super().__init__()
        name = "piece" + str(i) + ".png"
        
        self.x = x
        self.y = y
        self.p = poffset + x*size
        self.q = qoffset + (7-y)*size
        self.image = pygame.image.load(name).convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.p,self.q))
        
    def moveTo(self,p,q):
        self.rect = self.image.get_rect(center = (p,q))