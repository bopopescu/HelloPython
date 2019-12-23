import pygame

def main():
    pygame.init()
    screen=pygame.display.set_mode((800,800))
    pygame.display.set_caption('Balls')
    screen.fill((242, 242, 242))
    # ball_image=pygame.image.load(r'D:\PyCharm\PycharmProjects\helloworld\venv\res\home.png')
    # screen.blit(ball_image,(50,50))
    pygame.draw.circle(screen,(255,0,0,),(100,100),30,0)
    pygame.display.flip()
    x, y=50,50
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0,), (x, y), 30, 0)
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 5, y + 5


if __name__ == '__main__':
    main()