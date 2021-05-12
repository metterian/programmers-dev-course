# Serialization & De-serialization

## 들어가며

### 환경 세팅

실습을 위해 다음과 같이 AWS AMI 환경에서 다음 코드들을 미리 실행 시켜 줍니다.

```bash
# 아나콘다 가상환경 실행 
conda activate pytorch_p36
# template 소스코드 다운로드 
git clone https://github.com/sackoh/kdt-ai-aws
cd ./kdt-ai-aws

# 필요 라이브러리 설치 
pip install $-r$ requirements.txt
```





## Skeleton of model handler to serve model

모델 서빙을 위한 코드 뼈대는 다음과 같습니다.

```python
class ModelHandler(BaseHandler):
    def init (self):
    	pass
    def initialize(self,  **kwargs): pass
    def preprocess(self, data):
    	pass
    def inference(self, data):
   	 	pass
    def postprocess(self, data):
   		pass
    def handle(self, data):
    	pass
```

### `handle()` 의 역할

실질적으로 API가 호출을 담담하는 역할을 합니다. 즉, **요청 정보를 받아 적절한 응답을 반환**하는 역활 입니다. 이는 다음과 같은 과정으로 진행 됩니다.

1. 정의된 양식으로 데이터가 입력됐는지 확인
2. 입력 값에 대한 전처리 및 모델에 입력하기 위한 형태로 변환
3. 모델 추론
4. 모델 반환값의 후처리 작업
5. 결과 반환



#### 코드 구현

위 내용을 실제 코드로 구현 하면 다음과 같습니다.

```python
def handle(self, data):
	model_input = self. preprocess (data)
	model_output = self. inference(model_input)
return self. postprocess (model_output)
```





### `initialize()` 의 역할

데이터 처리나 모델, configuration 등 초기화 등을 담당합니다. 이는 다음과 같은 과정으로 수행 됩니다.
1. Configuration 등 초기화
2. (Optional) 신경망을 구성하고 초기화
3. 사전 학습한 모델이나 전처리기 불러오기 (De-serialization)



#### 주의 할 점

모델은 전역변수로 불러와야 합니다. 만약 inference를 할 때마다 모델을 불러오도록 한다면 그로 인해 발생하는 시간이나 자원 등의 낭비가 발생합니다. 일반적으로 요청을 처리하기 전에 모델을 불러 둡니다.





