import codecs

html_content = codecs.open('c:/Users/chani/presentation/인공지능과피지컬컴퓨팅/YOLO/index.html', 'r', 'utf-8').read()

import re
# 1. CSS 및 배경 스타일 교체
new_css = """
        /* 1. Reset & CSS Variables (기본 Green 테마) */
        :root {
            --main: #3aaa5c;
            --dark: #2d8a49;
            --light: #e8f5e9;
            --accent: #43b867;
            --white: #ffffff;
            --black: #333333;
            --gray-100: #f5f5f5;
            --gray-200: #eeeeee;
            --gray-500: #9e9e9e;
            --gray-600: #757575;
            --gray-700: #616161;
            font-size: clamp(16px, 1.5vw, 28px);
        }

        * { box-sizing: border-box; }
        
        body {
            margin: 0; padding: 0;
            background-color: var(--gray-100);
            color: var(--black);
            font-family: 'Noto Sans KR', sans-serif;
            overflow: hidden; 
            line-height: 1.6;
        }

        /* Typography */
        h1, h2, h3 { font-family: 'Noto Sans KR', sans-serif; font-weight: 700; color: var(--black); margin-top: 0; word-break: keep-all; }
        h1 { font-size: 2.4rem; margin-bottom: 1rem; line-height: 1.3;}
        h2 { font-size: 1.5rem; margin-bottom: 1.5rem; }
        h3 { font-size: 1.15rem; margin-bottom: 1rem; }
        p { font-size: 1rem; line-height: 1.7; margin-top: 0; word-break: keep-all;}
        .font-mono { font-family: 'Space Mono', monospace; }

        .text-gradient {
            background: linear-gradient(90deg, var(--main), var(--dark));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            color: var(--main);
            display: inline-block;
        }

        /* 3. Slide Layouts */
        .presentation { width: 100vw; height: 100vh; position: relative; }
        .slide {
            position: absolute; top: 0; left: 0; right: 0; bottom: 0;
            padding: 5vh 5vw 8vh 5vw; /* 하단 네비게이션 공간 확보 */
            display: none;
            opacity: 0;
            transition: opacity 0.4s ease;
        }
        .slide.active { display: block; opacity: 1; }

        .browser-card {
            background: var(--white);
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            display: flex; flex-direction: column;
            width: 100%; height: 100%;
            overflow: hidden;
            position: relative;
        }
        
        .browser-topbar {
            height: 2.5rem; background: var(--gray-100); border-bottom: 1px solid var(--gray-200);
            display: flex; align-items: center; padding: 0 1rem; gap: 0.5rem;
        }
        .browser-topbar::before {
            content: ''; display: inline-block; width: 12px; height: 12px; border-radius: 50%;
            background: #ff5f56; box-shadow: 20px 0 0 #ffbd2e, 40px 0 0 #27c93f;
        }

        .browser-content { padding: 3rem; flex: 1; overflow-y: auto; }

        /* 4. Navigation Bar */
        .progress-bar { position: fixed; top: 0; left: 0; height: 4px; background: linear-gradient(90deg, var(--main), var(--accent)); z-index: 1000; width: 0%; transition: width 0.3s linear; }
        .nav-bar {
            position: fixed; bottom: 0; left: 0; right: 0;
            display: flex; align-items: center; justify-content: center;
            gap: 1rem; padding: 0.35rem 1.5rem;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-top: 1px solid var(--gray-200);
            z-index: 999;
        }
        .nav-btn {
            display: flex; align-items: center; justify-content: center;
            width: 1.8rem; height: 1.8rem; border-radius: 50%;
            background: transparent; border: 1.5px solid var(--gray-200); color: var(--gray-700);
            cursor: pointer; transition: 0.2s; padding: 0;
        }
        .nav-btn:hover:not(:disabled) { background: var(--main); border-color: var(--main); color: var(--white); }
        .nav-btn:disabled { opacity: 0.35; cursor: not-allowed; }
        .nav-btn svg { width: 0.8rem; height: 0.8rem; fill: currentColor; }
        .nav-counter { font-size: 14px; color: var(--gray-600); font-family: 'Space Mono'; display: flex; align-items: center; font-weight: bold;}
        .slide-input { background: none; border: none; border-bottom: 1px solid transparent; color: inherit; font-family: inherit; font-weight: bold; width: 1.5rem; text-align: center; font-size: 14px; outline: none; }
        .slide-input:focus { border-bottom-color: var(--main); background: var(--light); border-radius: 4px;}

        /* 5. Utility Components */
        .center-slide { display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; height: 100%; }
        .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: center; height: 100%; }
        
        .badge {
            display: inline-block; padding: 0.4em 1em; border-radius: 20px; font-size: 0.82rem; font-weight: bold;
            background: var(--light); color: var(--dark);
            border: 1px solid var(--main); margin-bottom: 1rem;
        }

        .highlight-box {
            background: var(--gray-100); border-left: 4px solid var(--main);
            padding: 1.5rem; border-radius: 0 8px 8px 0; margin-bottom: 1.5rem;
        }

        .card-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
        .info-card {
            background: var(--white); padding: 1.5rem; border-radius: 12px;
            border: 1px solid var(--gray-200); box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: transform 0.2s;
        }
        .info-card:hover { transform: translateY(-5px); box-shadow: 0 8px 15px rgba(0,0,0,0.1); border-color: var(--main);}
        .info-card .emoji { font-size: 2.5rem; margin-bottom: 0.5rem; display: block; }

        /* Mockup for image */
        .image-mockup { width: 100%; height: 100%; border-radius: 12px; object-fit: cover; border: 1px solid var(--gray-200); }

        /* ml5.js Demo Section */
        .demo-layout { display: flex; flex-direction: column; align-items: center; justify-content: flex-start; height: 100%; width: 100%;}
        .canvas-container { 
            position: relative; margin: 1.5rem 0; width: 100%; max-width: 800px; 
            border: 2px solid var(--gray-200); border-radius: 12px; overflow: hidden; background: #000;
            display: flex; justify-content: center; align-items: center; min-height: 400px;
        }
        #demoImage { display: none; }
        #demoCanvas { max-width: 100%; display: block; object-fit: contain; }
        .control-panel { 
            display: flex; justify-content: space-between; align-items: center; width: 100%; max-width: 800px;
            background: var(--gray-100); padding: 1rem 1.5rem; border-radius: 12px; border: 1px solid var(--gray-200);
        }
        .btn-neon {
            background: var(--main); color: var(--white); border: none;
            padding: 0.6rem 1.2rem; border-radius: 8px; font-weight: bold; cursor: pointer; transition: 0.2s;
        }
        .btn-neon:hover { background: var(--dark); }
        .status-text { color: var(--gray-600); font-weight: bold; font-size: 0.9rem;}
        
        /* Timeline */
        .timeline-list { list-style: none; padding-left: 1.5rem; border-left: 2px solid var(--gray-200); margin: 1.5rem 0; }
        .timeline-list li { position: relative; padding-bottom: 1.5rem; padding-left: 1rem; }
        .timeline-list li::before { content: ''; position: absolute; left: -1.5rem - 6px; top: 0.3rem; width: 12px; height: 12px; border-radius: 50%; background: var(--main); border: 3px solid var(--white);}
        .timeline-list li:last-child { padding-bottom: 0; }

        /* Keyframes */
        @keyframes float { 0% { transform: translate(0, 0); } 100% { transform: translate(5%, 5%); } }
"""
html_content = re.sub(r'<style>.*?</style>', f'<style>\n{new_css}\n        @keyframes spin {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}\n    </style>', html_content, flags=re.DOTALL)

