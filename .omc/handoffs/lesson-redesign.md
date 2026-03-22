# 6차시 CSS 심화 수업 재설계 계획서

## 기존 수업 분석

### 기존 구조 (8 슬라이드)
| # | 슬라이드 | 유형 |
|---|---------|------|
| 1 | CSS 심화: 응용과 레이아웃 | 커버 |
| 2 | 오늘 배울 내용 | 목차 |
| 3 | 직접 코딩하며 결과 확인하기 | 실습 안내 |
| 4 | 식별자에 CSS 설정하기 (class, id) | 실습 (HTML+CSS 분리 에디터) |
| 5 | 자손 선택자와 자식 선택자 | 실습 (HTML+CSS 분리 에디터) |
| 6 | 여백 (Margin과 Padding) | 실습 (HTML+CSS 분리 에디터) |
| 7 | 레이아웃 배치 (Flexbox) | 실습 (HTML+CSS 분리 에디터) |
| 8 | 나만의 자기소개 페이지 완성하기 | 최종 미션 |

### 기존 문제점
1. **HTML/CSS 에디터 분리**: 학생들이 HTML 전체 구조를 보지 못하고 body 내부 코드만 보게 됨
2. **`<style>` 태그 위치 이해 불가**: CSS가 어디에 위치하는지 전체 맥락 없이 학습
3. **설명 슬라이드 부족**: 각 주제에 대한 개념 설명 없이 바로 코드 실습으로 진입
4. **점진적 학습 부재**: class/id 개념 설명 후 바로 복합 예제를 보여줌

---

## 재설계 원칙

### 핵심 변경사항
- **통합 에디터**: HTML 에디터와 CSS 에디터를 분리하지 않고, 하나의 통합 에디터에 전체 HTML 문서 구조(`<!DOCTYPE html>`부터 `</html>`까지)를 보여줌
- **`<style>` 태그 포함**: CSS를 `<style>` 태그 안에 포함한 완전한 HTML 문서로 실습 코드를 구성
- **설명→실습 쌍**: 각 주제마다 개념 설명 슬라이드 + 실습 슬라이드를 쌍으로 구성
- **점진적 난이도**: 간단한 예제에서 복합 예제로 단계적 진행

### 에디터 설계 변경
- **기존**: `editor-pane` 안에 `html-editor` + `css-editor` 두 개의 textarea
- **변경**: `editor-pane` 안에 하나의 `code-editor` textarea에 전체 HTML 문서 표시
- **이유**: 학생들이 아직 HTML 구조에 익숙하지 않으므로, `<!DOCTYPE html>`, `<html>`, `<head>`, `<style>`, `<body>` 등 전체 구조를 보면서 CSS가 어디에 위치하는지 이해할 수 있도록 함

### 코드 에디터 동작 변경
- 기존: `htmlCode` + `cssCode`를 JavaScript에서 조합하여 iframe에 주입
- 변경: textarea의 전체 내용을 그대로 iframe의 `srcdoc`에 전달 (이미 완전한 HTML 문서이므로)

---

## 슬라이드 구성안 (총 12 슬라이드)

---

### 슬라이드 1: 커버
- **제목**: CSS 심화: 응용과 레이아웃
- **유형**: 커버
- **내용**:
  - 배지: "프로그래밍 6차시"
  - 부제: 식별자 CSS 설정 / 자손·자식 선택자 / Margin과 Padding / Flex 배치
- **변경사항**: 기존과 동일

---

### 슬라이드 2: 목차
- **제목**: 오늘 배울 내용
- **유형**: 목차
- **내용**: 4개 주제 카드 (클릭 시 해당 슬라이드로 이동)
  1. 식별자에 CSS 설정하기 (class, id)
  2. 선택자 응용 심화 (자손/자식)
  3. 여백 (Margin, Padding)
  4. 레이아웃 배치 (Flexbox)
- **변경사항**: 기존과 동일 (이동 대상 슬라이드 번호만 조정)

---

### 슬라이드 3: 실습 안내
- **제목**: 직접 코딩하며 결과 확인하기
- **유형**: 안내
- **내용**:
  - 코드 에디터 사용법 안내
  - **추가 안내**: "코드에는 전체 HTML 문서 구조가 포함되어 있습니다. `<style>` 태그 안의 CSS 부분을 수정해보세요!"
  - 왼쪽에서 코드를 수정하면 오른쪽에 즉시 결과 반영
- **변경사항**: 통합 에디터 사용법에 맞게 안내 문구 수정

---

### 슬라이드 4: class와 id 개념 설명
- **제목**: class와 id란?
- **유형**: 개념 설명
- **내용**:
  - class: 여러 요소에 같은 이름을 붙일 수 있음 (`.클래스이름`으로 선택)
  - id: 하나의 요소에 고유한 이름을 붙임 (`#아이디이름`으로 선택)
  - 비유: class = "학년" (여러 명), id = "출석번호" (한 명)
  - 시각적 비교 표로 정리
