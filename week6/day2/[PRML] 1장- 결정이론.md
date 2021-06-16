## 들어가며

우리는 앞장에서 불확실성을 정량화시키고 일관된 수학적 프레임워크를 구성하는 과정을 살펴보았습니다. 이제 Decision 이론을 이용하여 확률 이론을 바탕으로 불확실성이 관여된 상황에서의 최적의 결정 과정을 살펴볼 것입니다.

> **목표** : 입력 **x** 와 이에 대한 타겟 **t** 를 이용하여 새로운 변수 $x_{new}$ 에 대응하는 타겟 값 $t_{new}$ 를 예측할 수 있다.

<br>

### 주의할 점

- 결합 확률(joint probabilty)을 이용하여 이에 대한 정보를 표현한다. $p(\mathbf{x}, \mathbf{t})$
- 학습데이터로 부터 $p(\mathbf{x}, \mathbf{t})$ 를 결정하는 것은 일종의 추론 과정입니다. 
- 추론의 문제 즉, $p(\mathbf{x}, \mathbf{t})$ 를 결정하는 문제는 불확실성에 대한 확률적 표현법으로 기술 하는 과정을 포함 합니다.  
- 이런 <u>확률 정보를 바탕으로 최적의 결정을 내는 것</u>을 바로 **결정이론**(decision theory)의 주제 입니다.



## 결정이론이란?

새로운 $\mathbf{x}$ 가 주어졌을때 확률모델 $p(\mathbf{x}, \mathbf{t})$에 기반해 **최적의 결정**(예: 분류)을 내리는 것을 말합니다.

- 추론단계: 결합확률분포 $p\left(\mathbf{x}, \mathcal{C}_{k}\right)$ 를 구하는 것 ($p\left(\mathcal{C}_{k} \mid \mathbf{x}\right)$ 을 직접 구하는 경우도 있음). 이것만 있으면 모든 것을 구할 수 있습니다.
- 결정단계: 상황에 대한 확률이 주어졌을 때 어떻게 최적의 결정을 내릴 것인지? 추론 단계를 거쳤다면 결정단계는 매우 쉽습니다.

$$
p\left(C_{k} \mid \mathbf{x}\right)=\frac{p\left(\mathbf{x} \mid C_{k}\right) p\left(C_{k}\right)}{p(\mathbf{x})}
$$



### 예제: X-Ray의 이미지로 암 판별

예를 들어 어떤 환자의 X-Ray 결과 $x$ 가 주어졌을 때 $t$ 는 환자의 암(cancer) 여부라 하자. 이 때 $t$의 값이 $C1$ 인 경우 암이고, $C2$ 인 경우 암이 아님을 의미합니다. 그래서 우리는 x-ray 이미지가 주어졌을 때 암의 여부를 분별하고 싶습니다. 이를 수식으로 나타내면 $p\left(C_{k} \mid \mathbf{x}\right)$ 으로 나타낼 수 있고 이를 정리하면 다음과 같습니다. 

- $\mathbf{x}: \mathbf{X}-\operatorname{Ray}$ 이미지

- $C_{1}:$ 암인 경우
- $C_{2}:$ 암이 아닌 경우
-  $p\left(C_{k} \mid \mathbf{x}\right)$ 의 값을 알기 원함

$$
\begin{aligned}
p\left(\mathcal{C}_{k} \mid \mathbf{x}\right) &=\frac{p\left(\mathbf{x}, \mathcal{C}_{k}\right)}{p(\mathbf{x})} \\
&=\frac{p\left(\mathbf{x}, \mathcal{C}_{k}\right)}{\sum_{k=1}^{2} p\left(\mathbf{x}, c_{k}\right)} \\
&=\frac{p\left(\mathbf{x} \mid \mathcal{C}_{k}\right) p\left(\mathcal{C}_{k}\right)}{p(\mathbf{x})} \\
& \propto \text { 우도(likelihood) } \times \text { 사전확률(prior) }
\end{aligned}
$$

- $p\left(C_{k}\right)$ 는 클래스 $C_k$의 사전(prior) 확률 함수
- $p\left(C_{k} \mid \mathbf{x}\right)$ 는 사후(posterior) 확률 함수

우리의 목적은 잘못된 선택을 하게될 가능성을 줄이는 것입니다. (암이 아닌데 암이라고 선택, 암인데 암이 아니라고 선택) 따라서, 직관적으로 **사후(posterior) 확률이 높은 클래스를 선택하는 문제**로 귀결된다



