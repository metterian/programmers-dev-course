## [코딩테스트 연습] 해시(Hash) - 완료하지 못한선수

> 적절한 자료구조와 알고리즘 선택 해야한다.
>
> 만약 이름 대신 번호가 주어 졌다면 -> 선형 배열 이지만, 번호 말고 다른것(예: 문자열)로 접근 할 수 있는 좋은 자료구조는 없나요?



## 해시 (Hash)

해쉬는 **키(Key)**와 해시 **테이블**(Hash Table)로 구성된다.

<img src="https://tva1.sinaimg.cn/large/008i3skNgy1gptlcb3hxcj30md0fwmyi.jpg" alt="image-20210423140043692" style="zoom:50%;" />

### 해쉬 함수(Hash Function)

+ 키를 해시 테이블에 매핑하기 위해서는 해시 함수가 필요하다. 

+ 해쉬 테이블의 수를 해시 버킷(hash bucket)이라고 한다. 

![image-20210423140208050](https://tva1.sinaimg.cn/large/008i3skNgy1gptldrnwjkj30rs0frtcc.jpg)



### 충돌(Collision)

해시 값이 같아서 해시가 충돌하는 경우가 생길 수 있다. 이럴 경우 버킷의 갯수를 늘리거나 한다. 

![image-20210423140311578](https://tva1.sinaimg.cn/large/008i3skNgy1gptlevhwnyj30q50fv0vs.jpg)





```python
from collections import defaultdict
def solution(participant, completion):
    d = defaultdict()
    for x in participant:
        d[x] = d.get(x, 0) + 1

    for x in completion:
        d[x] -= 1

    dnf = [k for k,v in d.items() if v > 0]
    answer = dnf[0]
    return answer
```

