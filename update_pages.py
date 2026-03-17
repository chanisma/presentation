import json

file_path = 'c:/Users/chani/presentation/pages.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_page = {
    "title": "YOLO - You Only Look Once",
    "path": "인공지능과피지컬컴퓨팅/YOLO/index.html",
    "emoji": "🤖",
    "description": "YOLO의 개념과 CNN과의 연관성, 그리고 웹 브라우저 안에서 실시간으로 사물을 인식해보는 인공지능 실습을 진행합니다.",
    "tags": [
        { "label": "YOLO", "color": "purple" },
        { "label": "객체 인식", "color": "orange" },
        { "label": "AI실습", "color": "green" }
    ],
    "gradient": "linear-gradient(90deg, #7B00FF, #00FF88)"
}

for subject in data.get('subjects', []):
    if subject.get('name') == '인공지능과피지컬컴퓨팅':
        # 중복 방지
        exists = any(p.get('path') == new_page['path'] for p in subject['pages'])
        if not exists:
            subject['pages'].append(new_page)
        break

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("pages.json updated")
