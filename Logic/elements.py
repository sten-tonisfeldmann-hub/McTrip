import pygame
class Timer:
    def __init__(self):
        self.algusaeg = pygame.time.get_ticks()
        self.font = pygame.font.SysFont("Arial", 24, bold=True)
        self.sekundid = 0

    def uuenda(self):
        self.sekundid = (pygame.time.get_ticks() - self.algusaeg) // 1000

    def joonista(self, aken):
        tekst = self.font.render(f"Aeg: {self.sekundid}s", True, (255, 255, 255))
        aken.blit(tekst, (20, 60))

    def reset(self):
        self.algusaeg = pygame.time.get_ticks()
        self.sekundid = 0

class Score:
    def __init__(self):
        self.points = 0
        self.high_score = 0
        self.font = pygame.font.SysFont("Arial", 24, bold=True)

    def lisa_punkte(self, kogus):
        self.points += kogus
        if self.points > self.high_score:
            self.high_score = self.points

    def joonista(self, aken):
        skoor_pind = self.font.render(f"Score: {int(self.points)}", True, (255, 255, 255))
        aken.blit(skoor_pind, (20, 20))

        high_score_pind = self.font.render(f"High Score: {int(self.high_score)}", True, (255, 255, 255))
        aken.blit(high_score_pind, (455, 20))

    def reset(self):
        self.points = 0

class Car:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 90)
        self.kiirus = 7
        self.PUNANE = (191, 12, 12)
        self.MUST = (30, 30, 30)
        self.KLAAS = (173, 216, 230)

    def liiguta(self):
        klahvid = pygame.key.get_pressed()
        if klahvid[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.kiirus
        if klahvid[pygame.K_RIGHT] and self.rect.right < 640:
            self.rect.x += self.kiirus

    def joonista(self, aken, varv=(191, 12, 12)):
        pygame.draw.rect(aken, varv, self.rect, border_radius=8)
        pygame.draw.rect(aken, (30, 30, 30), self.rect, 2, border_radius=8)
        ratta_laius, ratta_korgus = 10, 18
        rattad = [
            (self.rect.x - 2, self.rect.y + 10),
            (self.rect.right - ratta_laius + 2, self.rect.y + 10),
            (self.rect.x - 2, self.rect.bottom - 25),
            (self.rect.right - ratta_laius + 2, self.rect.bottom - 25)
        ]
        for r in rattad:
            pygame.draw.rect(aken, (30, 30, 30), (r[0], r[1], ratta_laius, ratta_korgus), border_radius=3)
        klaasi_varv = (173, 216, 230)
        pygame.draw.rect(aken, klaasi_varv, (self.rect.x + 8, self.rect.y + 20, 34, 15), border_radius=2)
        pygame.draw.rect(aken, klaasi_varv, (self.rect.x + 8, self.rect.bottom - 30, 34, 10), border_radius=2)