- **학생 활동**: 설명을 읽고 이해

---

### 슬라이드 5: class와 id 실습
- **제목**: 식별자에 CSS 설정하기 실습
- **유형**: 실습 (통합 에디터)
- **실습 코드**:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>class와 id 실습</title>
  <style>
    /* 모든 .box 클래스에 적용 */
    .box {
      background-color: lightgray;
      padding: 10px;
      margin-bottom: 10px;
    }

    /* .highlight 클래스에만 적용 */
    .highlight {
      color: red;
      font-weight: bold;
    }

    /* #special 아이디에만 적용 */
    #special {
      background-color: gold;
      border: 2px dashed black;
    }
  </style>
</head>
<body>
  <div class="box">나는 일반 박스야!</div>
  <div class="box highlight">나는 강조된 박스야!</div>
  <div class="box" id="special">나는 특별한 아이디를 가진 박스야!</div>
  <div class="box">나도 그냥 박스야!</div>
</body>
</html>
```

- **학생 활동 지시사항**:
  1. `.highlight`의 `color`를 `blue`로 바꿔보세요
  2. 새로운 class `.big`을 만들어서 `font-size: 24px;`를 적용해보세요
  3. `#special`의 `background-color`를 다른 색으로 바꿔보세요

---

### 슬라이드 6: 자손 선택자와 자식 선택자 개념 설명
- **제목**: 자손 선택자와 자식 선택자
- **유형**: 개념 설명
- **내용**:
  - 자손 선택자 (`A B`): A 안에 있는 모든 B를 선택 (손자, 증손자 포함)
  - 자식 선택자 (`A > B`): A 바로 아래에 있는 B만 선택 (직계 자식만)
  - 시각적 트리 구조 다이어그램으로 차이 설명
  - 색상으로 어떤 요소가 선택되는지 표시
- **학생 활동**: 설명을 읽고 이해

---

### 슬라이드 7: 자손/자식 선택자 실습
- **제목**: 선택자 응용 실습
- **유형**: 실습 (통합 에디터)
- **실습 코드**:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>선택자 응용 실습</title>
  <style>
    /* .menu 안의 모든 li (자손 선택자) */
    .menu li {
      color: blue;
    }

    /* .menu 바로 아래 li만 (자식 선택자) */
    .menu > li {
      font-weight: bold;
      font-size: 20px;
    }

    /* 서브메뉴 글씨색을 바꿔보세요! */
  </style>
</head>
<body>
  <ul class="menu">
    <li>메뉴 1</li>
    <li>메뉴 2
      <ul>
        <li>서브메뉴 A</li>
        <li>서브메뉴 B</li>
      </ul>
    </li>
    <li>메뉴 3</li>
  </ul>
</body>
</html>
```

- **학생 활동 지시사항**:
  1. `.menu li`의 `color`를 `green`으로 바꿔보세요 → 모든 li가 변하는 것 확인
  2. `.menu > li`의 `color`를 `red`로 추가해보세요 → 1단계 li만 변하는 것 확인
  3. 서브메뉴만 `color: purple;`로 만들어보세요 (힌트: `.menu ul li`)

---

### 슬라이드 8: Margin과 Padding 개념 설명
- **제목**: 박스 모델의 핵심: Margin & Padding
- **유형**: 개념 설명
- **내용**:
  - 박스 모델 시각적 다이어그램 (content → padding → border → margin)
  - **padding**: 박스 안쪽 여백 (내용물과 테두리 사이)
  - **margin**: 박스 바깥쪽 여백 (요소 사이의 간격)
  - 비유: padding = "액자 안 여백", margin = "액자 사이 간격"
  - 방향 지정: `margin-top`, `margin-right`, `margin-bottom`, `margin-left`
  - 단축 표기: `margin: 10px 20px;` (상하 좌우)
- **학생 활동**: 설명을 읽고 이해

---

### 슬라이드 9: Margin과 Padding 실습
- **제목**: Margin & Padding 실습
- **유형**: 실습 (통합 에디터)
- **실습 코드**:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Margin과 Padding 실습</title>
  <style>
    .container {
      background-color: #f1f5f9;
      border: 2px solid #cbd5e1;
    }

    .box {
      background-color: #42a5f5;
      color: white;
      border: 2px solid #1565c0;
    }

    /* box1: 안쪽 여백 (padding) */
    .box1 {
      padding: 20px;
    }

    /* box2: 바깥 여백으로 중앙 정렬 */
    .box2 {
      margin: 30px auto;
      width: 150px;
      text-align: center;
    }

    /* box3: 위쪽 바깥 여백만 */
    .box3 {
      margin-top: 50px;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="box box1">Box 1 (padding)</div>
    <div class="box box2">Box 2 (margin)</div>
    <div class="box box3">Box 3 (margin-top)</div>
  </div>
</body>
</html>
```