# Delete aurora div
html_content = re.sub(r'<div class="aurora-bg">.*?</div>', '', html_content, flags=re.DOTALL)

# Insert missing browser-topbar
html_content = re.sub(r'(<div class="browser-card">)', r'\1\n                <div class="browser-topbar"></div>', html_content)

# Dark mode text styling fixes
html_content = html_content.replace('color: var(--text-body)', 'color: var(--gray-600)')
html_content = html_content.replace('color: var(--text-title)', 'color: var(--black)')
html_content = html_content.replace('rgba(255,255,255,0.05)', 'var(--gray-100)')
html_content = html_content.replace('color: var(--glow-3)', 'color: var(--dark)')
html_content = html_content.replace('color: var(--glow-2)', 'color: var(--main)')
html_content = html_content.replace('color: var(--glow-1)', 'color: var(--main)')
html_content = html_content.replace('border-color: rgba(255,255,255,0.2)', 'border-color: var(--gray-200)')
html_content = html_content.replace('rgba(123,0,255,0.1)', 'var(--light)')
html_content = html_content.replace('rgba(123,0,255,0.3)', 'var(--main); color: var(--white)')
html_content = html_content.replace('rgba(0,0,0,0.8)', 'rgba(255,255,255,0.9)')
html_content = html_content.replace('border: 1px dashed rgba(255,255,255,0.2);', 'border: 1px dashed var(--gray-500);')
html_content = html_content.replace('color:var(--white)', 'color:var(--black)')
html_content = html_content.replace('class="info-card" style="border-color: var(--glow-1);"', 'class="info-card"')
html_content = html_content.replace('class="info-card" style="border-color: var(--glow-3);"', 'class="info-card"')
html_content = html_content.replace('class="info-card" style="border-color: var(--glow-2);"', 'class="info-card"')
html_content = html_content.replace('<h1 class="text-gradient" style="font-size: 5rem; margin-bottom: 0.5rem;">YOLO</h1>', '<h1 class="text-gradient" style="font-size: 5rem; margin-bottom: 0.5rem; margin-top:0;">YOLO</h1>')

