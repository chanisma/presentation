---
name: presentation-builder
description: >
  한국 교육용 프레젠테이션 HTML 페이지를 생성합니다. 프레젠테이션, 발표자료, 슬라이드, PPT 대체, 수업자료, 학교 발표,
  교육 프레젠테이션을 만들고 싶을 때 사용하세요. '발표자료 만들어줘', '프레젠테이션 생성', '슬라이드 제작', '수업 PPT' 등의
  요청에 반드시 이 스킬을 사용하세요. Also use for: "create presentation", "make slides", "build a deck",
  "education slides", "school presentation", or any request involving 30 modern design styles like
  Glassmorphism, Neo-Brutalism, Bento Grid, Dark Academia, Aurora Neon Glow, Cyberpunk Outline etc.
  한국 학교/학부모 안내, 교육 발표자료 요청에도 반드시 활성화하세요.
  퀵스타트: "빠르게", "간단하게", "바로", "지금 바로" 키워드가 있으면 퀵스타트 모드를 사용하세요.
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "WebFetch", "AskUserQuestion"]
---

# Presentation Builder - 한국 교육용 프레젠테이션 생성기

단일 HTML 파일로 아름다운 프레젠테이션을 생성하는 스킬입니다.
브라우저 윈도우 크롬 스타일의 카드 기반 디자인을 사용하며, 반응형이고 터치/키보드/마우스 휠/프레젠터 클리커 네비게이션을 지원합니다.

## References 가이드

이 스킬은 progressive disclosure 방식으로 구성되어 있습니다. 아래 참조 파일들은 **해당 단계에서만** 읽으세요.

| 파일 | 읽는 시점 | 내용 |
|------|----------|------|
| `references/styles.md` | 스타일 선택 후, 해당 스타일 섹션만 | 31개 디자인 스타일 상세 스펙 (배경, 컬러, 폰트, 레이아웃) |
| `references/html-template.md` | HTML 생성 직전 | HTML 뼈대, CSS 설계, JS 네비게이션 코드 |
| `references/features.md` | 해당 기능 활성화 시에만 | 자동재생, 다크모드, 발표자노트, 인쇄, 전체화면 상세 |

---

## ⚡ 퀵스타트 모드 (빠른 생성)

사용자가 "빠르게", "바로", "간단하게", "지금 바로" 등을 언급하거나, 주제만 간단히 제시한 경우 사용합니다.

**3가지만 확인 후 즉시 생성:**

```
다음 3가지만 알려주시면 바로 만들어 드립니다:
1. 📌 주제/제목: (예: 2026년 프로그래밍 수업 오리엔테이션)
2. 👥 발표 대상: (예: 중학교 1학년 학생 / 학부모 / 교사)
3. 🏫 학교/기관명: (선택사항)
```

**퀵스타트 기본값 (자동 적용):**

| 항목 | 기본값 |
|------|--------|
| 슬라이드 수 | 대상에 따라 자동 결정 (아래 템플릿 참조) |
| 디자인 스타일 | 대상에 따라 자동 선택 |
| 컬러 테마 | `blue` |
| 폰트 | `noto-sans-kr` |
| 이미지 | `emoji` |
| 네비게이션 | 기본값 전체 적용 |
| 추가 기능 | 모두 off |

퀵스타트로 생성 후: "디자인이나 구성을 바꾸고 싶으시면 말씀해 주세요."

---

## 1단계: 설정 인터뷰 (표준 모드)

퀵스타트가 아닌 경우, **단계별 의사결정 트리**로 진행합니다. 한 번에 모든 옵션을 나열하지 말고, 핵심 3가지만 먼저 확인하세요.

### 핵심 질문 3가지 (필수)

```
프레젠테이션을 만들기 전에 확인할게요:

1. 제목과 주제는 무엇인가요?
   (예: "2026 수학 오리엔테이션" / "AI 윤리 수업자료")

2. 발표 대상과 학교/기관명을 알려주세요.
   (예: "중학교 1학년 학생" / "학부모" / "교사 연수")

3. 내용을 직접 제공하시겠어요, 아니면 제가 주제에 맞게 자동 구성할까요?
   (직접 제공 → 내용 붙여넣기 / 자동 구성 → 주제만으로 생성)

4. 참고할 자료가 있나요? (선택사항)
   (PDF, PPTX, 한글(HWPX), 이미지, 구글 문서 URL 등)
   → 있으면 파일 경로나 URL을 알려주세요. 자료에서 내용을 추출하여 슬라이드를 구성합니다.
```

### 선택 질문 (사용자가 원할 때만)

사용자가 "커스터마이징", "세부 설정", "직접 고를게요" 등을 언급할 때만 아래 항목을 **하나씩** 물어보세요.

**디자인 분위기** → 아래 스타일 추천 매트릭스 참조
**슬라이드 수** → 기본: 대상/유형별 자동 결정
**추가 기능** → QR코드, 다크모드, 발표자노트, 자동재생 등

---

## 1.5단계: 외부 자료 참조 워크플로우

사용자가 참고 자료를 제공한 경우, 아래 형식별 처리 방법을 따릅니다.

### 자료 형식 자동 감지 (확장자 기반)

