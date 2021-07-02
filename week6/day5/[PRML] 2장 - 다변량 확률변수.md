## 들어가며

지금까지 살펴 보았던 이항 분포(Binomial)는 2개의 가능한 변수 중에서 하나를 선택하는 문제였습니다. 이제 부터는 $K$ 개의 가능성 중 하나를 선택하는 문제를 다뤄보고자 합니다.

문제를 간단하게 하기 위해 $K$ 차원의 크기를 가지는 입력변수를 고려해 봅시다. 여기서 하나의 요소를 $x_k$ 로 정의하고, $x_k$ 의 값이 1이라면 나머지 값은 모두 0인 상태로 가정합니다. 예를 들어, $K=6$ 인 상태에서 $x_3 = 1$ 인 경우를 표현하면 다음과 같습니다.
$$
\mathbf{x}=(0,0,1,0,0,0)^{T}
$$
이제 $\sum_{k=1}^{K} x_{k}=1$ 임을 알 수 있습니다. (One-hot). 특정 데이터 $x_k=1$ 일때의 확률의 모수를 $\mu_k$ 라고 정의하고 이를 표현 하면 $p(x_k=1) = \mu_k$ 가 됩니다. 이런식으로 하나의 데이터 $\mathbf{x}$ (데이터 벡터) 에 대한 확률값은 다음과 같이 정의 가능 합니다.
$$
p(\mathbf{x} \mid \boldsymbol{\mu})=\prod_{k=1}^{K} \mu_{k}^{x_{k}}
$$
예를 들어, $x_3 = 1$ 이라고 한다면 $p(x_k=1) = \mu_k$ 를 이용해서 다음과 같이 표현 할 수 있습니다. 
$$
p(x_1 = 9, x_2=1, x_3=0) = \mu_1^{0}\mu_2^{1}\mu_3^{0} = \mu_2
$$
매개변수도 벡터 형태로 표현 가능하므로 $\boldsymbol{\mu}=\left(\mu_{1}, \ldots, \mu_{K}\right)^{T}$ 와 같이 정의 됩니다. ($\mu_{k} \geq 0, \sum_{k} \mu=1$) 앞서 설명한 

**$\mathbf{x}$ 의 기댓값**
$$
\mathrm{E}[\mathbf{x} \mid \boldsymbol{\mu}]=\sum_{\mathbf{x}} p(\mathbf{x} \mid \boldsymbol{\mu})=\left(\mu_{1}, \ldots, \mu_{M}\right)^{T}=\boldsymbol{\mu}
$$

$$
E[\mathbf{x} \mid \boldsymbol{\mu}]=\left[\begin{array}{c}
E\left[x_{1} \mid \mu \right] \\
\vdots \\
E\left[x_{1} \mid \mu\right]
\end{array}\right] =
\left[\begin{array}{c}
\mu_{1} \\
\vdots \\
\mu_{k}
\end{array}\right]=\boldsymbol{\mu}
$$

## 다항변수(Multinomial Variable): 빈도주의 방법

### 가능도 함수

$\mathbf{x}$ 값을 $N$ 번 관찰한 결과 $\mathcal{D}=\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{N}\right\}$ 가 주어졌을 때, 우도 함수는 다음과 같다. 이때 $\mathcal{D}$ 의 형태는 다음과 같이 주어졌습니다. 
$$
\mathcal{D}=\left[\begin{array}{c}
-x_{1}^{T}- \\
-x_{2}^{T}- \\
\vdots\\
-x_{N}^{T}-
\end{array}\right]
$$

$$
p(\mathcal{D} \mid \boldsymbol{\mu})=\prod_{n=1}^{N} \prod_{k=1}^{K} \mu_{k}^{x_{n k}}=\prod_{k=1}^{K} \mu_{k}^{\left(\sum_{n} x_{n k}\right)}=\prod_{k=1}^{K} \mu_{k}^{m_{k}}\\
m_{k}=\sum_{n} x_{n k}
$$

위 식의 $\prod_{k=1}^{K} \mu_{k}^{m_{k}}$ 를 살펴 봅시다. 이는 우리가 이항변수에서 구했던 $P(\mathcal{D} \mid m)=\mu^{m}(1-\mu)^{l}$ 을 일반화 시킨 결과라고 생각 할 수 있습니다.

