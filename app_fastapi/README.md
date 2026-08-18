# 실시간 교통 상태 대시보드
공공 교통 API를 활용하여 도로상황을 실시간 모니터링한다.
과거 데이터를 기반으로 혼잡도 예측

- [창원 <---불모산터널---> 김해 장유]
- [김해 <---낙동강---> 부산]
- [부산 고가도로]

## 목적
- 창원/부산/김해를 연결하는 유명한 교통체증 구간의  도로상황을 실시간 확인하여 원할한 일정 조율을 돕는다.


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