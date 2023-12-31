# README

## 1. Overview
  Weather seller에서 개발한 추천 시스템의 이름은 '오밥무(오늘 밥은 무엇)'입니다.
  Weather seller는 날씨 정보를 활용한 금융/비금융 데이터 기반 추천 알고리즘을 만드는 것이 목표입니다.
  따라서 저희는 고객에게 날씨와 소비자 경향을 분석하고, 날씨와 비금융데이터/금융데이터를 연계하여 추천 시스템을 만드는 것입니다.
  
- **필요성**
  고객이 식당을 찾기 위해 일일이 돌아다니는 것은 번거로운 일입니다.
  그리고 날씨와 자신의 경제적 상황을 모두 분석할 수 새로운 추천 시스템을 개발합니다.

  이런 추천 시스템은 고객이 식당에 대한 고민을 해결하고, 자신의 지역을 중심으로 원활한 식사 계획을 진행할 수 있습니다.
  그리고 자기 지역에 있지만 미처 가보지 못한 우리 지역의 식당도 만나볼 수 있습니다.
  업체들 또한 근거리에 있는 주민들에게 자기 식당을 데이터셋으로 보내어 홍보하는 효과도 있습니다.

## 2. 전체적인 역할 분담

*이 부분은 자신의 역할을 최대한 많이 담아주세요~ 제가 다 확인해보지 않아서 모를 수도 있어요...
또 정확하게 작성했는지도 확인해주세요. :)

- *엄정석*: 팀장, 회의 현황 조율, 관련 학습자료 조사 및 발표 담당, 결과 보고서 보완 및 정리
- *김제현*: 웹 인터페이스(GUI) 구현, 데이터베이스 관리, API 적용, 데이터 취합 및 정리
- *이수연*: 데이터 전처리 및 분석, 성능 적합성 판단, 인공지능 기반 추천 알고리즘(로직) 구현, 자문 결과 및 각종 보고서 작성
- *주정윤*: 서버 구현, 인터페이스-로직 연결, 기계학습 처리, 회계자료 작성

## 3. 수행 과정

- **9월**: 프로젝트 문제풀 안내 및 데이터 전처리 시작
- **10월**: 프로젝트 작업에 필요한 소프트웨어 구입(GPT 4.0), 기초 작업 환경 마련
- **11월**: 프로젝트 작업 시작
1. 데이터 전처리 코드: pandas 라이브러리 및 데이터 전처리(이상치, 결측치, 정규화)
2. 성능 측정 척도(metric)를 통한 적합성 판단: 정확성, 재현율, F-척도를 이용한 metric 확인 및 적합성 판단
3. 인공지능/기계학습 신경망 및 서버 구현: 날씨 정보와 사용자 입력을 받아 추천하는 신경망 모델 구성, 로직과 GUI 연결
4. 인터페이스 구현 및 최종 디자인 구성: 웹의 형태로 최종 형태 시연
5. 전문가와의 피드백 : 프로젝트를 수행하면서 멘토님과 피드백을 주고받으며 수정 및 보완
-  **12월**: 결과보고서 작성, 발표자료 작성

## 4. 최종 기능

-날씨를 먼저 분석하고, 이를 사용자 화면에 출력
-소비자 정보를 받아 식당 추천  
-소비자 경향성 분석: 식당 분야별로 ~% 출력
-순위 부여(ranking) 및 관련 정보 반환: 업체명, 평점, URL

## 5. 의의

1. 사용자에게 날씨에 맞는 카드 혜택 추천을 제공하는 기반을 마련
2. 개인 맞춤형, 지역 맞춤형 서비스 경험 가능
3. 기업 및 자영업자의 영업 마케팅의 효율성 증진