| 확장자 / 형식 | 처리 방법 | 도구 |
|--------------|----------|------|
| `.pdf` | Read 도구로 읽기, pages 파라미터로 범위 지정 | `Read` |
| `.pptx`, `.ppt` | `/pptx` 스킬로 내용 추출 | `Skill: pptx` |
| `.hwpx`, `.hwp` | `/hwpxskill` 스킬로 읽기 | `Skill: hwpxskill` |
| `.png`, `.jpg`, `.jpeg`, `.webp` | Read 도구로 시각적 분석 | `Read` |
| `.csv`, `.xlsx` | Read 도구 또는 Bash로 읽기, 통계/차트 슬라이드 변환 | `Read` / `Bash` |
| Google Docs/Slides/Sheets URL | WebFetch 또는 브라우저 자동화(GWS)로 접근 | `WebFetch` / `Browser` |
| 기타 텍스트 파일 (`.txt`, `.md`) | Read 도구로 읽기 | `Read` |

### 형식별 처리 상세

#### PDF 파일
```
1. Read 도구로 파일 읽기 (pages: "1-5" 등 범위 지정)
2. 큰 PDF(10페이지 초과)는 목차/첫 페이지로 구조 파악 후 핵심 페이지만 읽기
3. 추출한 내용을 슬라이드 구조로 자동 변환
4. 원본 문서의 섹션 구조를 존중하여 슬라이드 순서 결정
```

#### PPTX 파일
```
1. /pptx 스킬 활용하여 슬라이드별 텍스트, 제목, 구조 추출
2. 기존 슬라이드 순서와 주요 내용을 파악
3. 텍스트 내용을 HTML 프레젠테이션으로 재구성
4. 원본 PPTX의 논리적 흐름을 유지하되, 디자인은 새 스타일 적용
```

#### HWPX / HWP 파일 (한글 문서)
```
1. /hwpxskill 스킬로 한글 문서 내용 읽기
2. 한국 교육 현장 공문/학습지/안내문 형식을 파악
3. 문서의 항목, 번호, 표 등을 슬라이드 컴포넌트로 변환
   - 번호 목록 → activity-list 또는 task-list
   - 표 → comparison 컴포넌트
   - 제목/섹션 → section-overview
```

#### 이미지 파일 (PNG, JPG 등)
```
1. Read 도구로 이미지 시각적 분석
2. 이미지 내 텍스트, 도표, 구조 파악
3. 분석 내용을 슬라이드로 구성, 원본 이미지는 image-focus 컴포넌트에 삽입 가능
```

#### CSV / Excel 데이터
```
1. 데이터 구조와 주요 수치 파악
2. 핵심 지표 → stat-highlight 컴포넌트
3. 비교 데이터 → comparison 또는 two-column 컴포넌트
4. 시계열/변화 → timeline 컴포넌트
5. 데이터 출처를 슬라이드 하단에 표기
```

#### Google Workspace 문서

**방법 1: WebFetch (공개 문서)**
```
공개 문서 (공유 링크 있음):
- WebFetch로 URL 접근하여 내용 추출
- Google Docs/Slides/Sheets의 공개 공유 링크에서 텍스트 추출
```

**방법 2: 브라우저 자동화 - GWS (로그인된 문서, 권장)**
```
사용자가 Chrome에서 Google 계정에 로그인된 상태라면:
1. mcp__claude-in-chrome 도구로 브라우저에서 직접 문서 접근
2. Google Docs:
   - navigate로 문서 URL 열기
   - get_page_text로 전체 텍스트 추출
   - 제목/본문/목록/표 구조 파악
3. Google Slides:
   - navigate로 프레젠테이션 URL 열기
   - get_page_text로 슬라이드별 텍스트 추출
   - 슬라이드 순서와 구조를 파악하여 HTML 프레젠테이션으로 재구성
4. Google Sheets:
   - navigate로 스프레드시트 URL 열기
   - get_page_text 또는 javascript_tool로 셀 데이터 추출
   - 데이터를 stat-highlight, comparison 등 컴포넌트로 변환

주의: 브라우저 자동화 시 alert/confirm 다이얼로그를 트리거하지 않도록 주의
```

**방법 3: 수동 제공 (접근 불가 시)**
```
WebFetch와 브라우저 자동화 모두 불가능한 경우:
- 사용자에게 안내:
  "구글 문서에 직접 접근이 어렵습니다.
   다음 방법 중 하나를 선택해 주세요:
   ① Chrome에서 해당 문서를 열어주세요 (브라우저 자동화로 읽기)
   ② 문서 내용을 텍스트로 붙여넣기
   ③ 파일 → 다운로드 → PDF 또는 PPTX로 저장 후 경로 제공"
```

**처리 우선순위**: 브라우저 자동화(GWS) > WebFetch > 수동 제공

### 자료 처리 후 워크플로우

```
자료 읽기 완료 →
  핵심 내용 목록 추출 →
  슬라이드 구조 자동 제안 (사용자에게 확인):
    "자료에서 다음 구조를 제안합니다:
     1. [섹션 제목] - [컴포넌트 유형]
     2. ...
     이 구조로 진행할까요, 아니면 수정하시겠어요?"
  →
  확인 후 HTML 생성
```

