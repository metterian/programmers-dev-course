# 트리(Trees)

> 데이터의 검색과 탐색에 아주 널리 이용되는 자료 구조로서 트리 (tree) 라는 것이 있습니다. 우리 말로 "나무" 라고 번역하기도 하는데, 대부분의 경우에는 그냥 "트리" 라고 부릅니다. 트리를 딱딱하게 말하면, 순환하는 길이 없는 그래프 (graph) 로 정의합니다.

![image](https://media.vlpt.us/images/inyong_pang/post/7668b115-90ed-46c7-8b41-fe17fa1bc99f/image.png)

- 정점(node)과 간선(edge)을 이용하여 데이터의 배치 형태를 추상화한 자료 구조



## 트리 용어

### 부모(Parent)노드와 자식(Child)노드

![image](https://media.vlpt.us/images/inyong_pang/post/0b001f7e-7197-4185-a4c3-82333a0356ea/image.png)

### 노드의 수준(Level)

- 트리의 높이(Height) = 최대 수준(level) + 1 
- 이를 깊이라고도 한다.

![image](https://media.vlpt.us/images/inyong_pang/post/af050cb5-d25f-499a-b53c-043e2abd4112/image.png)

![image](https://media.vlpt.us/images/inyong_pang/post/5d74694c-c5d8-4577-bc17-1c119984293f/image.png)

### 부분 트리(서브트리 - Subtree)

트리는 여러개의 서브 트리로 구성 될 수 있다.

![image](https://media.vlpt.us/images/inyong_pang/post/aec4f657-4e14-4da7-aebb-26b75e9f557b/image.png)



### 노드의 차수(Degree)

> = 자식 (서브트리)의 수

![img](https://media.vlpt.us/images/inyong_pang/post/513d3250-3a6d-4f0c-8868-bb842c407115/image.png)





## </br>이진 트리(binary trees)

- 모든 노드의 **차수**(degree)가 **2이하**인 트리
- 빈 트리(empty tree)도 이진 트리다.

#### **재귀속성**

재귀적으로 정의 할 수 잇다.

- 루트 노드 + 왼쪽 서브트리 + 오른쪽 서브트리
  (단, 이 때 왼쪽과 오른쪽 서브트리 또한 이진 트리→ 재귀 속성의 종료 조건)

![image](https://media.vlpt.us/images/inyong_pang/post/a1de5ec8-bfd6-4973-9a8e-3643963a60cf/image.png)

### 포화 이진 트리(full binary tree)

모든 레벨에서의 **노드들이 모두 채워져 있는 이진트리**를 말한다. 포화 이진 트리는 높이가 K이고 노드의 개수가 $2^K -1$개인 이진트리라는 속성을 가진다

![image](https://media.vlpt.us/images/inyong_pang/post/482b84ab-f576-4c2e-b889-6cb57856cf76/image.png)

### 완전 이진 트리(complete binary tree)

- 높이 $k$인 완전 이진트리는 레벨 $k-2$까지는 모든 노드가 2개의 자식을 가진 포화 이진트리로 구성
- 단, 마지막 레벨 $k-1$에 풀로 채워져 있지 않더라도 **왼쪽부터 노드가 순차적으로 채워져** 있다면
  완전 이진 트리(complete binary tree)

![img](https://media.vlpt.us/images/inyong_pang/post/06133890-a5c6-4516-8567-06a965822b12/image.png)