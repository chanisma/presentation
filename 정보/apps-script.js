/**
 * 정보 과목 활동지 — Google Apps Script (과목 공용)
 *
 * 이 스크립트 하나로 정보 과목의 모든 활동지 데이터를 받아
 * 활동지 종류(source)에 따라 각기 다른 시트 탭에 자동 저장합니다.
 *
 * [등록된 활동지]
 *   - 'writing-prompt' (기본) → 자기평가문활동지 시트
 *   - 'notebooklm'            → 에이전틱AI활동지 시트
 *   - 'deeplearning'          → 딥러닝기초활동지 시트 (이미지 3장 → Drive 저장)
 *
 * [새 활동지 추가 방법]
 *   1. 활동지 HTML의 getFormData()에 source: '식별자' 추가
 *   2. 아래 doPost()에 else if (data.source === '식별자') 블록 추가
 *   3. 재배포 (배포 관리 → 새 버전)
 *
 * [최초 설정]
 * 1. Google 스프레드시트 열기
 * 2. 확장 프로그램 → Apps Script
 * 3. 이 파일 내용 전체 붙여넣기
 * 4. 배포 → 새 배포 → 웹 앱
 *    - 실행 계정: 나
 *    - 액세스 권한: 모든 사용자 (익명 포함) ← 반드시 이것
 * 5. 배포 URL을 각 활동지.html 의 ⚙ 버튼 → URL 저장
 *    (모든 활동지가 동일한 URL을 사용)
 */

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    var ss   = SpreadsheetApp.getActiveSpreadsheet();

    if (data.source === 'deeplearning') {
      // ── 딥러닝 기초 활동지 (이미지 3장 포함) ──
      var sheet3 = ss.getSheetByName('딥러닝기초활동지') || ss.insertSheet('딥러닝기초활동지');
      if (sheet3.getLastRow() === 0) {
        sheet3.appendRow([
          '제출시각', '이름', '반/번호', '날짜',
          '테스트결과1', '테스트결과2', '테스트결과3',
          'Q1_틀린이유', 'Q2_데이터양', 'Q3_고양이', 'Q4_전이학습'
        ]);
        var h3 = sheet3.getRange(1, 1, 1, 11);
        h3.setBackground('#1E2033');
        h3.setFontColor('#FFFFFF');
        h3.setFontWeight('bold');
        sheet3.setFrozenRows(1);
      }

      // 이미지 처리 (최대 3장)
      var imgUrl1 = data.image1 ? saveImageToDrive(data.image1, (data.studentName || 'unknown') + '_1') : '';
      var imgUrl2 = data.image2 ? saveImageToDrive(data.image2, (data.studentName || 'unknown') + '_2') : '';
      var imgUrl3 = data.image3 ? saveImageToDrive(data.image3, (data.studentName || 'unknown') + '_3') : '';

      sheet3.appendRow([
        new Date().toLocaleString('ko-KR'),
        data.studentName || '',
        data.classInfo   || '',
        data.today       || '',
        imgUrl1 ? '=IMAGE("' + imgUrl1 + '")' : '',
        imgUrl2 ? '=IMAGE("' + imgUrl2 + '")' : '',
        imgUrl3 ? '=IMAGE("' + imgUrl3 + '")' : '',
        data.q1 || '',
        data.q2 || '',
        data.q3 || '',
        data.q4 || ''
      ]);

      // 이미지가 있으면 행 높이 키우기
      if (imgUrl1 || imgUrl2 || imgUrl3) {
        sheet3.setRowHeight(sheet3.getLastRow(), 150);
      }

    } else if (data.source === 'notebooklm') {
      // ── 에이전틱AI·NotebookLM 활동지 ──
      var sheet2 = ss.getSheetByName('에이전틱AI활동지') || ss.insertSheet('에이전틱AI활동지');
      if (sheet2.getLastRow() === 0) {
        sheet2.appendRow([
          '제출시각', '이름', '반/번호', '날짜',
          '소스1', '소스2', '소스3', '소스관찰',
          '미션1산출물', '미션1별점', '미션1메모',
          '미션2유형', '미션2산출물', '미션2별점', '미션2메모',
          '미션3유형', '미션3산출물', '미션3별점', '미션3메모',
          'Q1최고미션', 'Q1이유',
          'Q2오류여부', 'Q2틀린내용', 'Q2누락내용',
          'Q3판정', 'Q3이유',
          '단계1요약', '단계2요약', '단계3요약', '인간의역할'
        ]);
        var h2 = sheet2.getRange(1, 1, 1, 30);
        h2.setBackground('#1B7ED4');
        h2.setFontColor('#FFFFFF');
        h2.setFontWeight('bold');
        sheet2.setFrozenRows(1);
      }
      sheet2.appendRow([
        new Date().toLocaleString('ko-KR'),
        data.studentName   || '',
        data.classInfo     || '',
        data.today         || '',
        data.src1          || '',
        data.src2          || '',
        data.src3          || '',
        data.srcObserve    || '',
        data.m1output      || '',
        data.m1stars       || '',
        data.m1memo        || '',
        data.m2type        || '',
        data.m2output      || '',
        data.m2stars       || '',
        data.m2memo        || '',
        data.m3type        || '',
        data.m3output      || '',
        data.m3stars       || '',
        data.m3memo        || '',
        data.q1best        || '',
        data.q1reason      || '',
        data.q2error       || '',
        data.q2wrong       || '',
        data.q2missing     || '',
        data.q3verdict     || '',
        data.q3reason      || '',
        data.step1summary  || '',
        data.step2summary  || '',
        data.step3summary  || '',
        data.humanRole     || ''
      ]);

    } else {
      // ── 글쓰기 프롬프트 설계 활동지 (기본) ──
      var sheet = ss.getSheetByName('자기평가문활동지') || ss.insertSheet('자기평가문활동지');
      if (sheet.getLastRow() === 0) {
        sheet.appendRow([
          '제출시각', '이름', '반/번호', '날짜',
          '과목', '활동명', '활동시기',
          '①무엇을했나', '②어떻게했나', '③배운점', '④느낀점',
          '역할Role', '맥락Context', '과제Task', '형식Format',
          '고급기법', '기법적용내용',
          'AI초안', '수정오류', '추가내용', '최종자기평가문',
          '효과적기법', '개선점', 'AI와나의역할'
        ]);
        var h = sheet.getRange(1, 1, 1, 24);
        h.setBackground('#F27321');
        h.setFontColor('#FFFFFF');
        h.setFontWeight('bold');
        sheet.setFrozenRows(1);
      }
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
    }

    return ContentService
      .createTextOutput(JSON.stringify({ status: 'ok' }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: err.message }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * base64 이미지를 Google Drive에 저장하고 공유 URL 반환
 * @param {string} base64String - "data:image/jpeg;base64,..." 형태
 * @param {string} prefix - 파일명 앞에 붙일 구분자 (학번 등)
 */
function saveImageToDrive(base64String, prefix) {
  var match = base64String.match(/^data:([^;]+);base64,(.+)$/);
  if (!match) return '';

  var mimeType = match[1];
  var ext = mimeType.split('/')[1] === 'jpeg' ? 'jpg' : mimeType.split('/')[1];
  var blob = Utilities.newBlob(
    Utilities.base64Decode(match[2]),
    mimeType,
    prefix + '_' + new Date().getTime() + '.' + ext
  );

  var file = DriveApp.createFile(blob);
  file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
  return file.getUrl();
}
