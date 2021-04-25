# [코딩테스트연습] 2 x n 타일링

###### 문제 설명

가로 길이가 2이고 세로의 길이가 1인 직사각형모양의 타일이 있습니다. 이 직사각형 타일을 이용하여 세로의 길이가 2이고 가로의 길이가 n인 바닥을 가득 채우려고 합니다. 타일을 채울 때는 다음과 같이 2가지 방법이 있습니다.

- 타일을 가로로 배치 하는 경우
- 타일을 세로로 배치 하는 경우

예를들어서 n이 7인 직사각형은 다음과 같이 채울 수 있습니다.

![Imgur](https://tva1.sinaimg.cn/large/008i3skNgy1gpuzpfz1wbj30by03i0sh.jpg)

직사각형의 가로의 길이 n이 매개변수로 주어질 때, 이 직사각형을 채우는 방법의 수를 return 하는 solution 함수를 완성해주세요.

##### 제한사항

- 가로의 길이 n은 60,000이하의 자연수 입니다.
- 경우의 수가 많아 질 수 있으므로, 경우의 수를 1,000,000,007으로 나눈 나머지를 return해주세요.

------

##### 입출력 예

| n    | result |
| ---- | ------ |
| 4    | 5      |

##### 입출력 예 설명

입출력 예 #1
다음과 같이 5가지 방법이 있다.

![Imgur](https://tva1.sinaimg.cn/large/008i3skNgy1gpuzpg5r8cj306t03g0ij.jpg)

![Imgur](https://tva1.sinaimg.cn/large/008i3skNgy1gpuzphe36rj306t03e0jn.jpg)

![Imgur](https://tva1.sinaimg.cn/large/008i3skNgy1gpuzpgtexlj306t03g0l0.jpg)

![Imgur](https://tva1.sinaimg.cn/large/008i3skNgy1gpuzpidhdwj306t03g0lx.jpg)

![Imgur](https://tva1.sinaimg.cn/large/008i3skNgy1gpuzphv327j306t03g0lh.jpg)





## 코드 풀이

동적 계획법으로 풀 수있는 쉬운 문제 중에 하나이다. 동적 계획법을 풀 때 보통 메모라이제이션(memorization) 혹은 bottom-up 방식을 사용한다. 처음에는 가장 쉬운 bottom-up 방식을 이용해서 풀어 보았다.

```python
def solution(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1000000007
```

이렇게 풀어도 정답은 맞지만, 효율성 체크에서 시간초과가 뜨고 만다. 아마 매우 큰 숫자를 입력했을때 파이썬 리스트의 속도가 느려지는 것 같았다. 

![image-20210424190517888](https://tva1.sinaimg.cn/large/008i3skNgy1gpuzrimmktj30ok05kt97.jpg)



이를 개선 하기 위해 리스트를 사용하지 않는 메모라이제이션 방식을 사용했다 [스택오버플로우](https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series) 에서는 Naive한 방식이라고 소개 되어있었는데 효율성 검사를 잘 통과 할 수 있었다.

```python
def solution(n):
    a,b = 1,2
    for _ in range(n-1):
        a,b = b, a + b
    return a % 1000000007
```

![image-20210424190722458](https://tva1.sinaimg.cn/large/008i3skNgy1gpuztocbxrj30om05nq3i.jpg)



## 추가 기록 - 동적 계획법 

동적 계획법으로 여러가지 방식이 존재한다. [스택오버플로우](https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series) 를 참고 하여, bottom-up, memorization, a naive 한 방식을 설명하고자 한다. 가장 쉬운 예로 피보나치 수열을 예로 들어 본다.

### from the bottom up

가장 쉬운 방식으로 저장된 이전의 값을 사용해서 다음 값을 계산한다.

```python
>>> def fib_to(n):
...     fibs = [0, 1]
...     for i in range(2, n+1):
...         fibs.append(fibs[-1] + fibs[-2])
...     return fibs
```

피보나치 수열 20을 구해보면 다음과 같다.

```python
>>> fib_to(20)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
```



### Memoization

다음은 메모라이제이션 방식이다. bottom-up 방식보다 조금 복잡하지만, 빠르다고 알려져 있다. bottom-up 방식의 문제점은 이미 계산한 값을 다시 계산하는 것이 문제이다. 이를 개선 하기 위해 이미 계산한 값을 어딘가 저장 해놓고 필요할때 다시 사용하는 방식을 메모라이제이션 방식이라고 한다. 

```python
>>> def fib(n, computed = {0: 0, 1: 1}):
...     if n not in computed:
...         computed[n] = fib(n-1, computed) + fib(n-2, computed)
...     return computed[n]
```

