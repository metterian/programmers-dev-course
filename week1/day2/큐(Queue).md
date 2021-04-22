# 큐 (Queues)

> 큐에서는 스택과는 반대로, 어느 시점에서 큐에 들어 있는 데이터 원소를 꺼내면 큐에 들어 있는 원소들 중 가장 먼저 넣었던 것이 꺼내집니다. 따라서 큐를 **선입선출** (FIFO; first-in first-out) 이라고도 부릅니다.

#### Enqueue 연산

- 자료를 넣은 때의 연산

#### Dequeue 연산

- 꺼낸 데이터를 반대쪽에서 뽑아내는 연산



## 큐의 동작

![img](https://media.vlpt.us/images/inyong_pang/post/d87f5540-24ad-4ee2-bcb4-b6433e72734d/image.png)

## 연산의 정의

- size() : 현재 큐에 들어있는 데이터 원소의 수를 구함
- isEmpty() : 현재 큐가 비어 있는지를 판단
- enqueue(x) : 데이터 원소 x를 큐에 추가
- dequeue() : 큐의 맨 앞에 저장된 데이터 원소를 제거(또는 반환)
- peek() : 큐의 맨 앞에 저장된 데이터 원소를 반환(제거하지 않음)





## 배열로 구현한 큐

```python
# 배열로 구현한 큐
class ArrayQueue:
    # 빈 큐를 초기화
    def __init__(self):
        self.data = []
        
    # 큐의 크기를 리턴
    def size(self):
        return len(self.data)

    # 큐가 비어있는지 판단
    def isEmpty(self):
        return self.size() == 0
    
    # 데이터 원소 추가 연산
    def enqueue(self, item):
        self.data.append(item)
        
    # 데이터 원소 삭제 연산
    def dequeue(self):
        return self.data.pop(0)
    
    # 큐의 맨 앞 원소 반환
    def peek(self):
        return self.data[0]
```





## 배열로 구현한 큐의 연산 복잡도

|    연산    |    복잡도     |
| :--------: | :-----------: |
|   size()   |    $O(1)$     |
| isEmpty()  |    $O(1)$     |
| enqueue(x) |    $O(1)$     |
| dequeue()  | $\bold{O(n)}$ |
|   peek()   |    $O(1)$     |

- 데이터 삭제 연산(dequeue)은 큐의 길이가 길어질수록 그 만큼 오래걸린다
- 큐의 길이에 비례하는 복잡도를 가진다
- e.g. **맨 앞의 원소가 삭제가 되면, 그 뒤에 있는 데이터들이 하나씩 앞으로 당겨서 와야함으로 큐의 길이만큼 연산이 일어남**

