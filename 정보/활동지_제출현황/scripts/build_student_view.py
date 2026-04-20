import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "data" / "submission_report.json"
HTML_OUT = ROOT / "활동지_내제출확인.html"

with JSON_PATH.open(encoding="utf-8") as f:
    data = json.load(f)

data_json = json.dumps(data, ensure_ascii=False)
generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

HTML = r"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>나의 활동지 제출 현황</title>
<style>
  * { box-sizing: border-box; }
  body { font-family: "Malgun Gothic", -apple-system, BlinkMacSystemFont, sans-serif; margin: 0; padding: 20px; background: #f5f6f8; color: #1f2937; }
  .wrap { max-width: 720px; margin: 0 auto; }
  h1 { margin: 0 0 6px 0; font-size: 22px; text-align: center; }
  .subtitle { color: #6b7280; font-size: 13px; text-align: center; margin-bottom: 20px; }
  .card { background: #fff; border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; box-shadow: 0 2px 6px rgba(0,0,0,.04); }
  .login-form { display: grid; grid-template-columns: 1fr; gap: 12px; }
  .login-row { display: grid; grid-template-columns: 90px 1fr; gap: 10px; align-items: center; }
  .login-row label { font-weight: 600; color: #374151; font-size: 14px; }
  .login-form input, .login-form select { padding: 10px 12px; border: 1px solid #d1d5db; border-radius: 8px; font-size: 15px; width: 100%; }
  .login-form input:focus, .login-form select:focus { outline: 2px solid #3b82f6; outline-offset: 1px; }
  .btn { padding: 12px 18px; border-radius: 8px; border: none; background: #3b82f6; color: #fff; font-size: 15px; font-weight: 600; cursor: pointer; width: 100%; margin-top: 6px; }
  .btn:hover { background: #2563eb; }
  .btn-secondary { background: #e5e7eb; color: #374151; width: auto; padding: 8px 14px; font-size: 13px; margin: 0; }
  .btn-secondary:hover { background: #d1d5db; }
  .error { background: #fee2e2; color: #991b1b; padding: 10px 14px; border-radius: 8px; font-size: 13px; margin-top: 10px; display: none; }
  .hidden { display: none !important; }
  .student-info { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid #e5e7eb; }
  .student-info .name { font-size: 20px; font-weight: 700; color: #111827; }
  .student-info .meta { color: #6b7280; font-size: 13px; margin-top: 2px; }
  .summary { background: #f9fafb; border-radius: 8px; padding: 12px 16px; margin-bottom: 16px; font-size: 13px; }
  .summary strong { color: #111827; }
  .sheet-list { display: grid; gap: 10px; }
  .sheet-row { display: grid; grid-template-columns: 1fr auto; gap: 10px; padding: 14px 16px; border-radius: 10px; border: 1px solid #e5e7eb; background: #fff; align-items: center; }
  .sheet-row.submitted { border-left: 4px solid #22c55e; background: #f0fdf4; }
  .sheet-row.missing { border-left: 4px solid #ef4444; background: #fef2f2; }
  .sheet-row.thin { border-left: 4px solid #f59e0b; background: #fffbeb; }
  .sheet-name { font-weight: 600; font-size: 15px; color: #111827; }
  .sheet-detail { color: #6b7280; font-size: 12px; margin-top: 3px; }
  .status { font-weight: 700; font-size: 14px; white-space: nowrap; }
  .status.ok { color: #16a34a; }
  .status.no { color: #dc2626; }
  .status.warn { color: #d97706; }
  .times-list { list-style: none; margin: 6px 0 0 0; padding: 0; font-size: 12px; color: #4b5563; }
  .times-list li { padding: 2px 0; }
  .times-list .thin-mark { color: #d97706; font-weight: 600; }
  .foot { text-align: center; margin-top: 16px; color: #6b7280; font-size: 12px; }
</style>
</head>
<body>
<div class="wrap">
  <h1>나의 활동지 제출 현황</h1>
  <div class="subtitle">본인의 반 · 번호 · 이름을 입력하면 제출 기록을 확인할 수 있어요<br><span style="font-size:11px; color:#9ca3af;">집계 기준: __GENERATED_AT__</span></div>

  <div class="card" id="loginCard">
    <div class="login-form">
      <div class="login-row">
        <label for="classInput">반</label>
        <select id="classInput">
          <option value="">선택</option>
        </select>
      </div>
      <div class="login-row">
        <label for="numberInput">번호</label>
        <input type="number" id="numberInput" min="1" max="30" placeholder="예: 13">
      </div>
      <div class="login-row">
        <label for="nameInput">이름</label>
        <input type="text" id="nameInput" placeholder="예: 홍길동">
      </div>
      <button class="btn" id="loginBtn">확인하기</button>
      <div class="error" id="errorMsg"></div>
    </div>
  </div>

  <div class="card hidden" id="resultCard">
    <div class="student-info">
      <div>
        <div class="name" id="resName"></div>
        <div class="meta" id="resMeta"></div>
      </div>
      <button class="btn btn-secondary" id="backBtn">← 다시 조회</button>
    </div>
    <div class="summary" id="resSummary"></div>
    <div class="sheet-list" id="resSheets"></div>
    <div class="foot">⚠ 빈약: 100자 미만 제출 · 여러 번 제출 시 모든 기록이 표시됩니다</div>
  </div>
</div>

<script>
const DATA = __DATA__;
const SHEETS = ["인공지능시대", "대형언어모델", "자기평가문", "에이전틱AI", "이미지분류"];
const THIN_THRESHOLD = 100;

function formatTime(iso) {
  if (!iso) return "";
  const d = new Date(iso);
  if (isNaN(d)) return iso;
  const pad = n => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}`;
}

function populateClasses() {
  const sel = document.getElementById("classInput");
  const classes = [...new Set(DATA.map(d => d.class))].sort((a,b)=>a-b);
  for (const c of classes) {
    const opt = document.createElement("option");
    opt.value = c;
    opt.textContent = `${c}반`;
    sel.appendChild(opt);
  }
}

function showError(msg) {
  const e = document.getElementById("errorMsg");
  e.textContent = msg;
  e.style.display = "block";
}

function hideError() {
  document.getElementById("errorMsg").style.display = "none";
}

function login() {
  hideError();
  const cls = document.getElementById("classInput").value;
  const num = document.getElementById("numberInput").value;
  const name = document.getElementById("nameInput").value.trim();

  if (!cls) return showError("반을 선택해 주세요.");
  if (!num) return showError("번호를 입력해 주세요.");
  if (!name) return showError("이름을 입력해 주세요.");

  const student = DATA.find(d =>
    d.class === parseInt(cls, 10) &&
    d.number === parseInt(num, 10) &&
    d.name === name
  );

  if (!student) {
    return showError("반/번호/이름이 일치하는 학생을 찾을 수 없어요. 다시 확인해 주세요.");
  }

  renderResult(student);
}

function renderResult(student) {
  document.getElementById("loginCard").classList.add("hidden");
  document.getElementById("resultCard").classList.remove("hidden");

  document.getElementById("resName").textContent = student.name;
  document.getElementById("resMeta").textContent = `${student.class}반 ${student.number}번`;

  const submittedCount = SHEETS.filter(s => student.sheets[s].count > 0).length;
  const missing = SHEETS.filter(s => student.sheets[s].count === 0);
  const thinSheets = SHEETS.filter(s => (student.sheets[s].chars || []).some(c => c < THIN_THRESHOLD));

  let summary = `총 <strong>${SHEETS.length}개</strong> 활동지 중 <strong>${submittedCount}개</strong> 제출 완료`;
  if (missing.length > 0) {
    summary += ` · 미제출 <strong style="color:#dc2626">${missing.length}개</strong>`;
  }
  if (thinSheets.length > 0) {
    summary += ` · 빈약 제출 <strong style="color:#d97706">${thinSheets.length}개</strong>`;
  }
  if (missing.length === 0 && thinSheets.length === 0) {
    summary = `🎉 모든 활동지를 잘 제출했어요!`;
  }
  document.getElementById("resSummary").innerHTML = summary;

  const container = document.getElementById("resSheets");
  container.innerHTML = "";

  for (const s of SHEETS) {
    const info = student.sheets[s];
    const chars = info.chars || [];
    const times = info.times || [];
    const hasThin = chars.some(c => c < THIN_THRESHOLD);

    const row = document.createElement("div");
    row.className = "sheet-row";
    if (info.count === 0) row.classList.add("missing");
    else if (hasThin) row.classList.add("thin");
    else row.classList.add("submitted");

    const left = document.createElement("div");
    const name = document.createElement("div");
    name.className = "sheet-name";
    name.textContent = s;
    left.appendChild(name);

    if (info.count > 0) {
      const list = document.createElement("ul");
      list.className = "times-list";
      times.forEach((t, i) => {
        const c = chars[i] ?? 0;
        const li = document.createElement("li");
        li.textContent = `${formatTime(t)} · ${c}자`;
        if (c < THIN_THRESHOLD) {
          const mark = document.createElement("span");
          mark.className = "thin-mark";
          mark.textContent = " ⚠ 빈약";
          li.appendChild(mark);
        }
        list.appendChild(li);
      });
      left.appendChild(list);
    } else {
      const detail = document.createElement("div");
      detail.className = "sheet-detail";
      detail.textContent = "제출 기록이 없어요.";
      left.appendChild(detail);
    }
    row.appendChild(left);

    const status = document.createElement("div");
    status.className = "status";
    if (info.count === 0) {
      status.classList.add("no");
      status.textContent = "미제출";
    } else if (hasThin) {
      status.classList.add("warn");
      status.textContent = info.count === 1 ? "⚠ 확인 필요" : `✓ ${info.count}회 (일부 빈약)`;
    } else {
      status.classList.add("ok");
      status.textContent = info.count === 1 ? "✓ 제출" : `✓ ${info.count}회 제출`;
    }
    row.appendChild(status);

    container.appendChild(row);
  }
}

function reset() {
  document.getElementById("resultCard").classList.add("hidden");
  document.getElementById("loginCard").classList.remove("hidden");
  document.getElementById("nameInput").value = "";
  document.getElementById("numberInput").value = "";
  document.getElementById("classInput").value = "";
  hideError();
}

populateClasses();
document.getElementById("loginBtn").addEventListener("click", login);
document.getElementById("backBtn").addEventListener("click", reset);

// Enter key on any field submits
document.querySelectorAll("#classInput, #numberInput, #nameInput").forEach(el => {
  el.addEventListener("keydown", e => { if (e.key === "Enter") login(); });
});
</script>
</body>
</html>
"""

html_content = HTML.replace("__DATA__", data_json).replace("__GENERATED_AT__", generated_at)
HTML_OUT.write_text(html_content, encoding="utf-8")
print(f"Written: {HTML_OUT} ({len(html_content)} chars)")
