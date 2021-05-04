# SVD, PCA

## SVD (특이값 분해)

특이값 분해는 주어진 행렬을 아래의 형태를 가지느 세 행렬의 곱으로 나누는 행렬분해 힙니다.

![image-20210430110451057](https://tva1.sinaimg.cn/large/008i3skNgy1gq1jlgxk05j30o009177m.jpg)

이를 그림으로 표현하면 다음과 같다.

![image-20210430110806477](https://tva1.sinaimg.cn/large/008i3skNgy1gq1jov1qo7j30xi07v0v6.jpg)

행령 U, D, T는 그 특성에 따라 다음과 같은 의미가 있습니다.

- $U$ : m차원 **회전행렬** (정규직교행렬)
- $D$ : n차원 **확대 축소** (확대 축소, 크키(스케일)에 따른 정렬 형태), 주대각성분, 내림차순
- $V$ : n차원 **회전행렬** (정규직교행렬)



##### Note

톡잇값 분해 $A = U\sum V^T$에서 $\sum$는 주대각 성분에 톡잇값이 위치하고 나머지 성분은 모두 0인 직사각행렬로, 이러한 행렬을 직사각 대각행렬(rectangular diagonal matrix)이라 한다. 기본적으로 대각행렬은 주대각 성분에만 0이 아닌 값이 허용되는 정방행렬을 말한다

<br>

### SVD의 의미

그림과 같이 $x$를 먼저 $V^T$에 의해 회전한 후, $\sum$로 확대 또는 축소하고, 다시 $U$에 의해 회전하는 것과 같다. 행렬의 특잇값($D$ 의 원소) $\sigma_1$, $\sigma_2$는 선형변환에서 확대 또 는 축소의 증폭 비율을 의미합니다.

- $U$ : 입력 차원인 $R^m$ 공간에서의 회전
- $D$ : 입력 차원인 $R^n$ 공간에 대해 축방향으로 확대 축소한 후, $R^n \rightarrow R^m$ 으로 차원 변환
- $V$ : 입력 차원인 $R^n$ 공간에서의 회전

#### 예제

$$
\begin{aligned}
A_{3 \times 2} \quad &=\quad \quad \quad U_{3 \times 3}  &D_{3 \times 2} \quad &\quad \quad  V_{2 \times 2}^{T} \\
\left[\begin{array}{rr}
2 & 2 \\
-\frac{1}{2} & \frac{1}{2} \\
-2 & -2
\end{array}\right]
&=\left[\begin{array}{rrr}
\frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}} \\
0 & 1 & 0 \\
-\frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}}
\end{array}\right]&
\left[\begin{array}{cc}
4 & \\
& & \frac{1}{\sqrt{2}} \\
& &
\end{array}\right]&\left[\begin{array}{rr}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
-\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}
\end{array}\right]
\end{aligned}
$$

위와 같이 행렬 $A$가 $S,V, D$ 행렬로 분해되어 있고 이를 기하학적으로 표현하면 다음과 같습니다.

![image-20210504120347814](https://tva1.sinaimg.cn/large/008i3skNgy1gq67s2aen0j30yf0a3779.jpg)

SVD의 기하학적 의미란, A라는 행렬이 주어졌을 때, S, V, D의 순서대로 생각 하는 것과 같습니다. 즉, 공간의 회전 -> 확대 축소 -> 공간의 회전으로 이해하는 것이 쉽습니다. 단 회전을 할때 D 행렬이 가지는 의미는 D의 원소가 기저 벡터(Basis vector)가 되고, 그 기저벡터의 방향으로 증폭(스칼라)된다는 의미 입니다. 

<br>

### SVD의 활용

A의 특이값 분해 U, D, V는 각각 열벡터의 순서대로 행렬 A의 열벡터가 어떤 방향으로 **강한 응집성**을 보이고 있는지를 분석한 것입니다.

$U, D, V$ 의 열벡터를 순서대로 $p$개 취한다면, 강한 응집성을 가지는 $p$개의 방향으로 수선의 발을 내린 $A$의 **근사치** $A^\prime$ 를 재구성 할 수 있습니다.

<br>

#### 예제

$$
\begin{aligned}
A_{3 \times 2} \quad &=\quad \quad \quad U_{3 \times 3}  &D_{3 \times 2} \quad &\quad \quad  V_{2 \times 2}^{T} \\
\left[\begin{array}{rr}
2 & 2 \\
-\frac{1}{2} & \frac{1}{2} \\
-2 & -2
\end{array}\right]
&=\left[\begin{array}{rrr}
\frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}} \\
0 & 1 & 0 \\
-\frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}}
\end{array}\right]&
\left[\begin{array}{cc}
4 & \\
& & \frac{1}{\sqrt{2}} \\
& &
\end{array}\right]&\left[\begin{array}{rr}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
-\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}
\end{array}\right]
\end{aligned}
$$