간단한 예를 살펴보면 다음과 같습니다. 
$$
\mathcal{D}=\left[\begin{array}{lll}
0 & 0 & 1 \\
1 & 0 & 0 \\
0 & 0 & 0 \\
0 & 1 & 0
\end{array}\right]
\begin{array}{l}
x_{1} \\
\vdots \\
\vdots\\
x_{N}
\end{array}
$$
위와 같이 데이터가 주어졌을 때, $p(\mathcal{D}\mid\mu)$ 를 구하면 다음과 같습니다.
$$
\begin{aligned}
p(\mathcal{D}\mid\mu) &= \mu_{3} \times \mu_{1} \times \mu_{1} \times \mu_{2}\\
&=\mu_1^2\mu_2\mu_1
\end{aligned}
$$
다변수 함수로 일반화 된 위 식을 다음과 같은 방법으로 가능도 함수를 구할 수 있습니다. $\mu$ 의 최대가능도 추정치(maximum likelilhood estimate)를 구하기 위해선 $\mu_k$ 의 합이 1이 된다는 조건을 이용해서 $\ln p(\mathcal{D} \mid \mu)$ 를 최대화 시키는 $\mu_k$ 를 구해야 합니다. 이때 라그랑주 승수(Lagrange multiplier) 를 $\lambda$ 를 사용해서 다음을 최대화 시키면 됩니다. 
$$
\sum_{k=1}^{K} m_{k} \ln \mu_{k}+\lambda\left(\sum_{k=1}^{K} \mu_{k}-1\right) \\
\mu_{k}^{M L}=\frac{m_{k}}{N}
$$

### 다항 분포(Multinomial Distribution)

매개변수 $\mu$ 와 전체 관찰 계수 $N$ 이 주어졌을 때 $m_{1}, \ldots, m_{K}$ 의 분포를 다항분포(multinomial distribution) 이라고 하고 다음과 같은 형태를 가진다.
$$
\operatorname{Mult}\left(m_{1}, \ldots, m_{K} \mid \mu, N\right)=\left(\begin{array}{c}
N \\
m_{1} m_{2} \ldots m_{K}
\end{array}\right) \prod_{k=1}^{K} \mu_{k}^{m_{k}}
$$
여기서 정규화(normalized) 계수는 다음과 같습니다
$$
\left(\begin{array}{c}
N \\
m_{1} m_{2} \ldots m_{k}
\end{array}\right)=\frac{N !}{m_{1} ! m_{2} ! \ldots m_{K} !}
$$
$m_k$는 다음과 같은 제약을 따릅니다.
$$
\sum_{k=1}^{K} m_{k}=N
$$

## 디리클레 분포(Dirichlet distribution)

디리클레 분포는 다항분포를 위한 켤레 사전 분포를 의미 합니다. 이항분포에 대한 공액 사전 분포로 베타 분포가 사용 되듯, 다항 분포에 대한 공액 사전 분포로 디리클레 분포가 사용됩니다. 다항 분포의 모수 추정을 위한 모수의 사전 분포로 다음과 같은 형태를 생각하면 됩니다.
$$
p(\boldsymbol{\mu} \mid \boldsymbol{\alpha}) \propto \prod_{k=1}^{K} u_{k}^{a_{k}-1}\\
\begin{aligned}
\text{s.t. }\quad 
&0 \leq \mu_{k} \leq 1\\ 
&\sum_{k} \mu_{k}=1 \\
&\boldsymbol{\alpha}=\left(\alpha_{1}, \ldots, \alpha_{K}\right)^{T}
\end{aligned}
$$
위의 식의 합의 제약으로 인해서 $\mu_k$ 에 대한 분포를 심플렉스 (simplex) 라고 불리우는 방식으로 표현이 가능하다. 심플렉스(simplex)는 $K-1$ 개의 차원으로 이루어진 공간에 정보를 표현 합니다.

예를 $K=3$ 일 때, 심플렉스 샘플은 아래와 같습니다. 

<img src="http://norman3.github.io/prml/images/Figure2.4.png" alt="Figure2.4" style="zoom:22%;" />