**원본 자료 존중 원칙:**
- 원본 문서의 논리적 순서와 섹션 구조를 최대한 유지
- 내용을 임의로 삭제하지 않고, 많으면 슬라이드를 추가로 분리
- 원본에서 온 수치, 날짜, 고유명사는 정확히 그대로 사용
- 디자인(색상, 레이아웃)만 새로 적용하고 내용은 원본 기준

---

## 2단계: 슬라이드 구조 자동 추천

발표 대상과 목적에 따라 아래 템플릿 중 하나를 자동 선택합니다. 사용자가 수정을 원하면 조정합니다.

### 🏫 오리엔테이션용 (학생 대상, 학기 초)

**추천 슬라이드 수:** 10~12장 | **추천 스타일:** `Glassmorphism`, `Bento Grid`, `Soft Pink Card UI`

```
1. 표지 (cover) - 연도, 과목명, 교사 소개
2. 목차 (toc) - 오늘 배울 내용
3. 수업 소개 (section-overview) - 과목이 뭘 배우나
4. 연간 학습 로드맵 (timeline) - 학기별 주요 단원
5. 수업 방식 (card-grid) - 이론/실습/프로젝트
6. 평가 기준 (comparison) - 성적 구성 비율
7. 준비물 & 규칙 (activity-list) - 필수 준비 사항
8. 주요 일정 (deadline-callout) - 시험, 제출 마감일
9. 선생님 소개 (two-column) - 연락처, 상담 시간
10. 기대하는 것 (quote) - 동기 부여 메시지
11. 마무리 (end) - 기대감 메시지 + QR
```

### 📚 수업자료용 (개념 설명, 단원 학습)

**추천 슬라이드 수:** 8~15장 | **추천 스타일:** `Swiss International`, `Nordic Minimalism`, `Dark Academia`

```
1. 표지 (cover) - 단원명, 학습 목표
2. 학습 목표 (stat-highlight) - 이번 수업에서 배울 3가지
3. 핵심 개념 도입 (section-overview) - 왜 배우나
4~N. 개념 설명 (card-grid / two-column / activity-list) - 핵심 내용
N+1. 예시 & 실습 (showcase-grid / task-list) - 실제 적용
N+2. 정리 & 요약 (stat-highlight) - 핵심 포인트 3가지
N+3. 다음 시간 예고 (deadline-callout) - 숙제, 다음 단원
N+4. 마무리 (end)
```

### 👨‍👩‍👧 학부모 안내용 (학부모 대상)

**추천 슬라이드 수:** 8~10장 | **추천 스타일:** `Soft Pink Card UI`, `Nordic Minimalism`, `Monochrome Minimal`

```
1. 표지 (cover) - 학교명, 행사/안내 제목, 날짜
2. 안내 목적 (section-overview) - 왜 이 안내를 드리나
3. 핵심 내용 1 (card-grid) - 주요 변경/안내 사항
4. 핵심 내용 2 (activity-list) - 세부 사항
5. 일정 & 마감 (deadline-callout) - 중요 날짜, 제출 서류
6. 학교 지원 방안 (two-column) - 학교에서 하는 것 vs 가정에서 할 것
7. 자주 묻는 질문 (card-grid) - FAQ 형식
8. 연락처 & 문의 (end) - 담임 연락처, QR코드
```

### 🎓 교사 연수용 (교사/직원 대상)

**추천 슬라이드 수:** 10~14장 | **추천 스타일:** `Swiss International`, `Bento Grid`, `Editorial Magazine`

```
1. 표지 (cover) - 연수 제목, 강사명, 날짜
2. 목차 (toc)
3. 배경 & 필요성 (two-column) - 현황 vs 문제점
4. 핵심 내용 1~3 (section-overview + card-grid)
5. 실습 / 적용 사례 (showcase-grid / task-list)
6. 토론 & Q&A 안내 (activity-list)
7. 실행 계획 (timeline) - 적용 단계
8. 참고 자료 (card-grid) - 링크, 자료 목록
9. 마무리 (end) - 핵심 요약, QR
```

### 🚀 프로젝트 발표용 (학생 결과물 발표)

**추천 슬라이드 수:** 6~10장 | **추천 스타일:** `Glassmorphism`, `Bento Grid`, `Neo-Brutalism`

```
1. 표지 (cover) - 프로젝트명, 팀원
2. 문제 정의 (two-column) - 문제 vs 해결 방향
3. 과정 (timeline) - 단계별 진행 과정
4. 결과물 소개 (showcase-grid / image-focus)
5. 핵심 성과 (stat-highlight) - 수치, 데이터
6. 배운 점 (card-grid) - 팀원별 소감
7. 마무리 (end) - 감사 + 데모 QR
```

---

## 3단계: 디자인 스타일 & 컬러 테마

### 모던 디자인 스타일 적용

사용자가 디자인 스타일을 선택한 경우:

1. **스펙 로딩**: `references/styles.md`에서 선택된 스타일의 상세 스펙을 읽기
2. **배경 적용**: 스타일의 Background 스펙을 `body` 및 `.slide` 배경에 적용
3. **컬러 매핑**: 스타일의 Colors를 CSS 변수로 변환 (`--style-bg`, `--style-primary`, `--style-accent`, `--style-text`, `--style-text-secondary`)
4. **폰트 적용**: 스타일 스펙의 Font를 Google Fonts CDN으로 로딩
5. **레이아웃 변환**: Layout/Signature Elements를 슬라이드 구조에 반영
6. **시그니처 요소**: 각 슬라이드에 Signature Elements를 최소 1개 포함
7. **금지 사항**: 스타일의 Avoid 항목을 반드시 준수

