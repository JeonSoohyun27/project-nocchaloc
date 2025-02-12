#README
# 🍵 녹차록 🍵

## 📍 프로젝트 개요
- **초기세팅부터 모두 직접 진행한 오설록 사이트 클론 프로젝트**
- **기 간**: 2021.07.05.~2021.07.16.(12일)
- **Team member**
  - Frontend: 2인(김수종, 오지수)
  - Backend: 3인(박성준, 안재경, 전수현)

## 📍 프로젝트 미리보기
![ezgif com-gif-maker](https://user-images.githubusercontent.com/74139727/126070910-dd2c6151-0245-436d-a2ab-12d2e0653079.gif)

## 📍 프로젝트 진행
- Trello를 이용한 Scrum관리
![image](https://user-images.githubusercontent.com/83414688/126182756-d41897ff-1e65-4201-a099-1edae691d2cc.png)

- 매일 어제 한 일, 오늘 할 일, 특이사항 공유
- 미팅전 Agenda 공유 

## 📍 Database 설계
![](https://images.velog.io/images/anjaekk/post/47adf0ea-2c4f-48f1-b8cc-d6590b3cc62e/image.png)

## 📍 구현 기능
|User(회원가입 및 로그인)|Product(제품 리스트 및 리뷰)|Order(장바구니 및 결제)|
|:-:|:-:|:-:|
|Bcrypt 암호화|pagination|장바구니 CRUD|
|JWT Access Token 전송|신상품, 가격, 조회수, 리뷰 기준 정렬|포인트 결제|
|회원가입 유효성 검사 구현|제품 타입에 별 filtering|
||제품 검색(이름, 설명)|
||리뷰 CRUD||

## 📍 내가 맡은 파트
- AqueryTool을 이용한 RDBMS 모델링
- Trello를 이용한 Scrum방식으로 협업 진행
- 회원가입 및 로그인(Bcrypt 암호화, JWT 사용, 정규표현식을 사용한 Validation)
- 상품에 대한 상품평 CRUD 기능 구현

## 📍 API Documentation
https://documenter.getpostman.com/view/16450829/Tzm8EErD
