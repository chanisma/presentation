/**
 * AI로 자기평가문 작성하기 — Google Apps Script
 *
 * [설정 방법]
 * 1. Google 스프레드시트 열기
 * 2. 확장 프로그램 → Apps Script
 * 3. 이 파일 내용 전체 붙여넣기
 * 4. 배포 → 새 배포 → 웹 앱
 *    - 실행 계정: 나
 *    - 액세스 권한: 모든 사용자 (익명 포함)  ← 반드시 이것
 * 5. 배포 URL을 활동지.html 의 ⚙ 버튼 → URL 저장
 */

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    var ss    = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName('자기평가문활동지') || ss.insertSheet('자기평가문활동지');

    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        '제출시각', '이름', '반/번호', '날짜',
        // STEP 1
        '과목', '활동명', '활동시기',
        // STEP 2
        '①무엇을했나', '②어떻게했나', '③배운점', '④느낀점',
        // STEP 3
        '역할Role', '맥락Context', '과제Task', '형식Format',
        // STEP 4
        '고급기법', '기법적용내용',
        // STEP 5
        'AI초안', '수정오류', '추가내용', '최종자기평가문',
        // 성찰
        '효과적기법', '개선점', 'AI와나의역할'
      ]);
      var h = sheet.getRange(1, 1, 1, 23);
      h.setBackground('#F27321');
      h.setFontColor('#FFFFFF');
      h.setFontWeight('bold');
      sheet.setFrozenRows(1);
    }

    // 고급 기법 적용 내용 (선택된 기법에 따라 내용 선택)
    var advContent = data.advEx1 || data.advEx2 || data.advEx3 || '';

    sheet.appendRow([
      new Date().toLocaleString('ko-KR'),
      data.studentName    || '',
      data.classInfo      || '',
      data.today          || '',
      data.subject        || '',
      data.activityName   || '',
      data.activityDate   || '',
      data.memo1          || '',
      data.memo2          || '',
      data.memo3          || '',
      data.memo4          || '',
      data.elemRole       || '',
      data.elemContext    || '',
      data.elemTask       || '',
      data.elemFormat     || '',
      data.advTech        || '',
      advContent,
      data.aiDraft        || '',
      data.fixError       || '',
      data.fixAdd         || '',
      data.finalText      || '',
      data.reflect1       || '',
      data.reflect2       || '',
      data.reflect3       || ''
    ]);

    return ContentService
      .createTextOutput(JSON.stringify({ status: 'ok' }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: err.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