위와 같이 행렬 A가 S,V, D 행렬로 분해되어 있고 이를 기하학적으로 표현하면 다음과 같습니다.

![image-20210504120347814](https://tva1.sinaimg.cn/large/008i3skNgy1gq67s2aen0j30yf0a3779.jpg)

##### 주대각행렬 선택

다음 SVD로 분해된 식의 $D$(**주대각 행렬**)을 살펴 보면 $[4, \frac{1}{\sqrt{2}}]$ 순으로 내림차순으로 대각 행렬이 형성 되어 있습니다. 즉, 이러한 주대각 행렬을 **강한 응집성의 순서**로 볼 수 있습니다. 이를 이용하여 주 대각성분중 4을 취한다고 가정 하면 다음과 같습니다. 즉, 행렬 전체를 취하는 것이 아니라 **근사치로 행렬을 생성**하는 것입니다.
$$
\begin{aligned}
\left[\begin{array}{r}
\frac{1}{\sqrt{2}} \\
0 \\
-\frac{1}{\sqrt{2}}
\end{array}\right] \quad &\left[\begin{array}{ll}
4
\end{array}\right] &\left[\begin{array}{ll}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}
\end{array}\right] &=\left[\begin{array}{rr}
2 & 2 \\
0 & 0 \\
-2 & -2
\end{array}\right] \\
U_{3 \times 1}^{\prime} \quad& D_{1 \times 1}^{\prime} & V_{1 \times 2}^{\prime T} \quad &=\quad \quad A_{3 \times 2}^{\prime}
\end{aligned}
$$
증폭값이 4의 성분만 성분만 취한다는 것은 $V^T$ 행렬에서 1행의 부분과 $U$행렬의 1열을 취한다는 말과 같습니다. 이렇게 부분의 행을 선택하여도 $A^\prime$ 의 차원과 $A$의 차원을 일치 합니다. <u>즉, 어떤 정보가 의미 있게 줄어든 결과를 보이게 됩니다.</u> 이를 그림으로 살펴보면 다음과 같습니다.

![image-20210504121558745](https://tva1.sinaimg.cn/large/008i3skNgy1gq684qog2rj30s108tmz9.jpg)

입력으로  $\begin{bmatrix}1 &0 \\ 0 &1 \end{bmatrix}$ 가 입력으로 주어졌습니다. 이 입력이 $V$ 행렬을 만나게 되면 $\left[\begin{array}{ll}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}
\end{array}\right]$ 의 결과가 나오게 되고, 이는 입력에서 $x$-축 방향으로 수선의 발($y$ 방향의 벡터가 $x$-축을 향하게 됨)을 내린 것과 같은 의미 입니다. (행렬에서 각 행은 각 차원의 축을 의미, 1행-$x$축, 2행-$y$축) 이렇게 얻은 x-축 방향의 값을 주대각성분 크기(4)만큼 증폭(스칼라)하게 됩니다. 이후, S 행렬을 만나게 되면서 $x$-축 방향과 $z$-축 방향으로 회전 하게 됩니다. 

<br>

##### 주대각 원소 선택 전과 비교

주대각 원소를 선택하기 이전의 행렬의 모습은 다음 그림과 같이 입력 벡터인 x벡터와 y 벡터는 행렬 A의 변환 이후에 약간 벌어져 있는 모습이였다.

