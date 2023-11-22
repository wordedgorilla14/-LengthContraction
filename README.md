# -LengthContraction
특수상대성이론을 간단하게 시각화 해보았다.

pygame 모듈을 활용.

전제조건:

1.빛의 속도는 어느 관성계에서 관측하던지 동일하게 관측된다. (항상 동일한 속도)

2.“관성계”는 일정한 속도로 달리는 열차와 같이 속도의 변화가 없는 공간이다.

3.이 실험에서 관성계는 ‘박스’(초록색 경계)이다.

4.광속불변의 원리에 기반하였기에 모든 작용은 진공상태에서 발생한다.

5.박스 내부에서의 빛의 이동거리는 Bounce * BoxDistance + (Red_pos or 200 - Red_pos)이다. Bounce가 짝수라면 Red_pos, 홀수라면 (200 - Red_pos)이다.
++[Bounce = 박스 내부에서 빛이 부딪힌 횟수. / BoxDistance = 두 초록색 경계사이의 거리. +BoxDistance는 distance between bars와 같다. / Red_pos는 관성계 내부에서 Red의 마지막 위치이다.]

-관성계 외부에서 움직이는 빛과 관성계 내부에서 움직이는 빛을 관측하는 위치에 따라 비교하여 시간수축에 대해서 알아보자.

작성자의 실험환경: 
-VisualStudioCode
-Window 10, 
-python 3.8
-pip 21.0.1