**스타일 추천 매트릭스 (발표 목적별):**

| 프레젠테이션 목적 | 추천 스타일 |
|-------------------|------------|
| 테크 / AI / 스타트업 | Glassmorphism, Aurora Neon, Cyberpunk Outline, SciFi Holographic |
| 기업 / 컨설팅 / 금융 | Swiss International, Monochrome Minimal, Editorial Magazine, Architectural Blueprint |
| 교육 / 연구 / 역사 | Dark Academia, Nordic Minimalism, Brutalist Newspaper |
| 한국 학교 / 학부모 안내 | Soft Pink Card UI |
| 브랜드 / 마케팅 | Gradient Mesh, Typographic Bold, Duotone Split, Risograph Print |
| 제품 / 앱 / UX | Bento Grid, Claymorphism, Pastel Soft UI, Liquid Blob |
| 엔터테인먼트 / 게임 | Retro Y2K, Dark Neon Miami, Vaporwave, Memphis Pop |
| 에코 / 웰니스 / 문화 | Hand-crafted Organic, Nordic Minimalism, Dark Forest Nature |
| IT 인프라 / 아키텍처 | Isometric 3D Flat, Cyberpunk Outline, Architectural Blueprint |
| 포트폴리오 / 크리에이티브 | Monochrome Minimal, Editorial Magazine, Risograph Print, Maximalist Collage |
| 피치덱 / 전략 | Neo-Brutalism, Duotone Split, Bento Grid, Art Deco Luxe |
| 럭셔리 / 이벤트 / 갈라 | Art Deco Luxe, Monochrome Minimal, Dark Academia |
| 과학 / 바이오텍 / 혁신 | Liquid Blob, SciFi Holographic, Aurora Neon |

**스타일-카드 호환 매핑:**

| 스타일 계열 | 권장 카드 스타일 | 카드 변형 |
|------------|-----------------|----------|
| 다크 배경 (Aurora, Cyberpunk, Vaporwave 등) | `minimal` | 반투명 dark panel, neon/glow border |
| 글래스 계열 (Glassmorphism, Pastel Soft UI) | `rounded` | frosted glass, backdrop-filter |
| 에디토리얼 (Swiss, Editorial, Brutalist) | `minimal` | thin border, serif 타이포 강조 |
| 유기적 (Nordic, Organic, Dark Forest) | `rounded` | soft shadow, organic shape |
| 팝/레트로 (Y2K, Memphis, Neo-Brutalism) | `browser` | thick border, hard shadow |
| 럭셔리 (Art Deco, Monochrome, Dark Academia) | `minimal` | gold/thin border, wide spacing |

### 기본 프리셋 테마 (스타일 미선택 시)

> **스타일 미선택 시**: 아래 기본 테마를 사용합니다.

| 설정 | 옵션 | 기본값 |
|------|------|--------|
| 컬러 테마 | `green`, `blue`, `purple`, `orange`, `navy`, `rose`, `custom` | `green` |
| 폰트 | `noto-sans-kr`, `pretendard`, `wanted-sans`, `gmarket-sans` | `noto-sans-kr` |
| 카드 스타일 | `browser` (macOS 윈도우), `minimal` (깔끔), `rounded` (둥근 모서리) | `browser` |
| 배경색 | 테마 메인 컬러 또는 커스텀 HEX | 테마 기본 |

```
green:  --main: #3aaa5c  --dark: #2d8a49  --light: #e8f5e9  --accent: #43b867
blue:   --main: #2196f3  --dark: #1565c0  --light: #e3f2fd  --accent: #42a5f5
purple: --main: #7c4dff  --dark: #6200ea  --light: #ede7f6  --accent: #9c27b0
orange: --main: #ff9800  --dark: #e65100  --light: #fff3e0  --accent: #ffb74d
navy:   --main: #1a237e  --dark: #0d1642  --light: #e8eaf6  --accent: #3f51b5
rose:   --main: #e91e63  --dark: #ad1457  --light: #fce4ec  --accent: #f06292
```

`custom` 선택 시 사용자에게 메인 컬러 HEX를 물어보고, dark/light/accent를 자동 생성하세요.

**보조 컬러 (모든 테마 공통):** 뱃지, 인포박스, 보더 등에 사용
```
blue-accent:   #2196f3 / bg: #e3f2fd
orange-accent: #ff9800 / bg: #fff3e0
purple-accent: #9c27b0 / bg: #f3e5f5
red-accent:    #e53935 / bg: #fce4ec
green-sub:     #43b867 / bg: #e8f5e9
```

---

## 4단계: 슬라이드 컴포넌트 카탈로그

아래 컴포넌트들을 조합하여 슬라이드를 구성합니다. 사용자가 특별히 지정하지 않으면, 내용에 맞게 적절한 컴포넌트를 선택하세요.