![image-20210504120347814](https://tva1.sinaimg.cn/large/008i3skNgy1gq6ax2lf8vj30yf0a33z0.jpg)

<br>

하지만, SVD 분해를 통해 주대각 원소중 가장 큰 원소를 선택하여 증폭하게 되면 다음 그림과 같이 x 벡터와 y벡터는 같은 방향 즉, 붙어 있게 된다. 이 말은 이전의 행렬 A의 변환에서 가장 큰(=의미 있는) 변환을 뽑아 변환을 한다는 것이다.

![image-20210504121558745](https://tva1.sinaimg.cn/large/008i3skNgy1gq6azwgm7qj30s108tdg4.jpg)

정리하지면 원래의 행렬 A 변환에서 데이터의 응집성이 가장 높은 방향만 선택 했다는 의미이다.
$$
\begin{aligned}
A \quad \quad \quad \quad &\quad \quad A^\prime\\
\left[\begin{array}{rr}
2 & 2 \\
-\frac{1}{2} & \frac{1}{2} \\
-2 & -2
\end{array}\right]
\; \rightarrow \;
&\left[\begin{array}{rr}
2 & 2 \\
0 & 0 \\
-2 & -2
\end{array}\right]
\end{aligned}
$$
<br>

## 주성분 분석 (PCA: Principa Component Analysis)

> 주성분 분석 (PCA)는 다수의 $n$ 차원 데이터에 대해, 데이터의 중심으로 부터 데이터의 응집력이 좋은 $n$ 개의 직교 방향을 분석하는 방법입니다.
>
> $K$ 개의 $n$차원 데이터 $\left\{\mathbf{x}_{i}\right\}_{i=1}^{K}$ 가 있을 때, 데이터의 중심 $m$과 공분산행렬 $C$는 다음과 같이 구합니다.
> $$
> \mathbf{m}=\frac{1}{K} \sum_{i=1}^{K} \mathbf{x}_{i}, \quad C=\frac{1}{K} \sum_{i=1}^{K}\left(\mathbf{x}_{i}-\mathbf{m}\right)\left(\mathbf{x}_{i}-\mathbf{m}\right)^{T}
> $$



### 주성분 분석의 의미

공분산행렬에 대해 주성분 분석(PCA)은 아래와 같습니다.

![Screen Shot 2021-05-04 at 2.09.48 PM](https://tva1.sinaimg.cn/large/008i3skNgy1gq6bfwrimbj314i09kdgf.jpg)

주성분분석을 통해 얻은 행렬 W, D는 다음과 같은 의미가 있습ㄴ디ㅏ.

- W : n차원 회전 행렬(정규직교행렬)
- D : n차원 확대축소 (확대축소 크기에 따른 정렬 형태)



### 주성분 분석의 활용

PCA는 데이터의 **분산(variance)**을 최대한 보존하면서 서로 직교하는 새 기저(축)를 찾아, 고차원 공간의 표본들을 선형 연관성이 없는 저차원 공간으로 변환하는 기법입니다. 즉, 새로운 기저 축을 찾아 데이터의 근사치를 기저 축으로 나타내는 방식입니다.

![img](https://tva1.sinaimg.cn/large/008i3skNgy1gq6bkbdr1lg30rs0b4anc.gif)

다음과 같이 데이터가 있을 때, 공분산 행렬과 이에 대한 주성분분석(PCA)는 다음과 같습니다.
$$
C=\frac{1}{6}\left[\begin{array}{ll}
28 & 18 \\
18 & 12
\end{array}\right] \approx\left[\begin{array}{lr}
-0.84 & 0.55 \\
-0.55 & -0.84
\end{array}\right]\left[\begin{array}{ll}
6.3 & \\
& 0.55
\end{array}\right]\left[\begin{array}{rr}
-0.84 & -0.55 \\
0.55 & -0.84
\end{array}\right]
$$
위 예제를 살펴보면 W의 행렬은 2개의 열로 구성 되어 있고 각 열은 축소된 차원의 기저를 의미 합니다. 
$$
W_1 = \begin{bmatrix} -0.84 \\ -0.55 \end{bmatrix}, \quad W_2 = \begin{bmatrix} 0.55 \\ -0.84 \end{bmatrix}
$$


