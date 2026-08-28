# 실시간 교통 상태 대시보드
공공 교통 API를 활용하여 도로상황을 실시간 모니터링한다.

## 목적
- 김해와 부산을 연결하는 낙동강다리의 실시간 교통량을 확인할 수 있다.
- 자주 막히는 구간의 cctv를 실시간 조회할 수 있다.


## 목표
- 공공 API 데이터 수집
- 5분 단위 데이터 캐싱
- 과거 데이터 분석 후 혼잡도 예측


## APP 구조
- main
- controller : HTTP 요청 처리
- service : 데이터 수집/가공/계산
- repository : DB, 캐시 접근
- scheduler : 공공 API 5분 주기 갱신


## 흐름
HTTP 요청
   ↓
Controller
   ↓
Service
   ↓
Repository
   ↓
PostgreSQL / Cache

Scheduler
↓
Service