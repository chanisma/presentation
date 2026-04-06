/**
 * 에이전틱 AI 체험 활동지 — Google Apps Script
 *
 * [설정 방법]
 * 1. Google 스프레드시트 열기
 * 2. 확장 프로그램 → Apps Script
 * 3. 이 파일 내용 전체 붙여넣기
 * 4. 배포 → 새 배포 → 웹 앱
 *    - 실행 계정: 나
 *    - 액세스 권한: 모든 사용자 (익명 포함)  ← 반드시 이것
 * 5. 배포 URL을 활동지.html 의 DEFAULT_URL 에 붙여넣기
 *    또는 활동지 오른쪽 상단 ⚙ 버튼 → URL 저장
 */

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    var ss    = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName('활동지') || ss.insertSheet('활동지');

    // 첫 실행 시 헤더 자동 생성
    if (sheet.getLastRow() === 0) {
      sheet.appendRow([
        '제출시각', '이름', '반/번호', '날짜',
        // STEP 1
        '소스1', '소스2', '소스3', 'AI처리관찰',
        // STEP 2 미션①
        '미션①핵심개념', '미션①완성도', '미션①관찰메모',
        // STEP 2 미션②
        '미션②산출물유형', '미션②인상적문항', '미션②완성도', '미션②관찰메모',
        // STEP 2 미션③
        '미션③산출물유형', '미션③핵심내용', '미션③완성도', '미션③관찰메모',
        // STEP 3
        'Q1최고산출물', 'Q1이유',
        'Q2오류여부', 'Q2틀린내용', 'Q2누락내용',
        'Q3판단', 'Q3이유',
        // 정리
        '정리①감지', '정리②판단', '정리③행동', '인간의역할'
      ]);
      // 헤더 스타일
      var headerRange = sheet.getRange(1, 1, 1, 30);
      headerRange.setBackground('#2563EB');
      headerRange.setFontColor('#FFFFFF');
      headerRange.setFontWeight('bold');
      sheet.setFrozenRows(1);
    }

    sheet.appendRow([
      new Date().toLocaleString('ko-KR'),
      data.studentName  || '',
      data.classInfo    || '',
      data.today        || '',
      data.src1         || '',
      data.src2         || '',
      data.src3         || '',
      data.srcObserve   || '',
      data.m1output     || '',
      data.m1stars      || 0,
      data.m1memo       || '',
      data.m2type       || '',
      data.m2output     || '',
      data.m2stars      || 0,
      data.m2memo       || '',
      data.m3type       || '',
      data.m3output     || '',
      data.m3stars      || 0,
      data.m3memo       || '',
      data.q1best       || '',
      data.q1reason     || '',
      data.q2error      || '',
      data.q2wrong      || '',
      data.q2missing    || '',
      data.q3verdict    || '',
      data.q3reason     || '',
      data.step1summary || '',
      data.step2summary || '',
      data.step3summary || '',
      data.humanRole    || ''
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
