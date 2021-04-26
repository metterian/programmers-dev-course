# [코딩테스트 연습] 해시(Hash) - 완료하지 못한선수

###### 문제 설명

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.

##### 입출력 예

| participant                                       | completion                               | return   |
| ------------------------------------------------- | ---------------------------------------- | -------- |
| ["leo", "kiki", "eden"]                           | ["eden", "kiki"]                         | "leo"    |
| ["marina", "josipa", "nikola", "vinko", "filipa"] | ["josipa", "filipa", "marina", "nikola"] | "vinko"  |
| ["mislav", "stanko", "mislav", "ana"]             | ["stanko", "ana", "mislav"]              | "mislav" |

##### 입출력 예 설명

예제 #1
"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2
"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3
"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.



## 문제해결

> 적절한 자료구조와 알고리즘 선택 해야한다.
>
> 만약 이름 대신 번호가 주어 졌다면 -> 선형 배열 이지만, 번호 말고 다른것(예: 문자열)로 접근 할 수 있는 좋은 자료구조는 없나요?



### 해시 (Hash)

해쉬는 **키(Key)**와 해시 **테이블**(Hash Table)로 구성된다.

<img src="https://tva1.sinaimg.cn/large/008i3skNgy1gptlcb3hxcj30md0fwmyi.jpg" alt="image-20210423140043692" style="zoom:50%;" />

#### 해쉬 함수(Hash Function)

+ 키를 해시 테이블에 매핑하기 위해서는 해시 함수가 필요하다.

+ 해쉬 테이블의 수를 해시 버킷(hash bucket)이라고 한다.

![image-20210423140208050](https://tva1.sinaimg.cn/large/008i3skNgy1gptldrnwjkj30rs0frtcc.jpg)



#### 충돌(Collision)

해시 값이 같아서 해시가 충돌하는 경우가 생길 수 있다. 이럴 경우 버킷의 갯수를 늘리거나 한다.

![image-20210423140311578](https://tva1.sinaimg.cn/large/008i3skNgy1gptlevhwnyj30q50fv0vs.jpg)



### 코드구현

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





## 추가 설명

### Get()

여기서 사용된 `get()`메소드는 특정한 키의 value를 리턴하는 메소드이다.

#### 문법

```python
dictionary.get(keyname, value)
```

#### Parameter Values

| Parameter | Description                                                  |
| :-------- | :----------------------------------------------------------- |
| *keyname* | Required. The keyname of the item you want to return the value from |
| *value*   | Optional. A value to return if the specified key does not exist. Default value None |

#### Example

```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("price", 15000)

print(x)
```

```python
15000
```

