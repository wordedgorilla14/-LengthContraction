import pygame
import sys

## 빛의 속도는 어느 관성계에서 관측하든 동일하게 관측됨.
## "관성계"는 일정한 속도로 달리는 열차와 같이 속도의 변화가 없는 공간.

# 초기화
pygame.init()

# 화면 설정
screen_width = 1400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gravity Refraction Simulation")

myFont = pygame.font.SysFont(None, 30) #(글자체, 글자크기) None=기본글자체

# 색상
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# 시뮬레이션 변수
light_speed = 5  # 광속
Object_Xpos = 0 # 빛의 시작 x좌표

# 박스 변수
xT = Object_Xpos
Box_speed = 3 # 박스의 속도 [단 박스의 속도는 빛보다 빠를 수 없음]
vxT = Box_speed
BoxDistance = 150 #박스사이의 거리

# BLUE 시작 위치와 속도 설정
xb = Object_Xpos
yb = screen_height
vxb = light_speed
vxy = light_speed

# RED 시작 위치와 속도 설정
xr = Object_Xpos
yr = screen_height
vxr = light_speed
vxy = light_speed

# 기록
LengthLog_B = 0
LengthLog_R = 0
BounceInt = 0
RealTime = 0
temp = 0 # 시간 임시저장.
decimal = 0 # 시간의 소수부분

# 파란빛이 벽에 닿았는지확인
BluePosCheck = True

clock = pygame.time.Clock()

# 측정 값 출력
def StringOutput(posX, posY, CategoryText, TextPara): 
    myText = myFont.render(str(CategoryText) + str(TextPara), True, black) #(Text, anti-alias, color)
    screen.blit(myText, (posX, posY)) #(글자변수, 위치)
    pygame.display.update()

GetStart = False

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 시작?
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        GetStart = True

    screen.fill(white)
    if GetStart:
        # 이동
        if BluePosCheck:
            xb += vxb
            xr += vxr
            
            #이동 거리 기록
            LengthLog_R = LengthLog_R + abs(vxr)
            LengthLog_B = xb

            # 박스 이동 [박스사이의 거리 : 150]- 상수
            xT += vxT

            # Red 화면 경계처리
            if xr >= int(xT+BoxDistance): #screen_height
                xr = int(xT+BoxDistance)
                vxr = -vxr
                BounceInt = BounceInt + 1

            if xr <= int(xT): #screen_height 
                xr = int(xT)
                vxr = -vxr
                BounceInt = BounceInt + 1
            
            # 시간변수
            RealTime = RealTime + 1
            decimal = decimal + 0.033
            if RealTime%30 == 0:
                temp = RealTime/30
                decimal = 0  

        # Blue 화면 경계 처리
        if xb >= screen_width: #screen_height
            xb = screen_width
            BluePosCheck = False
        else:
            LengthLog_B = LengthLog_B + 1 

    StringOutput(50, 50, "Time : ", round(temp+decimal, 2))
    StringOutput(50, 80, "Bounce : ", BounceInt)
    StringOutput(50, 110, "ExternalObservation_TravelDistanceBlue : ", LengthLog_B)
    StringOutput(50, 140, "ExternalObservation_TravelDistanceRed : ", LengthLog_R)
    StringOutput(1000, 50, "distance between bars : ", BoxDistance)

    pygame.draw.line(screen, green, (int(xT), int(yr*(3/4)-100)), (int(xT), int(yr*(3/4)+100)))
    pygame.draw.line(screen, green, (int(xT+BoxDistance), int(yr*(3/4)-100)), (int(xT+BoxDistance), int(yr*(3/4)+100)))

    #blue ball
    pygame.draw.circle(screen, blue, (int(xb), int(yb/4)), 3)

    #red ball
    pygame.draw.circle(screen, red, (int(xr), int(yr*(3/4))), 3)

    # 디스플레이 설정
    pygame.draw.line(screen, black, (0, screen_height // 2), (screen_width, screen_height // 2))
    #pygame.draw.line(screen, black, (screen_width // 2, 0), (screen_width // 2, screen_height))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()