<br>

## 오분류 최소화 (Minimizing the misclassification rate)

앞서 언급했듯 우리의 목적은 어찌보면 잘못된 분류 가능성을 최대한 줄이는 것입니다. 따라서 **모든 $x$ 에 대해서 특정 클래스로 할당시키는 규칙이 필요**합니다. 이런 규칙은 결국 입력공간을 각 클래스 별로 나누는효과를 가지게 됩니다.

- 이렇게 나누어진 공간은 decision region이라고 하고 $R_k$라고 표기한다. 
- decision region을 통해 나누어진 구역의 경계면을 decision boundaries 혹은 decision surfare라고 부릅니다. (결정면, 결정경계)

### 분류 오류 확률 (Probability of Misclassification)

클래스가 잘못 분류될 가능성을 생각해보면, 이것을 하나의 확률식으로 표현이 가능합니다.
$$
\begin{aligned}
p(\mathrm{mis}) &=p\left(x \in \mathcal{R}_{1}, C_{2}\right)+p\left(x \in \mathcal{R}_{2}, C_{1}\right) \\
&=\int_{\mathcal{R}_{1}} p\left(x, C_{2}\right) d x+\int_{\mathcal{R}_{2}} p\left(x, C_{1}\right) d x
\end{aligned}
$$
위 식이 나타내는 의미는 오분류될 확률 값을 모두 합한 확률로, 이를 최소화하는 조건을 세워 모델을 설계해야 합니다. 

