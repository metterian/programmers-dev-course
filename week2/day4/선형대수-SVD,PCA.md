# 선형대수-SVD,PCA

## SVD (특이값 분해)

특이값 분해는 주어진 행렬을 아래의 형태를 가지느 세 행렬의 곱으로 나누는 행렬분해 힙니다.

![image-20210430110451057](https://tva1.sinaimg.cn/large/008i3skNgy1gq1jlgxk05j30o009177m.jpg)

이를 그림으로 표현하면 다음과 같다.

![image-20210430110806477](https://tva1.sinaimg.cn/large/008i3skNgy1gq1jov1qo7j30xi07v0v6.jpg)

행령 U, D, T는 그 특성에 따라 다음과 같은 의미가 있습니다.

- $U$ : m차원 회전행렬 (정규직교행렬)
- $D$ : n차원 확대 축소 (확대 축소, 크키(스케일)에 따른 정렬 형태), 주대각성분
- $V$ : n차원 회전행렬 (정규직교행렬)



##### Note

톡잇값 분해 $A = U\sum V^T$에서 $\sum$는 주대각 성분에 톡잇값이 위치하고 나머지 성분은 모두 0인 직사각행렬로, 이러한 행렬을 직사각 대각행렬(rectangular diagonal matrix)이라 한다. 기본적으로 대각행렬은 주대각 성분에만 0이 아닌 값이 허용되는 정방행렬을 말한다



### SVD의 기하학적 의미

그림과 같이 $x$를 먼저 $V^T$에 의해 회전한 후, $\sum$로 확대 또는 축소하고, 다시 $U$에 의해 회전하는 것과 같다. 행렬의 특잇값 $\sigma_1$, $\sigma_2$는 선형변환에서 확대 또 는 축소의 비율을 의미한다 .

![image-20210430111408827](https://tva1.sinaimg.cn/large/008i3skNgy1gq1jv5bskuj30rx06htem.jpg)



j