| 컴포넌트 | 설명 | 적합 용도 |
|----------|------|----------|
| `cover` | 연도 뱃지 + 대제목 + 부제목 + 기관명, 중앙 정렬 | 표지 |
| `toc` | 번호 리스트 + goToSlide 연결 + 호버 효과 | 목차 |
| `section-overview` | 아이콘+제목 divider + highlight-box + grid-2 카드 | 섹션 시작 |
| `activity-list` | 이모지+제목+설명 리스트, 선택적 사이드 이미지 | 활동/항목 나열 |
| `card-grid` | grid-2 또는 grid-3, 아이콘+제목+설명 카드 | 항목 비교/소개 |
| `showcase-grid` | 5열 그리드, 큰 이모지+이름+설명, 호버 효과 | 쇼케이스 |
| `task-list` | 번호+제목+설명, 왼쪽 컬러 보더 | 과제/단계 목록 |
| `timeline` | 가로 배치, 원형 마커, highlight 강조 | 일정/연혁 |
| `comparison` | 표 형태, 테마 dark 헤더, 짝수행 배경 교대 | 비교 |
| `deadline-callout` | 큰 아이콘+날짜+설명, 주황색 테두리, 액션 버튼 | 마감/강조 알림 |
| `cosware-cards` | 3열 그리드, 고유 배경색 카드 | 서비스/도구 소개 |
| `qr-section` | 중앙 QR 이미지 + 라벨 + URL | QR 코드 |
| `stat-highlight` | 큰 숫자+라벨 그리드, highlight-box | 통계/수치 강조 |
| `quote` | 큰 따옴표 + 인용 텍스트(이탤릭) + 출처 | 인용문/명언 |
| `two-column` | 좌우 분할 (50:50 / 60:40) | 비교, 전후 대비 |
| `image-focus` | 큰 이미지 영역 + 캡션 | 사진/도표 설명 |
| `end` | 감사 메시지 + 핵심 요약 highlight-box + QR | 마무리 |

---

## 5단계: HTML 생성

> HTML/CSS/JS 코드 템플릿은 `references/html-template.md`를 읽으세요.

핵심 원칙만 여기에 기록합니다:

- **단일 HTML 파일**, 외부 의존성은 Google Fonts CDN만 허용
- **빔프로젝터 가독성**: 1920x1080 기준 본문 최소 22px, 어떤 텍스트도 0.8rem 미만 금지
- **반응형 폰트**: `clamp()`로 뷰포트 대응
- **카드 스타일별 상단바**: browser(dot 3개), minimal(타이틀만), rounded(둥근+그림자)
- **네비게이션 바**: 고정 px(14px)로 본문 rem과 독립, 최소 크기 유지
- **SVG 아이콘**: 유니코드(◀▶) 대신 반드시 SVG 사용 (폰트별 정렬 문제 방지)
- **이모지 절제**: 이모지는 section-divider 아이콘, 카드 아이콘 등 시각적 구분 목적에만 사용. 본문 텍스트, highlight-box, tip 설명문 안에 이모지를 남발하지 않는다. 한 슬라이드당 이모지는 최대 5~6개 이내로 제한하고, 같은 이모지를 반복 사용하지 않는다. 이모지가 정보를 전달하지 않고 장식에 불과하다면 빼는 것이 낫다.

---

## 5.5단계: 슬라이드 세로 높이 검증

> **목표**: 모든 슬라이드가 1920×1080 전체화면에서 스크롤 없이 표시되도록 보장합니다.

### 높이 예산 계산 (1080px 기준, base font 28px)

```
전체 뷰포트:          1080px
─ progress bar:         3px
─ nav bar:             42px
─ slide padding:       34px  (1.2rem × 28px)
─ browser topbar:      35px
─ content padding:     50px  (1.8rem × 28px)
──────────────────────────────
content 가용 높이:    ≈860px
```

### 요소별 높이 참조표 (base 28px 기준)

| 요소 | 예상 높이 |
|------|----------|
| section-divider (아이콘 인라인 + 제목 + 자막) | ~50px |
| card (아이콘 + 제목 + 본문 1줄) | ~80px |
| card (아이콘 + 제목 + 본문 2줄) | ~110px |
| grid-2 gap | ~17px (0.6rem) |
| highlight-box (1줄) | ~55px |
| highlight-box (2줄) | ~75px |
| step-item (2x2 grid) | ~90px |
| stat-card | ~100px |
| tip-item | ~45px |

### 설계 시 검증 방법

각 슬라이드의 콘텐츠 요소 높이를 합산하여 **860px 이내**인지 확인합니다:

```
슬라이드 높이 = section-divider
             + grid 높이 (카드 높이 × 행 수 + gap × (행 수 - 1))
             + highlight-box (있으면)
             + margin/gap 합산

→ 860px 이내이면 OK
→ 초과하면 조정:
  1. 텍스트 간결하게 축약
  2. 카드 padding/gap 축소
  3. section-divider를 아이콘 인라인 배치로 변경
  4. 콘텐츠를 2개 슬라이드로 분리
```

### 넘침 방지 CSS 가이드라인

- section-divider: 아이콘을 h2 왼쪽에 `display: inline`으로 배치하여 세로 공간 절약
- card padding: `0.8rem 1rem` 이하
- grid gap: `0.6rem` 이하
- highlight-box margin: `0.6rem 0` 이하
- 카드 본문 텍스트 1~2줄 이내로 유지

