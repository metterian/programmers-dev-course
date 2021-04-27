# 선형대수 - LU 분해

## 행렬분해(matrix decomposition)의 의미

### 인수분해

숫자의 인수 분해는 주어진 숫자(예: 12)를 여러 숫자의 곱으로 분해(예: $3 * 4$)하여 표현 하는 것을 말한다. 이러한 인수 분해는 다음과 같은 상황에서 필요하다

- 분수의 약분
- 두 수의 최대공약수
- 두 수의 최소공배수

예를 들어 $\frac{4}{24}$를 약분 한다고 하면 우리는 간단히 분자와 분모를 4로 나누어 $\frac{1}{6}$ 으로 표현한다. 이때 분모와 분자에 나누어 준 숫자가 바로 인수분해를 통해 얻은 값이다. 가령 이렇게 간단한 분수가 아니라, $\frac{3341234}{23452345}$ 와 같이 매우 복잡 수는 어떻게 약분을 할 수 있을까?

즉, 주어진 숫자를 인수분해 한 상태로 가지고 있으면 여러모로 계산이 편한 경우가 많다.



### 행렬분해

행렬의 경우도 위와 마찬가지이다. 주어진 행렬을 행렬분해 한 상태로 가지고 있으면 여러모로 계산이 편한 경우가 많다.

대표적인 행렬 분해는 다음과 같다.

- LU 분해
- QR 분해
- 특이값 분해(SVD, Singular Value Decomposition)

본 포스팅에서는 LU 분해를 다뤄 보려 한다. 이전에 배운 Gauss 소거법을 행렬로 표현 한 것이 바로 LU 분해 이기 때문이다. 



## LU 분해(LU decomposition)

> 임의의행렬 $A$를 하삼각행렬 $L$과 상삼각행렬 $U$의곱인 $A=LU$로 표현히는것을 **LU 분해** (LU matrix decomposition) 또는 **LU 행렬 분해**라고 한다.

*여기서, L은 Lower trianlguar matrix를 의미하고, U: 는 upper trianlgular matrix를 의미한다.*

![image-20210427152817113](../../../../Library/Application Support/typora-user-images/image-20210427152817113.png)

### LU 분해의 장점

LU 분해의 장점은 다음과 같습니다. LU 분해를 이용해 Ax= b 문제를 아래와 같이 나타내면
$$
Ax = b \Rightarrow (LU)x = b \Rightarrow L(Ux) = b \\
\Rightarrow Ly = b, (단, Ux=y)
$$
위와 같이 나타낼 수 있다. 이렇게 식을 얻게 되면 다음과 같은 두 단계로 간단히 해결 할 수 있다.  Ax=b 라는 문제를 두 개의 작은 문제로 분할 해서 생각 할 수 있다. 위에서 설명한 내용을 정리하면 다음과 같다.

#### Forward-subsitution(전방 대치법) : y 구하기

<img src="https://tva1.sinaimg.cn/large/008i3skNgy1gpyaswz8noj30gz068dgl.jpg" alt="image-20210427154348355" style="zoom:50%;" />

##### $Ly = b$ 

$(LU)x = b$  문제를 한번에 풀지않고, $Ux = y$ 이라고 치환하고, $Ly=b$ 의 식으로 다시 쓸 수 있다. 이 식은 곧 $y$ 를 구하는 문제로 바뀌게 된다.

L의 형태를 보면 Lower Triangular Matrix 형태를 띄고 있다. 즉, 위에서 계산한 미지수를 통해 아래의 선형 방정식을 구해 나갈 수 있다.

#### Back-subsitution(후방 대치법) : x 구하기

<img src="https://tva1.sinaimg.cn/large/008i3skNgy1gpyaumfjygj30h906kdgp.jpg" alt="image-20210427154528451" style="zoom:50%;" />

##### $Ux = y$

위에서 구한 $y$를 통해 $x$를 구할 수 있게 된다.

U의 형태를 보면 upper trianlguar matrix의 형태이다. 이는 Gauss 소거법을 통해 미지수를 구해 나갈 수 있다.



### LU 분해의 의미

> LU 분해는 가우스 소거법의 forward elimination(전방 소거법)을 행렬로 코드화 한 것이다.즉,  가우스 소거법을 진행 할때 복잡한 계산과정(noting)을 코드화 하여 계산이 편하도록 한 것이다.

- L : 행렬 A를 전방소거 하는데 쓰인 replacement와 scaling에 대한 EROs를 기록해 둔 행렬
- U: 행렬 A를 전방소거한 후 남은 upper triangluar matrix(상삼각행렬)
- P: 행렬 A를 전방소거하는데 쓰인 interchange에 대한 EROs를 기록해 둔 행렬(옵션)





### LU 분해의 활용

LU 분해는 다음의 이유로 활용 됩니다.

#### 수치적 안정성

선형 시스템 $Ax =b$의 해를 역행렬 $A^{-1}$를 바로 구하는 것 보다 $PLU$ 분해를 이용하는 것이 더 수치적으로 안정적인 경우가 많다.

#### b가 자주 업데이트 되는 경우

선형 시스템 $Ax=b$에서 행렬 A는 고정되어 있고 $b$가 자주 변하는 문제가 종종 있습니다. 이런경우, 행렬 $A$를 미리 $PLU$로 분해해 둔다면, $b$가 업데이트 될때 마다 선형시스템의 해 $x$를 실시간으로 구할 수 있습니다.











