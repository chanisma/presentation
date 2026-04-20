import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "data" / "submission_report.json"
HTML_OUT = ROOT / "활동지_제출현황.html"

with JSON_PATH.open(encoding="utf-8") as f:
    data = json.load(f)

data_json = json.dumps(data, ensure_ascii=False)
generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

HTML = r"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>2026 정보 활동지 제출 현황</title>
<style>
  * { box-sizing: border-box; }
  body { font-family: "Malgun Gothic", -apple-system, BlinkMacSystemFont, sans-serif; margin: 0; padding: 16px; background: #f5f6f8; color: #1f2937; }
  h1 { margin: 0 0 8px 0; font-size: 20px; }
  .subtitle { color: #6b7280; font-size: 13px; margin-bottom: 12px; }
  .controls { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 12px; align-items: center; }
  .controls input, .controls select { padding: 6px 10px; border: 1px solid #d1d5db; border-radius: 6px; font-size: 13px; background: #fff; }
  .stats { display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 12px; }
  .stat { background: #fff; border: 1px solid #e5e7eb; border-radius: 8px; padding: 8px 14px; min-width: 120px; }
  .stat .label { color: #6b7280; font-size: 11px; text-transform: uppercase; letter-spacing: .05em; }
  .stat .value { font-weight: 600; font-size: 18px; color: #111827; }
  .stat .sub { color: #6b7280; font-size: 11px; margin-top: 2px; }
  table { border-collapse: collapse; background: #fff; width: 100%; font-size: 12px; box-shadow: 0 1px 2px rgba(0,0,0,.04); }
  th, td { border: 1px solid #e5e7eb; padding: 6px 8px; vertical-align: middle; text-align: center; white-space: nowrap; }
  th { background: #f9fafb; color: #374151; font-weight: 600; position: sticky; top: 0; z-index: 5; cursor: pointer; user-select: none; }
  th:hover { background: #f3f4f6; }
  tr:hover td { background: #f9fafb; }
  .name-cell { text-align: left; font-weight: 500; }
  .cell-submitted { background: #dcfce7; cursor: pointer; }
  .cell-submitted:hover { background: #bbf7d0; }
  .cell-missing { background: #fee2e2; color: #991b1b; }
  .cell-multi { background: #dbeafe; cursor: pointer; }
  .cell-multi:hover { background: #bfdbfe; }
  .cell-thin { box-shadow: inset 0 0 0 2px #f59e0b; }
  .thin-badge { display: inline-block; padding: 1px 4px; background: #f59e0b; color: #fff; border-radius: 4px; font-size: 9px; margin-left: 3px; font-weight: 700; }
  .count-badge { display: inline-block; min-width: 18px; padding: 1px 5px; border-radius: 10px; background: rgba(0,0,0,.1); font-size: 10px; margin-left: 4px; font-weight: 600; }
  .dup-row { background: #fef3c7 !important; }
  .dup-cell { background: #fcd34d; }
  .tooltip { position: fixed; background: #1f2937; color: #fff; padding: 8px 10px; border-radius: 6px; font-size: 11px; max-width: 320px; z-index: 1000; box-shadow: 0 4px 12px rgba(0,0,0,.2); pointer-events: none; display: none; white-space: pre-line; }
  .sheet-filter { display: flex; gap: 4px; flex-wrap: wrap; }
  .sheet-filter label { display: inline-flex; align-items: center; gap: 4px; padding: 4px 8px; background: #fff; border: 1px solid #d1d5db; border-radius: 6px; font-size: 12px; cursor: pointer; }
  .sheet-filter input { margin: 0; }
  .legend { display: inline-flex; gap: 10px; font-size: 11px; color: #6b7280; align-items: center; flex-wrap: wrap; }
  .legend span { display: inline-flex; align-items: center; gap: 4px; }
  .swatch { width: 12px; height: 12px; border-radius: 3px; border: 1px solid #e5e7eb; }
</style>
</head>
<body>
<h1>2026 정보 활동지 제출 현황</h1>
<div class="subtitle">1학년 전체 <span id="totalStudents"></span>명 · <span id="sheetCount"></span>개 시트 · 집계 기준 <span id="lastDate"></span></div>

<div class="stats" id="stats"></div>

<div class="controls">
  <input type="search" id="search" placeholder="이름 / 반 / 번호 검색" style="width: 220px;">
  <select id="filterSubmission">
    <option value="all">전체</option>
    <option value="any-missing">미제출 있음</option>
    <option value="all-submitted">모두 제출</option>
    <option value="duplicate">동일 결과물 있음</option>
    <option value="thin">빈약한 제출 있음</option>
  </select>
  <select id="classFilter">
    <option value="">전체 반</option>
  </select>
  <div class="legend">
    <span><div class="swatch" style="background:#dcfce7"></div>제출</span>
    <span><div class="swatch" style="background:#dbeafe"></div>복수 제출</span>
    <span><div class="swatch" style="background:#fee2e2"></div>미제출</span>
    <span><div class="swatch" style="background:#fef3c7"></div>중복 결과물</span>
    <span><div class="swatch" style="box-shadow: inset 0 0 0 2px #f59e0b; background: #fff;"></div>빈약 제출 (&lt;100자)</span>
  </div>
</div>

<table id="tbl">
  <thead>
    <tr id="thead-row"></tr>
  </thead>
  <tbody id="tbody"></tbody>
</table>

<div id="tooltip" class="tooltip"></div>

<script>
const DATA = __DATA__;
const SHEETS = ["인공지능시대", "대형언어모델", "자기평가문", "에이전틱AI", "이미지분류"];
const THIN_THRESHOLD = 100;

function formatTime(iso) {
  if (!iso) return "";
  const d = new Date(iso);
  if (isNaN(d)) return iso;
  const pad = n => String(n).padStart(2, "0");
  return `${d.getMonth()+1}/${d.getDate()} ${pad(d.getHours())}:${pad(d.getMinutes())}`;
}

function buildHead() {
  const tr = document.getElementById("thead-row");
  const cols = [
    { key: "class", label: "반" },
    { key: "number", label: "번호" },
    { key: "name", label: "이름" },
  ];
  for (const s of SHEETS) cols.push({ key: `sheet_${s}`, label: s });
  cols.push({ key: "duplicate_groups", label: "동일결과물" });
  for (const c of cols) {
    const th = document.createElement("th");
    th.textContent = c.label;
    th.dataset.key = c.key;
    tr.appendChild(th);
  }
}

let sortKey = "class", sortAsc = true;

function render() {
  const q = document.getElementById("search").value.trim().toLowerCase();
  const mode = document.getElementById("filterSubmission").value;
  const classVal = document.getElementById("classFilter").value;

  const tbody = document.getElementById("tbody");
  tbody.innerHTML = "";

  let filtered = DATA.filter(d => {
    if (classVal && String(d.class) !== classVal) return false;
    if (q) {
      const hay = `${d.class} ${d.number} ${d.name} ${d.class}반 ${d.number}번`.toLowerCase();
      if (!hay.includes(q)) return false;
    }
    const submittedSheets = SHEETS.filter(s => d.sheets[s].count > 0).length;
    const totalRequired = SHEETS.length;
    if (mode === "any-missing" && submittedSheets === totalRequired) return false;
    if (mode === "all-submitted" && submittedSheets !== totalRequired) return false;
    if (mode === "duplicate" && Object.keys(d.duplicate_groups).length === 0) return false;
    if (mode === "thin") {
      const hasThin = SHEETS.some(s => (d.sheets[s].chars || []).some(c => c < THIN_THRESHOLD));
      if (!hasThin) return false;
    }
    return true;
  });

  filtered.sort((a, b) => {
    let av, bv;
    if (sortKey.startsWith("sheet_")) {
      const s = sortKey.slice(6);
      av = a.sheets[s].count; bv = b.sheets[s].count;
    } else if (sortKey === "duplicate_groups") {
      av = Object.keys(a.duplicate_groups).length;
      bv = Object.keys(b.duplicate_groups).length;
    } else {
      av = a[sortKey]; bv = b[sortKey];
    }
    if (av === bv) {
      // secondary sort
      if (a.class !== b.class) return a.class - b.class;
      return a.number - b.number;
    }
    if (typeof av === "string") return sortAsc ? av.localeCompare(bv) : bv.localeCompare(av);
    return sortAsc ? av - bv : bv - av;
  });

  for (const d of filtered) {
    const tr = document.createElement("tr");
    const hasDup = Object.keys(d.duplicate_groups).length > 0;
    if (hasDup) tr.classList.add("dup-row");

    const addTd = (txt, cls) => {
      const td = document.createElement("td");
      td.textContent = txt;
      if (cls) td.className = cls;
      tr.appendChild(td);
      return td;
    };

    addTd(d.class);
    addTd(d.number);
    const nameTd = addTd(d.name, "name-cell");
    nameTd.textContent = d.name;

    for (const s of SHEETS) {
      const info = d.sheets[s];
      const td = document.createElement("td");
      const chars = info.chars || [];
      const hasThin = chars.some(c => c < THIN_THRESHOLD);
      const detailLines = (info.times || []).map((t, i) => {
        const c = chars[i] ?? 0;
        const mark = c < THIN_THRESHOLD ? " ⚠" : "";
        return `${formatTime(t)} (${c}자${mark})`;
      });
      if (info.count === 0) {
        td.className = "cell-missing";
        td.textContent = "-";
      } else if (info.count === 1) {
        td.className = "cell-submitted";
        td.innerHTML = hasThin ? `✓<span class="thin-badge">${chars[0]}</span>` : "✓";
        td.dataset.tooltip = `[${s}]\n${detailLines.join("\n")}`;
      } else {
        td.className = "cell-multi";
        const minChars = Math.min(...chars);
        td.innerHTML = `✓<span class="count-badge">${info.count}</span>` + (hasThin ? `<span class="thin-badge">${minChars}</span>` : "");
        td.dataset.tooltip = `[${s}] ${info.count}회 제출\n` + detailLines.join("\n");
      }
      if (hasThin) td.classList.add("cell-thin");
      tr.appendChild(td);
    }

    const dupTd = document.createElement("td");
    if (hasDup) {
      dupTd.className = "dup-cell";
      const entries = Object.entries(d.duplicate_groups);
      dupTd.textContent = entries.map(([k,v]) => `${k}(${v.length})`).join(", ");
      dupTd.dataset.tooltip = entries.map(([k,v]) => `[${k}]\n${v.join("\n")}`).join("\n\n");
    } else {
      dupTd.textContent = "";
    }
    tr.appendChild(dupTd);
    tbody.appendChild(tr);
  }
  document.getElementById("countInfo") && (document.getElementById("countInfo").textContent = `${filtered.length}명 표시`);
  updateStats(filtered);
}

function updateStats(filtered) {
  const statsEl = document.getElementById("stats");
  statsEl.innerHTML = "";
  const mk = (label, value, sub) => {
    const d = document.createElement("div");
    d.className = "stat";
    d.innerHTML = `<div class="label">${label}</div><div class="value">${value}</div>${sub ? `<div class="sub">${sub}</div>` : ""}`;
    statsEl.appendChild(d);
  };
  mk("표시 학생", filtered.length, `전체 ${DATA.length}명 중`);
  for (const s of SHEETS) {
    const submitted = filtered.filter(d => d.sheets[s].count > 0).length;
    const multi = filtered.filter(d => d.sheets[s].count > 1).length;
    const totalSubs = filtered.reduce((a, d) => a + d.sheets[s].count, 0);
    const thinSubs = filtered.reduce((a, d) => a + (d.sheets[s].chars || []).filter(c => c < THIN_THRESHOLD).length, 0);
    const thinStr = thinSubs > 0 ? `, 빈약 ${thinSubs}회` : "";
    mk(s, `${submitted}/${filtered.length}`, `제출 ${totalSubs}회, 복수 ${multi}명${thinStr}`);
  }
}

function populateClassFilter() {
  const sel = document.getElementById("classFilter");
  const classes = [...new Set(DATA.map(d => d.class))].sort((a,b)=>a-b);
  for (const c of classes) {
    const opt = document.createElement("option");
    opt.value = c;
    opt.textContent = `${c}반`;
    sel.appendChild(opt);
  }
}

document.getElementById("totalStudents").textContent = DATA.length;
document.getElementById("sheetCount").textContent = SHEETS.length;
document.getElementById("lastDate").textContent = "__GENERATED_AT__";
buildHead();
populateClassFilter();

document.getElementById("search").addEventListener("input", render);
document.getElementById("filterSubmission").addEventListener("change", render);
document.getElementById("classFilter").addEventListener("change", render);

document.getElementById("thead-row").addEventListener("click", (e) => {
  if (e.target.tagName !== "TH") return;
  const key = e.target.dataset.key;
  if (sortKey === key) sortAsc = !sortAsc;
  else { sortKey = key; sortAsc = true; }
  render();
});

// Tooltip
const tooltip = document.getElementById("tooltip");
document.addEventListener("mouseover", (e) => {
  const t = e.target.closest("[data-tooltip]");
  if (!t) return;
  tooltip.textContent = t.dataset.tooltip;
  tooltip.style.display = "block";
});
document.addEventListener("mousemove", (e) => {
  if (tooltip.style.display !== "block") return;
  const pad = 12;
  let x = e.clientX + pad, y = e.clientY + pad;
  const w = tooltip.offsetWidth, h = tooltip.offsetHeight;
  if (x + w > window.innerWidth - 8) x = e.clientX - w - pad;
  if (y + h > window.innerHeight - 8) y = e.clientY - h - pad;
  tooltip.style.left = x + "px";
  tooltip.style.top = y + "px";
});
document.addEventListener("mouseout", (e) => {
  if (!e.target.closest("[data-tooltip]")) tooltip.style.display = "none";
});

render();
</script>
</body>
</html>
"""

html_content = HTML.replace("__DATA__", data_json).replace("__GENERATED_AT__", generated_at)
HTML_OUT.write_text(html_content, encoding="utf-8")
print(f"Written: {HTML_OUT} ({len(html_content)} chars)")
