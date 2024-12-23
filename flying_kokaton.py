import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_1 = pg.transform.flip(bg_img, True, False)
    kou_img = pg.image.load("fig/3.png")
    kou_img = pg.transform.flip(kou_img, True, False)
    kou_rct = kou_img.get_rect()
    kou_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        x = 0
        y = 0
        if key_lst[pg.K_UP]:  # 上矢印キーが押されたら
            y += -1
        if key_lst[pg.K_DOWN]:  # 下矢印キーが押されたら
            y += 1 
        if key_lst[pg.K_RIGHT]:
            x += 2
        kou_rct.move_ip(-1+x, 0+y)
        x = -(tmr % 3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img_1, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img_1, [x+4800, 0])
        screen.blit(kou_img, kou_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)
            


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()