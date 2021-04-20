## 연결 리스트(Linked Lists)

> 선형 배열이 "번호가 붙여진 칸에 원소들을 채워넣는" 방식이라고 한다면, 연결 리스트는 "각 원소들을 줄줄이 엮어서" 관리하는 방식입니다.

#### Node
- Data
- Link (next)

Node 내의 데이터는 다른 구조로 이루어질 수 있다.
ex) 문자열, 레코드. 또 다른 연결 리스트 등

### 기본적인 연결 리스트

기본적인 연결 리스트는 **Head**, **Tail**, **number of nodes** 로 구성된다. 

![image-20210420234742311](/Users/seungjun/Library/Application Support/typora-user-images/image-20210420234742311.png)

### 자료 구조 정의

#### Node

node는 data와 link(next)로 구성된다. 이를 Python 클래스로 구현하면 다음과 같다.

```python
class Node:
    def __init__(self, item) -> None:
        self.data = item # item을 받아서 data에 저장
        self.next = None
```

이를 그림으로 표현 하면 다음과 같다.

<img src="/Users/seungjun/Library/Application Support/typora-user-images/image-20210420235129159.png" alt="image-20210420235129159" style="zoom:40%;" />

#### Linked List

처음에 연결리스트를 생성할 때 비어있는 연결리스트를 생성하기 위해서 다음과 같이 초기화를 해준다. 

```python
class LinkedList:
    def __init__(self) -> None:
        self.nodeCount = 0
        self.head = None
        self.tail = None
```

이를 그림으로 표현 하면 다음과 같다.

<img src="/Users/seungjun/Library/Application Support/typora-user-images/image-20210420235345923.png" alt="image-20210420235345923" style="zoom:50%;" />

### 연산 정의

1. 특정 원소 참조 ($k$ 번째)
2. 리스트 순회
3. 길이 얻어내기
4. 원소 삽입
5. 원소 사게
6. 두 리스트 합치기



### 특정 원소 참조

특정 원소를 찾아가는 코드를 구현하면 다음과 같다.

```python
def getAt(self, pos):
    if pos <= 0 or pos > self.nodeCount: # 찾는 위치가 불가능 할 경우
        return None

    i = 1
    curr = self.head
    while i < pos:
        curr = curr.next
        i += 1

    return curr
```





### Array와 Linked List 비교

|                | 배열        | 연결 리스트      |
| -------------- | ----------- | ---------------- |
| 저장 공간      | 연속한 위치 | 임의의 위치      |
| 특정 원소 지칭 | 매우 간편   | 선형 탐색과 유사 |
| 시간 복잡도    | $O(1)$      | $O(n)$           |

