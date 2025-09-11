# CIWAL
Civilisation &amp; Values

# CIWAL
Civilization &amp; Values

# 문명과 가치 (Civilization & Values)

## 개요
**정책은 가치 선택이며, 가치 선택은 사회의 결과를 바꾼다.**  
본 프로젝트는 사회 발전 단계를 압축적으로 체험할 수 있는 시뮬레이션 게임입니다.  
플레이어는 부족장 → 왕 → 대통령이 되어 정책을 선택하고, 그 결과로 사회 지표(GDP, 행복, 자유, 불평등, 지속가능성)가 어떻게 변하는지 직관적으로 확인합니다.

- **플랫폼**: 전시형 설치물 (프로젝션 + 버튼패드), Steam/PC  
- **엔진**: Unity (시각화/UI), Python (Mesa/NumPy 기반 시뮬레이션)  
- **타깃 플레이타임**: 10–15분 (전시), 반복 플레이 가능 (Steam)

---

## 주요 시스템

### 1. 에이전트 (Agent)
- 속성: wealth, productivity, health, education, happiness, mobility, occupation, location, relationships
- 행동: 이동(move), 생산(produce), 거래(trade), 행복 갱신(update_happiness), 전직(change_occupation)

### 2. 토지 (Land)
- 속성: fertility, resources, pollution, facility_type, population_capacity
- 행동: 자원 갱신(update_resources), 오염 갱신(update_pollution), 업그레이드(upgrade)

### 3. 사회 지표 (Metrics)
- GDP per capita
- 행복 지수
- 자유 지수
- 불평등 지수 (Gini coefficient)
- 지속가능성 지수

### 4. 정책 시스템
- 플레이어 입력(세금, 복지, 환경규제, 무역정책 등) → 파라미터 변경 → 함수 값 변화

---

## 발전 단계
1. **부족**: 충돌 거래만 가능, 움집/농지 중심
2. **마을**: 관계 기반 거래 추가, 시장 등장
3. **영지**: 시장이 허브 역할, 성/행정 시설 등장
4. **도시/세계화**: 네트워크 기반 원거리 거래, 금융/서비스 업종 등장

---

## 개발 순서 계획
1. Python으로 시뮬레이션 엔진 구현 (Agent, Land, Simulation)
2. Unity에서 Tilemap + 기본 시각화
3. 토지 자동 업그레이드 로직 추가
4. 발전 단계별 거래 규칙 확장
5. 정책 시스템 & UI 구현
6. NPC 대사/말풍선 추가
7. 지표 그래프/스코어보드 + 엔딩 분석
8. QR코드/프린트 연동 (전시 모드)
9. Steam 버전: 챌린지 모드 + 리더보드

---
