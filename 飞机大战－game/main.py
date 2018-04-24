"""
作者：刘琪
时间：18-4-18
题目：
"""
import pygame
from pygame.locals import *
from random import *
import myplane
import enemyplane
import buttle
import time

# 定义敌机数量
small_enemiesnum = 3
mid_enemiesnum = 2
big_enemiesnum = 2
bullet_num = 10

# 创建指定个数的小型敌机，并加入组内
def add_small_enemy(group1,group2,num,bg_rect):
    for i in range(num):
        each = enemyplane.SmallPlane(bg_rect)
        group1.add(each)
        group2.add(each)
# 创建指定个数的中型敌机，并加入组内
def add_mid_enemy(group1,group2,num,bg_rect):
    for i in range(num):
        each = enemyplane.MidPlane(bg_rect)
        group1.add(each)
        group2.add(each)
# 创建指定个数的大型敌机，并加入组内
def add_big_enemy(group1,group2,num,bg_rect):
    for i in range(num):
        each = enemyplane.BigPlane(bg_rect)
        group1.add(each)
        group2.add(each)
# 改变敌机组内敌机速度
def speed_increase(group,inc):
    for e in group:
        e.speed += inc

def main():

    # 初始化游戏
    pygame.init()

    # 游戏窗口
    bg_size = width,height = 480,700
    screen = pygame.display.set_mode(bg_size)
    # 设置标题
    pygame.display.set_caption("飞机大战-v1.0")
    # 加载背景音乐
    bg_music = pygame.mixer.music.load("./sound/game_music.ogg")
    # 调节音量大小
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    # 加载音乐
    bomb_bullet_fly_sound = pygame.mixer.Sound("./sound/bullet.wav")
    bomb_bullet_fly_sound.set_volume(0.1)
    bomb_enemy1_down_sound = pygame.mixer.Sound("./sound/enemy1_down.wav")
    bomb_enemy1_down_sound.set_volume(1)
    bomb_enemy2_down_sound = pygame.mixer.Sound("./sound/enemy2_down.wav")
    bomb_enemy2_down_sound.set_volume(1)
    bomb_enemy3_down_sound = pygame.mixer.Sound("./sound/enemy3_down.wav")
    bomb_enemy3_down_sound.set_volume(1)
    bomb_bigenemy_down_sound = pygame.mixer.Sound("./sound/enemy3_flying.wav")
    bomb_bigenemy_down_sound.set_volume(0.3)
    bomb_myplane_down_sound = pygame.mixer.Sound("./sound/me_down.wav")
    bomb_myplane_down_sound.set_volume(0.3)
    # 背景图片
    bg_image = pygame.image.load("./images/background.png").convert_alpha()


    # Game Over　结束游戏
    game_over = pygame.image.load('./images/gameover.png').convert_alpha()
    game_rect = game_over.get_rect()
    #　Game again重新开始
    again_image = pygame.image.load("./images/again.png").convert_alpha()
    again_rect = again_image.get_rect()

    #暂停按钮图片
    paused = False
    paused_nor_image = pygame.image.load("./images/pause_nor.png")
    paused_pressed_image = pygame.image.load("./images/pause_pressed.png")
    resume_nor_image = pygame.image.load("./images/resume_nor.png")
    resume_pressed_image = pygame.image.load("./images/resume_pressed.png")
    paused_image = paused_nor_image
    paused_rect = paused_image.get_rect()
    paused_rect.left,paused_rect.top = width - paused_rect.width - 10,10
    paused_flag = False

    #实例化我方飞机，子弹，敌机
    my_plane = myplane.HeroPlane(bg_image.get_rect())

    #　控制图片切换速度
    deply = 0
    change_img = False

    #设置刷新速度
    clock = pygame.time.Clock()
    running = True


    # 定义一个敌机组
    enemies = pygame.sprite.Group()

    # 生成三个敌机组,大　中　小
    small_enemies =  pygame.sprite.Group()
    mid_enemies   =  pygame.sprite.Group()
    big_enemies   =  pygame.sprite.Group()

    #实例化小敌机组
    add_small_enemy(small_enemies,enemies,small_enemiesnum,bg_image.get_rect())
    # 实例化中敌机组
    add_mid_enemy(mid_enemies,enemies,mid_enemiesnum,bg_image.get_rect())
    # 实例化大敌机组
    add_big_enemy(big_enemies,enemies,big_enemiesnum,bg_image.get_rect())

    # 销毁索引
    small_index = 0
    mid_index = 0
    big_index = 0
    me_index = 0
    bullet_index=0

    # 实例化子弹对象
    bullet_group = pygame.sprite.Group()
    bulletlist = []
    for i in range(bullet_num):
        b = buttle.Bulletmyplane(my_plane.rect.midtop)
        bullet_group.add(b)
        bulletlist.append(b)

    #　生命数量
    life_image = pygame.image.load('./images/life.png')
    life_rect = life_image.get_rect()
    life_num = 3

    # 全屏炸弹
    bomb_img = pygame.image.load("./images/bomb.png").convert_alpha()
    bomb_rect = bomb_img.get_rect()
    bomb_rect.left,bomb_rect.top = (5,height-bomb_rect.height-5)
    bom_num = 3
    fnt2 = pygame.font.Font("./font/myfont.ttf",48)

    # 补给炸弹
    bombs_image = pygame.image.load("./images/bomb_supply.png").convert_alpha()
    bombs_rect = bombs_image.get_rect()

    # 设置显示分数
    score = 0

    # font对像　屏幕上写字用到
    fnt = pygame.font.Font('./font/myfont.ttf',30)
   # 设置大、中、小飞机数量，速度,等级分数
    num1, num2, num3 = 0, 0, 0
    smallspeed, midspeed, bigspeed = 0, 0, 0
    level = 1
    myscore = 50000


    # 按键控制
    step = 3
    move = {K_UP: 0, K_DOWN: 0, K_LEFT: 0, K_RIGHT: 0}
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(1)
            if event.type == MOUSEBUTTONDOWN:
                # 判断鼠标左键，并在按钮区域
                if event.button==1 and paused_rect.collidepoint(event.pos):
                    paused_flag = not paused_flag
            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused_flag:
                        #　暂停
                        paused_image = resume_pressed_image
                    else:
                        paused_image = paused_pressed_image
                else:
                    if paused_flag:
                        paused_image = resume_nor_image
                    else:
                        paused_image = resume_nor_image
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    # 放炸弹
                    for e in enemies:
                        if e.alive and e.rect.top>0:
                            e.alive = False
                    bom_num -= 1


        # 画背景图片
        screen.fill((255, 255, 255))
        screen.blit(bg_image, bg_image.get_rect())
        if not paused_flag:
            # 判断等级
            if level == 1 and score > myscore:
                level =+ 1
                add_small_enemy(small_enemies,enemies,num1+3,bg_image.get_rect())
                add_mid_enemy(mid_enemies,enemies,num2+2,bg_image.get_rect())
                add_big_enemy(big_enemies,enemies,num3+1,bg_image.get_rect())
                myscore += 100000
                speed_increase(small_enemies,smallspeed+1)
                speed_increase(mid_enemies,midspeed+0.7)
                speed_increase(big_enemies,bigspeed+0.4)
                smallspeed += 1
                bigspeed += 0.4
                midspeed += 0.7

            # 频繁按键
            pressedkeys = pygame.key.get_pressed()
            if pressedkeys[K_LEFT]:
                my_plane.move_left()
            elif pressedkeys[K_RIGHT]:
                my_plane.move_right()
            elif pressedkeys[K_UP]:
                my_plane.move_up()
            elif pressedkeys[K_DOWN]:
                my_plane.move_down()

            # 子弹重置
            if not deply%10:
                bulletlist[bullet_index].reset(my_plane.rect.midtop)
                bullet_index = (bullet_index+1)%bullet_num

            #绘制子弹
            for d in bullet_group:
               # bomb_bullet_fly_sound.play()
                if d.alive:
                    d.move()
                    screen.blit(d.image,d.rect)
                    #判断子弹相撞
                    collide_bullet = pygame.sprite.spritecollide(d,enemies,False,\
                                                         pygame.sprite.collide_mask)
                    for e in collide_bullet:
                       if e in small_enemies:
                           score += 1000
                           e.alive = False
                       else:
                           e.energy -= 1
                           if e.energy == 0:
                               if e in big_enemies:
                                   score += 10000
                               else:
                                   score += 5000
                               e.alive = False
                       d.alive = False
            # 绘制敌方飞机
            for e in big_enemies:
                if e.alive:
                    e.move()

                    if deply%4 ==0:
                        screen.blit(e.image1,e.rect)
                    else:
                        screen.blit(e.image2,e.rect)
                    # 绘制血槽
                    pygame.draw.line(screen,(0,0,0),(e.rect.left,e.rect.top-5),\
                                                    (e.rect.right,e.rect.top-5),2)
                    #　剩余血量
                    current_egy = e.energy / enemyplane.BigPlane.energy
                    if current_egy < 0.2:
                        color_paint = (255,0,0)
                    else:
                        color_paint = (0,255,0)
                    pygame.draw.line(screen, color_paint, (e.rect.left, e.rect.top-5), \
                                     (e.rect.left + e.rect.width * current_egy, e.rect.top - 5), 2)

                else:
                    screen.blit(e.destroy_images[big_index],e.rect)
                    if deply%3 == 0:
                        bomb_enemy3_down_sound.play(-1)
                        big_index += 1
                        if big_index == 5:
                            bomb_enemy3_down_sound.stop()
                            big_index = 0
                            e.reset()

            for e in mid_enemies:
                if e.alive:
                    e.move()
                    screen.blit(e.image1,e.rect)
                    # 绘制血槽
                    pygame.draw.line(screen, (0, 0, 0), (e.rect.left, e.rect.top - 5), \
                                     (e.rect.right, e.rect.top - 5), 2)
                    # 剩余血量
                    current_egy = e.energy / enemyplane.MidPlane.energy
                    if current_egy < 0.2:
                        color_paint = (255,0,0)
                    else:
                        color_paint = (0,255,0)
                    pygame.draw.line(screen, color_paint, (e.rect.left, e.rect.top - 5), \
                                     (e.rect.left+e.rect.width * current_egy, e.rect.top - 5), 2)
                else:
                    screen.blit(e.destroy_images[mid_index],e.rect)
                    if deply % 3==0:
                        bomb_enemy2_down_sound.play(-1)
                        mid_index += 1
                        if mid_index==4:
                            bomb_enemy2_down_sound.stop()
                            mid_index=0
                            e.reset()

            for e in small_enemies:
                if e.alive:
                    e.move()
                    screen.blit(e.image1,e.rect)
                else:
                    screen.blit(e.destroy_images[small_index],e.rect)
                    if deply%3 == 0:
                        bomb_enemy1_down_sound.play(-1)
                        small_index += 1
                        if small_index==4:
                            bomb_enemy1_down_sound.stop()
                            small_index = 0
                            e.reset()


        # 检测飞机相撞
        collide_plane = pygame.sprite.spritecollide(my_plane,enemies,False,pygame.sprite.collide_mask)
        if collide_plane:
            #　发生碰撞
            for e in collide_plane:
                e.alive = False
                my_plane.alive = False

        # 显示文字
        myrender = fnt.render("Score:%d"%score,True,(43,24,250))

        #显示等级文字
        screen.blit(myrender,(5,5))
        myrender = fnt.render("level:%d"%level,True,(234,23,56))
        screen.blit(myrender,(width-myrender.get_rect().width-200,\
                              height-myrender.get_rect().height-10))
        # 显示炸弹
        if bom_num > 0:
            screen.blit(bomb_img,bomb_rect)
            myrender = fnt2.render("x %d"%bom_num,True,(234,23,56))
            screen.blit(myrender,(bomb_rect.right+2,bomb_rect.top))

        # 随机出现炸弹

        # 实现飞机动态
        if my_plane.alive:
            if not change_img:
                screen.blit(my_plane.image1, my_plane.rect)
            else:
                screen.blit(my_plane.image2, my_plane.rect)
        else:
            screen.blit(my_plane.destroy_images[me_index],my_plane.rect)
            if not deply%10:
                bomb_myplane_down_sound.play(-1)
                me_index += 1
                if me_index==4:
                    bomb_myplane_down_sound.stop()
                    life_num -= 1
                    me_index = 0
                    my_plane.reset(bg_size)

        if life_num == 0:

            pygame.mixer.music.stop()
            pygame.mixer.stop()
            for e in enemies:
                e.alive = False
            for b in bullet_group:
                b.alive = False

            game_rect.left,game_rect.top = (width - game_rect.width) / 2, 400

            screen.blit(game_over,game_rect)
            again_rect.left,again_rect.top = (width - again_rect.width)/2, 300

            screen.blit(again_image,again_rect)
            # 检测用户鼠标操作
            if pygame.mouse.get_pressed()[0]:
                #获取鼠标坐标
                pos = pygame.mouse.get_pos()
                # 用户点击重新开始
                if again_rect.left < pos[0] < again_rect.right and\
                    again_rect.top < pos[1] < again_rect.bottom:
                    pygame.mixer.music.play()
                    pygame.mixer.music.rewind()
                    for e in enemies:
                        e.alive = True
                    for b in bullet_group:
                        b.alive = True
                    main()
                elif game_rect.left < pos[0] < game_rect.right and\
                    game_rect.top < pos[1] < game_rect.bottom:
                    # 退出游戏
                    pygame.quit()
                    exit(1)
            # 画生命值
        if life_num:
            for i in range(life_num):
                screen.blit(life_image, \
                        (width - 10 - (i + 1) * life_rect.width, \
                        height - 10 - life_rect.height))

        # 绘制暂停开始
        screen.blit(paused_image, paused_rect)
        deply += 1
        if deply % 5 == 0:
            change_img = True
        else:
            change_img = False

        # 刷新
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