---

## 6단계: 생성 워크플로우

1. **설정 수집**: 1단계(또는 퀵스타트)에 따라 사용자 설정 확인
2. **슬라이드 구조 선택**: 2단계 템플릿에서 대상/목적에 맞는 구조 자동 선택
3. **스타일 스펙 로딩**: 스타일 선택 시 `references/styles.md`에서 해당 스타일만 읽기
4. **HTML 템플릿 로딩**: `references/html-template.md`를 읽고 코드 구조 확인
5. **추가 기능 로딩**: 활성화된 추가 기능이 있으면 `references/features.md` 읽기
6. **구조 설계 공유**: 슬라이드 순서와 컴포넌트 구성을 사용자에게 간략히 공유
7. **HTML 생성**: 단일 파일로 완전한 프레젠테이션 생성
8. **세로 높이 검증**: 5.5단계 기준으로 각 슬라이드가 860px 이내인지 코드상 확인하고 초과 시 조정
9. **폴더 생성 & 파일 저장**: 아래 디렉토리 규칙에 따라 저장
10. **pages.json 업데이트**: 아래 매니페스트 규칙에 따라 항목 추가
11. **확인 안내**: 브라우저에서 열어 확인하도록 안내

### 파일 저장 디렉토리 규칙

```
{작업 디렉토리}/
└── {과목명}/
    └── {내용(주제)}/
        ├── index.html          ← 프레젠테이션 본체
        └── (이미지, QR 등 에셋)
```

**예시:** `프로그래밍/오리엔테이션/index.html`, `정보/AI윤리-수업자료/index.html`

**규칙:**
- 과목명과 내용(주제)은 사용자에게 확인하거나, 제목에서 자동 추출
- 폴더명에 공백 대신 하이픈(`-`) 사용 가능, 한글 폴더명 허용
- HTML 파일명은 `index.html` 기본
- 에셋 파일은 같은 폴더에 저장

### pages.json 매니페스트 업데이트 규칙

프레젠테이션 생성 후, 작업 디렉토리 루트의 `pages.json`을 읽어서 새 항목을 추가합니다.

```json
{
  "title": "프레젠테이션 제목",
  "path": "과목/내용/index.html",
  "emoji": "대표 이모지",
  "description": "1~2문장 설명",
  "tags": [{ "label": "태그명", "color": "blue|green|purple|orange" }],
  "gradient": "linear-gradient(90deg, #색상1, #색상2)"
}
```

**규칙:**
- `pages.json`이 존재하면 해당 과목의 `pages` 배열에 새 항목 추가
- 해당 과목이 없으면 `subjects` 배열에 새 과목 객체 추가
- `pages.json`이 없으면 새로 생성
- gradient 색상은 선택한 컬러 테마에 맞춰 설정
- tags는 핵심 키워드 2~4개 추출

### 관리 대시보드 초기화

프레젠테이션 생성 후, 루트에 `pages.json`과 `index.html`(관리 대시보드)이 있는지 확인하세요.

없으면 사용자에게 안내:
> "수업 자료를 한눈에 볼 수 있는 **관리 대시보드**가 없습니다. 지금 생성할까요?"

동의 시 단일 HTML 파일로 생성:
- `pages.json` fetch → 과목별 카드 목록 렌더링
- 과목별 필터 탭 + 검색창 + gradient 카드 디자인
- 로컬 환경 안내: `python -m http.server 8080` 등 로컬 서버 필요

---

## 콘텐츠 생성 가이드라인

### 대상별 언어 수준

| 대상 | 어휘 수준 | 문장 스타일 | 주의사항 |
|------|----------|------------|---------|
| 초등학생 (1~3학년) | 쉬운 한글, 한자 없음 | 짧은 문장, 구어체, "~해요" | 이모지 적극 활용, 긴 설명 금지 |
| 초등학생 (4~6학년) | 기본 어휘, 쉬운 외래어 | 보통 길이 문장, "~합니다" | 예시 중심, 추상 개념 최소화 |
| 중학생 | 일반 어휘, 교과 용어 허용 | 간결한 문어체, "~입니다" | 핵심 용어에 설명 병기 |
| 고등학생 | 전문 어휘, 영문 약어 가능 | 논리적 문체, 데이터 포함 | 근거 제시, 비판적 사고 유도 |
| 학부모 | 정중한 일상 어휘 | 공손한 문체, "~드립니다" | 전문 용어 최소화, 실용 정보 우선 |
| 교사/교직원 | 교육 전문 용어 가능 | 간결한 업무 문체 | 법령·정책 용어 정확히 사용 |

### 슬라이드당 최적 텍스트량

| 대상 | 슬라이드당 최대 단어 수 | 글머리 기호 최대 수 | 권장 폰트 크기 |
|------|----------------------|------------------|--------------|
| 초등학생 | 30단어 | 3개 | 30px+ |
| 중·고등학생 | 50단어 | 5개 | 24px+ |
| 학부모 | 60단어 | 5개 | 22px+ |
| 교사/교직원 | 80단어 | 7개 | 20px+ |
| 일반 발표 | 60단어 | 5개 | 22px+ |