- **학생 활동 지시사항**:
  1. `.box1`의 `padding`을 `5px`로 줄여보세요 → 안쪽 공간이 줄어드는 것 확인
  2. `.box2`의 `margin`을 `50px auto`로 바꿔보세요 → 위아래 간격 변화 확인
  3. `.box3`에 `padding: 30px;`을 추가해보세요 → margin과 padding의 차이 확인

---

### 슬라이드 10: Flexbox 개념 설명
- **제목**: Flexbox - 가로 세로 배치의 마법사
- **유형**: 개념 설명
- **내용**:
  - `display: flex;`를 부모 요소에 적용하면 자식들이 가로로 정렬됨
  - **flex-direction**: `row`(가로) / `column`(세로)
  - **justify-content**: 주축 정렬 (`flex-start`, `center`, `flex-end`, `space-between`, `space-around`)
  - **align-items**: 교차축 정렬 (`flex-start`, `center`, `flex-end`, `stretch`)
  - **gap**: 항목 사이 간격
  - 시각적 다이어그램으로 각 속성 효과 표시
- **학생 활동**: 설명을 읽고 이해

---

### 슬라이드 11: Flexbox 실습
- **제목**: Flexbox 배치 실습
- **유형**: 실습 (통합 에디터)
- **실습 코드**:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Flexbox 실습</title>
  <style>
    .flex-container {
      display: flex;
      flex-direction: row;
      gap: 15px;
      justify-content: flex-start;
      align-items: center;
      background-color: #e2e8f0;
      height: 200px;
      padding: 20px;
    }

    .item {
      background-color: #ff9800;
      color: white;
      padding: 20px;
      border-radius: 8px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="flex-container">
    <div class="item">Item 1</div>
    <div class="item">Item 2</div>
    <div class="item">Item 3</div>
    <div class="item">Item 4</div>
  </div>
</body>
</html>
```

- **학생 활동 지시사항**:
  1. `flex-direction`을 `column`으로 바꿔보세요 → 세로 배치 확인
  2. `justify-content`를 `center`로 바꿔보세요 → 가운데 정렬
  3. `justify-content`를 `space-between`으로 바꿔보세요 → 균등 분배
  4. `align-items`를 `flex-end`로 바꿔보세요 → 아래쪽 정렬

---

### 슬라이드 12: 최종 미션
- **제목**: 나만의 자기소개 페이지 완성하기
- **유형**: 과제
- **내용**:
  - 체크리스트:
    1. 지금까지 만들었던 자기소개 HTML 문서를 엽니다
    2. 오늘 배운 Margin과 Padding을 사용해 디자인 간격을 띄워주세요
    3. Flexbox (`display: flex`)를 이용하여 프로필 사진과 소개글을 나란히 배치해보세요
    4. `class` 또는 `id` 속성을 이용해서 포인트 컬러를 적용해주세요
  - 구글 폼 제출 링크
- **변경사항**: 기존과 동일

---

## 기술 구현 변경사항

### 에디터 구조 변경
```
기존:
editor-pane
  ├── pane-title: "HTML"
  ├── textarea.html-editor (HTML 코드 조각만)
  ├── pane-title: "CSS"
  └── textarea.css-editor (CSS 코드만)

변경:
editor-pane
  ├── pane-title: "코드 (수정해보세요)"
  └── textarea.code-editor (전체 HTML 문서)
```

### JavaScript 프리뷰 로직 변경
```javascript
// 기존: HTML과 CSS를 조합
function updatePreview(id) {
  const htmlCode = document.getElementById(`html-${id}`).value;
  const cssCode = document.getElementById(`css-${id}`).value;
  const content = "<!DOCTYPE html>..." + cssCode + "..." + htmlCode + "...";
  iframe.srcdoc = content;
}

// 변경: 전체 HTML 문서를 그대로 전달
function updatePreview(id) {
  const code = document.getElementById(`code-${id}`).value;
  iframe.srcdoc = code;
}
```

### 에디터 이벤트 리스너 변경
```javascript
// 기존: html-editor, css-editor 각각 리스닝
document.querySelectorAll('.html-editor, .css-editor').forEach(...)

// 변경: code-editor 하나만 리스닝
document.querySelectorAll('.code-editor').forEach(...)
```

---

## 요약: 기존 대비 변경 포인트

| 항목 | 기존 | 변경 |
|------|------|------|
| 슬라이드 수 | 8개 | 12개 |
| 에디터 구조 | HTML/CSS 분리 | 통합 (전체 HTML 문서) |
| 개념 설명 | 없음 (바로 실습) | 각 주제마다 설명 슬라이드 추가 |
| 실습 코드 | body 내부 조각 + CSS 조각 | 완전한 HTML 문서 |
| JS 프리뷰 로직 | 두 에디터 값 조합 | 단일 에디터 값 직접 전달 |
| 학생 활동 지시 | 없음 | 각 실습마다 단계별 지시사항 포함 |