# Add Slide 7 (Usage Case)
slide_usage = """
        <!-- Slide 7: YOLO 활용 사례 -->
        <div class="slide" id="slide7">
            <div class="browser-card">
                <div class="browser-topbar"></div>
                <div class="browser-content">
                    <h2><span style="color:var(--main);">5.</span> YOLO는 언제 어디에 쓰일까?</h2>
                    <p style="margin-bottom: 2rem;">"한 번만 봐도 아는" 엄청난 눈치와 스피드 덕분에 우리 주변 곳곳에서 활약하고 있습니다.</p>

                    <div class="grid-2">
                        <div>
                            <ul class="timeline-list">
                                <li>
                                    <strong style="color: var(--main); font-size: 1.1em;">자율주행 자동차 🚗</strong><br>
                                    도로 위의 앞차, 신호등, 보행자를 빛의 속도로 파악해서 피하거나 멈춰야 합니다.
                                </li>
                                <li>
                                    <strong style="color: var(--main); font-size: 1.1em;">무인 매장 (ex. 아마존 고) 🛒</strong><br>
                                    고객이 어떤 물건을 집어 들었는지 천장에 달린 수십 대의 카메라가 즉시 인식해서 지갑 없이 결제되도록 돕습니다.
                                </li>
                                <li>
                                    <strong style="color: var(--main); font-size: 1.1em;">스마트 CCTV & 방범 🚨</strong><br>
                                    도둑이나 위험한 무기(칼 등)를 들고 있는 사람을 화면 안에서 발견 즉시 경찰에 알려줍니다.
                                </li>
                                <li>
                                    <strong style="color: var(--main); font-size: 1.1em;">불량품 검사 과정 🏭</strong><br>
                                    초고속으로 움직이는 공장 컨베이어 벨트 위에서 불량 사과나 부서진 플라스틱을 골라내는 데 쓰입니다.
                                </li>
                            </ul>
                        </div>
                        <div style="display:grid; grid-template-rows: repeat(2, 1fr); gap:1rem; height:100%;">
                            <!-- 활용 사례 대표 이미지들 (안전한 unsplash 랜덤 소스 활용) -->
                            <div style="position:relative; width:100%; border-radius:12px; overflow:hidden;">
                                <img src="https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?auto=format&fit=crop&w=600&q=80" style="width:100%; height:100%; object-fit:cover;" alt="자율주행">
                                <span class="badge" style="position:absolute; bottom:10px; right:10px; background:rgba(0,0,0,0.6); color:#fff; border:none; margin:0;">🚙 차량 내부/자율주행 시점</span>
                            </div>
                            <div style="position:relative; width:100%; border-radius:12px; overflow:hidden;">
                                <img src="https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=600&q=80" style="width:100%; height:100%; object-fit:cover;" alt="무인매장 쇼핑">
                                <span class="badge" style="position:absolute; bottom:10px; right:10px; background:rgba(0,0,0,0.6); color:#fff; border:none; margin:0;">🛍️ 무인 매장에서의 객체 인식</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
"""

html_content = html_content.replace('<!-- Slide 7: 실습 도구 소개', slide_usage + '\n        <!-- Slide 8: 실습 도구 소개')
html_content = html_content.replace('id="slide7"', 'id="slide8"')
html_content = html_content.replace('id="slide8"', 'id="slide9"')
html_content = html_content.replace('id="slide9"', 'id="slide10"')
html_content = html_content.replace('<div class="slide active" id="slide10">', '<div class="slide" id="slide10">')
html_content = html_content.replace('id="slide7">', 'id="slide8">') # Rollback some id overlaps manually via regex below
html_content = html_content.replace('5.</span> 오늘 우리가 사용할 마법 도구', '6.</span> 오늘 우리가 사용할 마법 도구')
html_content = html_content.replace('실습:</span> 인공지능으로 사진 속 사물 찾기', '실습:</span> 인공지능으로 사진 속 사물 찾기')

# Fix slide 8 id since the previous replace broke it
html_content = re.sub(r'<!-- Slide 8: 실습 도구 소개 \(활동 리스트\) -->\s*<div class="slide" id="slide9">', r'<!-- Slide 8: 실습 도구 소개 (활동 리스트) -->\n        <div class="slide" id="slide8">', html_content)
html_content = re.sub(r'<!-- Slide 9: Interactive Demo \(JavaScript 기반\) -->\s*<div class="slide" id="slide10">', r'<!-- Slide 9: Interactive Demo (JavaScript 기반) -->\n        <div class="slide" id="slide9">', html_content)

html_content = html_content.replace("slides[currentSlide].id === 'slide8'", "slides[currentSlide].id === 'slide9'")

# js style fixes
html_content = html_content.replace("ctx.strokeStyle = '#00FF88'", "ctx.strokeStyle = '#3aaa5c'")
html_content = html_content.replace("ctx.fillStyle = '#1A1A2E'", "ctx.fillStyle = '#3aaa5c'")
html_content = html_content.replace("ctx.fillStyle = '#00FF88'", "ctx.fillStyle = '#ffffff'")

# Go to slide fix
html_content = html_content.replace('goToSlide(7)', 'goToSlide(8)')

with codecs.open('c:/Users/chani/presentation/인공지능과피지컬컴퓨팅/YOLO/index.html', 'w', 'utf-8') as f:
    f.write(html_content)

print("Slide content rewritten!")