**황금 규칙:**
- 빔프로젝터에서 5초 안에 핵심 파악 가능해야 함
- 한 슬라이드에 하나의 핵심 메시지만
- 텍스트가 많으면 슬라이드를 분리하거나 `activity-list`/`card-grid` 컴포넌트로 시각화

### 기타 콘텐츠 원칙

- 한국어를 기본 언어로 사용
- 교육 현장에 적합한 정중하고 명확한 문체
- 이모지를 아이콘으로 적극 활용 (별도 이미지 불필요)
- 각 슬라이드의 텍스트량은 화면에 스크롤 없이 보일 정도로 조절
- 핵심 수치나 키워드는 `<strong>` 또는 뱃지로 강조
- 링크가 있으면 `target="_blank"`

---

## 핵심 디자인 원칙

- 선택된 스타일의 배경, 폰트, 레이아웃 스펙을 **엄격히** 준수
- 모든 슬라이드에 **최소 1개 시각 요소** (아이콘, 컬러 블록, 도형) 포함 — 텍스트만 있는 슬라이드 금지
- 스타일의 **시그니처 요소**를 모든 슬라이드에 일관되게 반복
- **정확한 HEX 값** 사용 — 근사치 색상은 미적 일관성을 깨뜨림
- **폰트 페어링**을 스펙 그대로 적용 — 타이포그래피가 스타일 인상의 50%를 결정

---

## 에러 처리 가이드

### 흔한 실패 패턴과 대응법

| 문제 | 증상 | 해결법 |
|------|------|--------|
| **콘텐츠 과부하** | 슬라이드가 스크롤 필요, 텍스트가 카드 밖으로 넘침 | 슬라이드 분리, `activity-list`/`card-grid`로 시각화, 텍스트 50% 축소 |
| **스타일 충돌** | 다크 배경에 어두운 텍스트, 배경과 카드 구분 안 됨 | 스타일-카드 호환 매핑 재확인, 텍스트 색상 대비 4.5:1 이상 확보 |
| **폰트 미로딩** | 시스템 기본 폰트로 표시, 자간/행간 무너짐 | Google Fonts CDN 링크 점검, `preconnect` 태그 확인 |
| **모바일 레이아웃 붕괴** | grid가 겹치거나 텍스트 잘림 | 768px 미만 grid → 1열, `clamp()` 폰트 적용 확인 |
| **네비게이션 미작동** | 키보드/스와이프 반응 없음 | JS 이벤트 리스너 중복 등록 확인, `currentSlide`/`totalSlides` 변수 확인 |
| **슬라이드 수 부족** | 내용이 너무 압축되어 이해 어려움 | 복잡한 슬라이드를 2~3장으로 분리, 섹션 divider 추가 |
| **슬라이드 수 과다** | 발표 시간 초과, 집중력 저하 | 유사 내용 통합, 세부 사항은 발표자 노트로 이동 |
| **QR 코드 미작동** | 빈 이미지 박스 표시 | placeholder 이미지 또는 실제 QR URL 사용 안내 |
| **인쇄 레이아웃 깨짐** | 슬라이드 짤림, 배경 미출력 | `@media print` CSS 확인, `page-break-after: always` 적용 |

### 사용자 입력 부족 시 대응

```
사용자가 주제만 제시하고 내용을 제공하지 않은 경우:
→ 대상 학년/직군에 맞는 내용을 AI가 자동 구성
→ 생성 후: "내용을 자동 구성했습니다. 수정할 부분이 있으면 말씀해 주세요."

사용자가 슬라이드 수를 지정하지 않은 경우:
→ 2단계 템플릿의 기본 슬라이드 수 사용

사용자가 스타일을 지정하지 않은 경우:
→ 대상/목적에 따라 추천 스타일 자동 선택, 생성 후 알림
```

---

## 레이아웃 & 네비게이션 세부 설정 (선택)

사용자가 "세부 설정" 또는 "직접 설정"을 원할 때만 제공합니다.

**레이아웃:**

| 설정 | 옵션 | 기본값 |
|------|------|--------|
| 콘텐츠 밀도 | `compact`, `normal`, `spacious` | `normal` |
| 최대 너비 | `1200px`, `1400px`, `1600px`, `full` | `1600px` |
| 이미지 스타일 | `emoji`, `placeholder`, `url`, `ai-generate` | `emoji` |

**네비게이션:**

| 설정 | 옵션 | 기본값 |
|------|------|--------|
| 네비 위치 | `bottom`, `top`, `hidden` | `bottom` |
| 프로그레스바 | `top`, `bottom`, `hidden` | `top` |
| 키보드 네비게이션 | `on`, `off` | `on` |
| 프레젠터 클리커 | `on`, `off` | `on` |
| 마우스 휠 네비게이션 | `on`, `off` | `on` |
| 터치 스와이프 | `on`, `off` | `on` |
| 슬라이드 번호 표시 | `on`, `off` | `on` |

**추가 기능:**

| 설정 | 옵션 | 기본값 |
|------|------|--------|
| QR 코드 | `on` (표지+마지막), `cover-only`, `end-only`, `off` | `off` |
| 전환 효과 | `fade`, `slide`, `none` | `fade` |
| 자동 재생 | `off`, `5s`, `10s`, `15s`, `30s` | `off` |
| 인쇄 스타일 | `on`, `off` | `off` |
| 다크모드 토글 | `on`, `off` | `off` |
| 발표자 노트 | `on`, `off` | `off` |
| 전체화면 버튼 | `on`, `off` | `off` |
| AI 이미지 생성 | `on`, `off` | `off` |

