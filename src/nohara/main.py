import pygame
from . import data
from . import world
from . import caret
from . import bgtext
from . import input as input_mod

# ============================================================
# Main Loop Helpers
# ============================================================


def init():
    pygame.init()
    screen = pygame.display.set_mode((data.SCREEN_W, data.SCREEN_H))
    pygame.display.set_caption("Nohara — Editor for Field Files (SFFF)")
    bgtext.init_font()
    return screen


def run(screen):
    clock = pygame.time.Clock()

    while data.RUNTIME["running"]:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                data.RUNTIME["running"] = False
            elif ev.type == pygame.KEYDOWN:
                input_mod.handle_keydown(ev)

        screen.fill(world.BG_COLOR)
        world.draw_grid(screen)
        bgtext.draw_bg_text(screen)
        caret.draw_caret(screen)

        pygame.display.flip()
        clock.tick(60)