![Figure1.24](http://norman3.github.io/prml/images/Figure1.24.png)

위의 그림에서 현재 클래스의 구분선(decision boundary)를 $\hat{x}$  라고 했다고 가정해봅시다. 그러면 $x \geq \widehat{x}$ 영역에서 해당 클래스가 $C_2$ 로 결정되어 집니다. (반대의 경우는 $C_1$ 으로 할당) 이를 색깔로 표현하면 오류의 합은은 파란색, 초록색, 빨강색이 됩니다. 이 색깔들의 영역을 최소화 하는 곳으로 decision boundary가 설정되어야 합니다. 

만약 $\hat{x}$ 를 왼쪽으로 이동하면 초록색 + 파란색의 면적을 그대로 이지만, 빨강색의 영역은 작아지게 됩니다. 따라서 위 그림의 오류를 최소화 하는 방법은 $\hat{x}=x_{0}$ 지점까지 decision boundary를 이동 시킨는 방법 입니다. 

앞서 설명한 수식과 같이 클래스가 오분류 될 가능성을 수식으로 표현 했지만 이는 반대로 제대로(올바르게) 분류될 확률값을 최대화 하는 형태로도 식을 표현해도 문제가 되지 않습니다. 이를 표현하면 다음과 같습니다.
$$
\begin{aligned}
p(\text { correct }) &=\sum_{k=1}^{K} p\left(\mathbf{x} \in \mathcal{R}_{k}, \mathcal{C}_{k}\right) \\
&=\sum_{k=1}^{K} \int_{\mathcal{R}_{k}} p\left(\mathbf{x}, \mathcal{C}_{k}\right) \mathrm{d} \mathbf{x}
\end{aligned}
$$
<br>

## 기대 손실 최소화 (Minimizing the expected loss)

앞서 설명한 내용에 오류가 있지는 않지만, 현실세계의 오분류(misclassification)을 설명하는데는 부족한 점이 있습니다. 

예를 들어, 암(cancer)을 진단 하는 예제에서 오분류를 생각해 봅시다.

- case 1: 암이 아닌데 암인 것으로 판단
- case 2: 암이 맞는데 암이 아닌 것으로 판다 

첫번째 경우보다 두번째 경우가 더 심각한 분류인데, 이렇게 오분류한경우 페털티를 강하게 주고 싶을 것입니다. 이러한 생각에서 나타는 것이 바로 손실 함수라는 개념입니다.

<br>

### 손실함수 (Loss Function)

단순히 오분류의 갯수를 구하는 것이 아니라, Loss라는 개념을 정의하고 이를 최소화 하는 방법을 생각해 봅시다. 이러한 방법을 통해 어떠한 결정에 대해 조금 더 능동적으로 행동을 조절 할 수 있게 됩니다.

개념은 간단합니다. 하나의 샘플 $x$가 실제로는 특정 클래스 $C_k$에 속하지만 우리가 이 샘플의 클래스를 $C_j$로 선택할 때(즉, **잘못된 선택을 한 경우, 오분류) 소요되는 비용을 정의**합니다. 여기서 모든 경우에 대한 Loss 값을 정의한 행렬을 Loss 행렬이라고 합니다. 

#### 수식

실제 Loss 함수를 최소화 하는 방법은 **Loss 함수에 대한 평균값을 최소화 하는 방법**을 사용합니다. 
$$
E[L]=\sum_{k} \sum_{j} \int_{R_{j}} L_{k j} p\left(\mathbf{x}, C_{k}\right) d \mathbf{x}
$$
위의 식 자체를 그냥 오류 함수로 정의 해서 사용하면 됩니다. (최소제곱법을 오류 함수로 사용한 것 처럼). 여기서 $x$ 는 반드시 하나의 $R_j$에 포함되게 됩니다. 따라서 우리는 오류값이 최소가 되는 $R_j$를 선택해야 합니다. 

결론적으로, $x$에 대해 $\sum_{k} L_{k j} p\left(\mathbf{x}, C_{k}\right)$ 를 최소화 하는 클래스를 찾으면 됩니다. $p\left(\mathbf{x}, C_{k}\right)=p\left(C_{k} \mid \mathbf{x}\right) p(\mathbf{x})$ 로 치환이 가능하고. $p(\mathbf{x})$ 는 글래스마다 동일하다고 생각하고 생략합니다. 새로운 $x_{new}$가 들어왔을때, 이 식을 이용하면 됩니다.

<br>

### 예제: 의료진단

다음과 같이 이진분류를 하는 클래스로 구분이 되어 있다고 가정해보자. $C_1$ 의 경우는 아픈 경우를 나타내고, $C_2$의 경우는 건간한 경우를 나타낸다.
$$
\left.C_{k} \in\{1,2\} \Longleftrightarrow \text { sick, healthy }\right\}
$$
이때, Loss 행렬은 다음과 같이 나타낼 수 있습니다. $L[0] = [0,100]$의 의미는 실제 sick을 의미하고, $L[1]=[1,0]$의 의미는 실제 heathly를 의미 합니다. 또한, 첫번째의 행의 의미는 sick이라고 분류한 경우를  나타내고 두번째 행의 경우는 health라고 분류한 경우를 나타냅니다. 
$$
L=\left[\begin{array}{cc}
0 & 100 \\
1 & 0
\end{array}\right]
$$
이때의, 기대손실을 구하면 다음과 같습니다. 즉 Loss 함수에 대한 평균값을 구하면 다음과 같습니다.
$$
\begin{aligned}
\mathbb{E}[L] &=\int_{\mathcal{R}_{2}} L_{1,2} p\left(\mathbf{x}, \mathcal{C}_{1}\right) \mathrm{d} \mathbf{x}+\int_{\mathcal{R}_{1}} L_{2,1} p\left(\mathbf{x}, \mathcal{C}_{2}\right) \mathrm{d} \mathbf{x} \\
&=\int_{\mathcal{R}_{2}} 100 \times\left(\mathbf{x}, \mathcal{C}_{1}\right) \mathrm{d} \mathbf{x}+\int_{\mathcal{R}_{1}} p\left(\mathbf{x}, \mathcal{C}_{2}\right) \mathrm{d} \mathbf{x}
\end{aligned}
$$
<br>

## 회귀를 위한 손실 함수 (Loss functions for regression)

위의 예제에서는 분류(classification)을 위한 결정이론을 살펴보았습니다. 이번에는 회귀(regression)문제에서의 손실함수를 다뤄 봅시다. 여기서 회귀문제의 주요한 특징은 다음과 같습니다. 

> 회귀문제는 분류를 하는 것이 아니라 실수인 타겟을 예측하는 것이다.

<br>

### 기대손실함수 (expected loss function)

회귀문제에서의 기대 손실함수(expected loss function)을 정의 해보면 다음과 같습니다.

- **expected loss** : 주어진 데이터로부터 얻어진 손실 함수의 평균값을 의미

$$
E[L]=\iint L(t, y(\mathbf{x})) p(\mathbf{x}, t) d \mathbf{x} d t
$$