---

## AI 이미지 생성 (GLM-Image / CogView-4)

> 이 기능은 `이미지 스타일: ai-generate` 또는 `AI 이미지 생성: on` 설정 시 활성화됩니다.
> 환경 변수 `ZAI_GLM_API_KEY`가 설정되어 있어야 합니다.

### 개요

Z.AI의 GLM-Image 또는 CogView-4 모델을 사용하여 프레젠테이션에 맞춤 이미지를 생성합니다.
이모지 대신 실제 일러스트/사진 스타일의 이미지를 슬라이드에 삽입하여 시각적 품질을 높입니다.

### API 호출 방법

```bash
# Bash로 이미지 생성 (curl)
curl -s -X POST "https://api.z.ai/api/paas/v4/images/generations" \
  -H "Authorization: Bearer $ZAI_GLM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "cogView-4-250304",
    "prompt": "이미지 설명 (한국어/영어 모두 가능)",
    "size": "1024x1024"
  }'
```

**응답 형식:**
```json
{
  "data": [{ "url": "https://..." }]
}
```

### 이미지 생성 워크플로우

```
1. 슬라이드 구조 확정 후, 이미지가 필요한 슬라이드 식별
2. 각 슬라이드의 주제에 맞는 이미지 프롬프트 작성:
   - 슬라이드 제목 + 핵심 키워드를 기반으로 프롬프트 구성
   - 프레젠테이션 스타일에 맞는 톤 지정 (예: "flat illustration style", "교육용 인포그래픽")
   - 텍스트가 포함되지 않도록 명시 ("no text, no letters")
3. API 호출로 이미지 URL 획득
4. 이미지 다운로드 → 프레젠테이션 폴더에 저장 (slide-1.png, slide-2.png 등)
5. HTML에서 <img src="slide-1.png"> 로 참조
```

### 프롬프트 작성 가이드

| 프레젠테이션 유형 | 프롬프트 스타일 | 예시 |
|-----------------|---------------|------|
| 수업 자료 | 교육용 플랫 일러스트 | "flat illustration of cloud computing concept, server icons, data flow, blue color scheme, educational style, no text" |
| 학부모 안내 | 따뜻한 사진 스타일 | "warm photo of students studying together in modern classroom, bright lighting, no text" |
| 기술 발표 | 미니멀 3D 렌더링 | "minimal 3D render of AI neural network, dark background, glowing nodes, no text" |
| 프로젝트 발표 | 인포그래픽 스타일 | "infographic style illustration of project timeline, milestone markers, clean design, no text" |

### 이미지 사이즈 권장

| 용도 | 사이즈 | 비고 |
|------|--------|------|
| 커버 슬라이드 배경 | `1920x1080` | 16:9 비율 |
| 카드 내 이미지 | `1024x1024` | 정사각형 |
| 아이콘/일러스트 | `512x512` | 작은 삽화 |
| image-focus 컴포넌트 | `1280x720` | 16:9 가로형 |

### 주의사항

- **비용**: CogView-4 $0.01/장, GLM-Image $0.015/장
- **생성 시간**: 이미지당 5~15초 소요
- **병렬 생성**: 여러 이미지가 필요한 경우 Bash를 병렬로 호출하여 시간 단축
- **파일 저장**: 이미지는 프레젠테이션과 같은 폴더에 저장 (외부 URL 의존 방지)
- **대체 계획**: API 호출 실패 시 이모지 아이콘으로 대체 (graceful fallback)
- **프롬프트에 "no text" 필수**: AI 생성 이미지의 텍스트는 부정확할 수 있으므로 제외

### 이미지 다운로드 및 저장

```bash
# 이미지 URL에서 다운로드하여 프레젠테이션 폴더에 저장
curl -s -o "{프레젠테이션_폴더}/slide-1.png" "{이미지_URL}"
```

### HTML에서 참조

```html
<!-- image-focus 컴포넌트에서 AI 생성 이미지 사용 -->
<div class="slide" id="slide-3">
  <div class="browser-window">
    <div class="browser-header"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
    <div class="browser-content image-focus-slide">
      <img src="slide-3.png" alt="클라우드 컴퓨팅 개념도" style="max-width:100%; border-radius:12px;">
      <p class="caption">▲ AI가 생성한 클라우드 컴퓨팅 개념 일러스트</p>
    </div>
  </div>
</div>
```

---

## 팁과 주의사항

- `overflow: hidden`이 body에 설정되므로 슬라이드 내용이 넘치지 않게 조절
- `browser-content`에 `overflow-y: auto`가 있어 스크롤 가능하지만, 가능하면 한 화면에 맞추기
- 네비 바가 하단 고정이므로 `.browser-content`에 `padding-bottom: 3rem` 이상 확보
- QR 코드는 사용자 제공 또는 placeholder 이미지
- CSS 변수 활용으로 색상 변경 용이
- Google Fonts 외 CDN 사용 금지 (오프라인 환경 대비)
- 반응형: 768px 이하에서 grid → 1열, 480px 이하에서 축소 대응
