import pygame
from random import randint
from time import sleep
pygame.init() # 初始化pygame
root = pygame.display.set_mode((932, 526)) # 创建窗口
pygame.display.set_caption("小码打字练习生") # 设置title
# 设置背景图片
bg = pygame.image.load(r"C:\Users\Administrator\Desktop\L2-第22课-学生素材-小码打字练习生1\bg.png")
root.blit(bg, (0,0))

transparent_image = pygame.image.load("pp.png")
word_list = [chr(i) for i in range(97,122)] # a-z
random_word_list = [] # 随机字母列表
position_list = [] # 随机(x, y)
font = pygame.font.Font("zh152.ttf",30) # 设置字体
word_y = 150
for i in range(26):
    wordindex = randint(0, 24)
    word = word_list[wordindex] # 获取随机字母
    random_word_list.append(word) # 添加进随机列表
    # 通过索引,设置随机取出的字母的(x,y)
    word_x = randint(230,690)
    word_y -= 50
    position_list.append((word_x, word_y))
### letter
##text = font.render("A",True,(255,255,255))
##root.blit(text, (letter_x, letter_y))
for i in range(len(random_word_list)):
    word = random_word_list[i] # 一次获取一个字母
    text = font.render(word, True, (255,255,255)) # 绘制
    word_x, word_y = position_list[i] # 获取字母的坐标
    # 如果在屏幕的范围内,粘贴字母
    if word_y < 320:
        root.blit(text, (word_x, word_y))
gameover_font = pygame.font.Font("zh152.ttf", 50)
gameover = gameover_font.render("Game Over", True, (255,255,255))
while True:
    root.blit(bg, (0,0))

    for i in range(len(random_word_list)):
        word = random_word_list[i]
        text = font.render(word, True, (255,255,255))
        # 获取当前字母的(x,y)
        word_x,word_y = position_list[i]
        # 根据坐标粘贴字母
        if word_y < 320:
            root.blit(text, (word_x, word_y))
        else:
            root.blit(bg, (0,0))
            root.blit(gameover, (320,220))
            pygame.display.update()
            break
        # ++y
        word_y += 1
        # update(x,y)
        position_list[i] = word_x, word_y
    root.blit(transparent_image, (0,0))
    pygame.display.update() # update

