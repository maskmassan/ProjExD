import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろこうかとん")
    screen_sfc = pg.display.set_mode((1600,900))#surface
    screen_rct = screen_sfc.get_rect() #rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg") #surface
    bgimg_rct = bgimg_sfc.get_rect()#rect
    screen_sfc.blit(bgimg_sfc,bgimg_rct)

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)

        #練習2番
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        pg.display.update()
        clock.tick(1000)






if __name__=="__main__":
    pg.init()
    main()#これから実行するゲームのメインの部分
    pg.quit()
    sys,exit()