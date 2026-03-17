import codecs

html_content = codecs.open('c:/Users/chani/presentation/인공지능과피지컬컴퓨팅/YOLO/index.html', 'r', 'utf-8').read()

slides = """
        <!-- Slide 1: Cover -->
        <div class="slide active" id="slide1">
            <div class="center-slide" style="height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <div class="badge">인공지능과 피지컬컴퓨팅</div>
                <h1 class="text-gradient" style="font-size: 5rem; margin-bottom: 0.5rem;">YOLO</h1>
                <h2 style="border: none; color: var(--text-body); font-family: 'Noto Sans KR'; font-size: 1.8rem; font-weight: 300;">You Only Look Once:<br>한 번만 보고 다 아는 객체 인식의 마법</h2>
            </div>
        </div>

        <!-- Slide 2: 목차 (TOC) -->
        <div class="slide" id="slide2">
            <div class="browser-card">
                <div class="browser-content">
                    <h2>오늘의 <span class="text-gradient">학습 여정</span></h2>
                    <ul class="toc-list" style="list-style: none; max-width: 800px; margin: 2rem auto;">
                        <li class="toc-item" onclick="goToSlide(2)">
                            <div class="toc-num">1</div>
                            <div>
                                <h3 style="margin-bottom:0.2rem; font-family:'Noto Sans KR';">이전 시간 복습 (CNN)</h3>
                                <div style="font-size: 0.9rem; color: var(--text-body); opacity: 0.8;">이미지를 어떻게 분류할까?</div>
                            </div>
                        </li>
                        <li class="toc-item" onclick="goToSlide(3)">
                            <div class="toc-num">2</div>
                            <div>
                                <h3 style="margin-bottom:0.2rem; font-family:'Noto Sans KR';">YOLO의 등장!</h3>
                                <div style="font-size: 0.9rem; color: var(--text-body); opacity: 0.8;">분류를 넘어 위치까지 찾아내는 AI 모델</div>
                            </div>
                        </li>
                        <li class="toc-item" onclick="goToSlide(5)">
                            <div class="toc-num">3</div>
                            <div>
                                <h3 style="margin-bottom:0.2rem; font-family:'Noto Sans KR';">사각형 상자의 비밀</h3>
                                <div style="font-size: 0.9rem; color: var(--text-body); opacity: 0.8;">Bounding Box는 어떻게 만들어지는가?</div>
                            </div>
                        </li>
                        <li class="toc-item" onclick="goToSlide(7)">
                            <div class="toc-num">4</div>
                            <div>
                                <h3 style="margin-bottom:0.2rem; font-family:'Noto Sans KR';">실전! YOLO 실습</h3>
                                <div style="font-size: 0.9rem; color: var(--text-body); opacity: 0.8;">웹 브라우저에서 실시간 객체 탐지 구동하기</div>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Slide 3: CNN 복습 (Two-column) -->
        <div class="slide" id="slide3">
            <div class="browser-card">
                <div class="browser-content">
                    <h2><span style="color:var(--glow-3);">1.</span> 이전 시간에 배운 CNN 복습</h2>
                    <div class="grid-2">
                        <div>
                            <div class="highlight-box">
                                <h3 style="margin-top:0;">CNN (합성곱 신경망)</h3>
                                <p>이미지의 특징을 스스로 학습하여, 사진 속에 있는 물체가 <strong>무엇인지(What) 지정된 클래스로 분류</strong>하는 기술입니다.</p>
                            </div>
                            <ul class="timeline-list">
                                <li><strong>특징 추출 (Feature Extraction):</strong> 필터(Filter)를 통과하여 이미지 데이터 뽑아냄</li>
                                <li><strong>차원 축소 (Pooling):</strong> 정보량을 줄여 요약하기</li>
                                <li><strong>결과 예측:</strong> "이 사진은 95% 확률로 강아지입니다!"</li>
                            </ul>
                        </div>
                        <div class="center-slide">
                            <div class="canvas-container" style="border-color: rgba(255,255,255,0.2); min-height: 250px; background: rgba(255,255,255,0.05); margin-top:0;">
                                <div style="font-size: 5rem; margin-bottom: 1rem;">🐶</div>
                                <div class="badge" style="border-color: var(--glow-2); color: #fff; background: var(--glow-2); margin-bottom: 0;">100% 강아지!</div>
                                <div style="margin-top: 1rem; color: #888; font-size: 0.9rem;">CNN은 이 사진이 '무엇'인지 아는 데 특화!</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 4: YOLO 개요 (section-overview) -->
        <div class="slide" id="slide4">
            <div class="browser-card">
                <div class="browser-content">
                    <h2><span style="color:var(--glow-3);">2.</span> YOLO란 무슨 뜻일까?</h2>
                    
                    <div style="text-align: center; margin: 3rem 0;">
                        <h1 class="text-gradient" style="font-size: 4rem;">You Only Look Once</h1>
                        <p style="font-size: 1.2rem; opacity: 0.9;">"너는 한 번만 본다" — <strong>단 한 번의 신경망 계산으로</strong> 전체 이미지를 파악함</p>
                    </div>

                    <div class="card-grid">
                        <div class="info-card">
                            <span class="emoji">⚡</span>
                            <h3>엄청 빠른 속도</h3>
                            <p>기존 방식은 물체가 있을 법한 곳을 수천 번 탐색했지만, YOLO는 이미지를 한 번에 쓱 훑어보고 계산을 끝냅니다.</p>
                        </div>
                        <div class="info-card">
                            <span class="emoji">🎯</span>
                            <h3>위치와 종류 동시 파악</h3>
                            <p>이미지가 <strong>무엇(Classification)</strong>인지와 <strong>어디(Localization)</strong>에 있는지를 동시에 예측합니다.</p>
                        </div>
                        <div class="info-card">
                            <span class="emoji">🚗</span>
                            <h3>실시간 활용</h3>
                            <p>동영상이나 자율주행 자동차, CCTV 시스템에서도 끊기지 않고 부드럽게 돌아갈 만큼 빠릅니다.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 5: YOLO 기반 CNN (Card Grid) -->
        <div class="slide" id="slide5">
            <div class="browser-card">
                <div class="browser-content">
                    <h2><span style="color:var(--glow-3);">3.</span> YOLO에서 CNN은 어떻게 쓰일까?</h2>
                    <p style="margin-bottom: 2rem;">YOLO의 뼈대(Backbone)는 <strong>우리가 지난 시간에 배운 CNN</strong>으로 이루어져 있습니다!</p>

                    <div class="grid-2" style="align-items: start;">
                        <div class="highlight-box" style="border-color: var(--glow-2); background: rgba(123,0,255,0.1)">
                            <h3 style="color: var(--glow-2); margin-top:0;">CNN (입력 → 특징 추출)</h3>
                            <p>카메라에서 들어온 거대한 이미지 데이터를 여러 번의 합성곱과 풀링을 거쳐 작은 크기의 특징 지도(Feature Map)로 압축합니다.</p>
                            <div style="font-size:3rem; text-align:center; padding:1rem 0;">🖼️ ➡️ 🧩</div>
                        </div>
                        <div class="highlight-box">
                            <h3 style="margin-top:0;">YOLO Layer (출력 → 위치 찾기)</h3>
                            <p>CNN이 찾아낸 퍼즐 조각(특징)들을 바탕으로, 이미지를 격자(Grid)로 나누고 사물이 있는 <strong style="color: var(--glow-1)">중심점과 상자 크기</strong>를 추리합니다.</p>
                            <div style="font-size:3rem; text-align:center; padding:1rem 0;">🧩 ➡️ 📦</div>
                        </div>
                    </div>
                    
                    <div style="text-align: center; margin-top: 1rem;">
                        <span class="badge" style="font-size: 1rem;">결론: CNN 기술이 없었으면 YOLO도 탄생할 수 없었습니다!</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 6: 바운딩 박스 만들어지는 원리 (image-focus) -->
        <div class="slide" id="slide6">
            <div class="browser-card">
                <div class="browser-content">
                    <h2><span style="color:var(--glow-3);">4.</span> 사각형 상자(Bounding Box)는 어떻게 그려질까?</h2>
                    
                    <div class="grid-2">
                        <div class="center-slide">
                            <div class="canvas-container" style="min-height: 250px; position:relative; margin-top:0;">
                                <!-- Mockup visualization -->
                                <div style="display:grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: repeat(3, 1fr); width:100%; height:100%; position:absolute; inset:0; border: 1px dashed rgba(255,255,255,0.2);">
                                    <div style="border: 1px dashed rgba(255,255,255,0.2);"></div>
                                    <div style="border: 1px dashed rgba(255,255,255,0.2);"></div>
                                    <div style="border: 1px dashed rgba(255,255,255,0.2);"></div>
                                    <div style="border: 1px dashed rgba(255,255,255,0.2);"></div>
                                    <div style="border: 1px dashed rgba(255,255,255,0.2); background: rgba(123,0,255,0.3); display:flex; align-items:center; justify-content:center;">
                                        <span style="font-size: 2rem;">🐈</span>
                                    </div>
                                    <div style="border: 1px dashed rgba(255,255,255,0.2);"></div>
                                    <div style="border: 1px dashed rgba(255,255,255,0.2);"></div>
                                    <div style="border: 1px dashed rgba(255,255,255,0.2);"></div>
                                    <div style="border: 1px dashed rgba(255,255,255,0.2);"></div>
                                </div>
                                <div style="position:absolute; width: 60%; height: 70%; border: 3px solid var(--glow-1); box-shadow: 0 0 10px var(--glow-1); left: 20%; top: 15%; display:flex; flex-direction:column; justify-content:space-between; z-index: 10;">
                                    <span style="background:var(--glow-1); color:#000; font-family:'Space Mono'; font-size:0.8rem; font-weight:bold; padding:2px 5px; align-self:flex-start;">고양이 0.98</span>
                                    <div style="position:absolute; top: 50%; left: 50%; width:8px; height:8px; background:var(--glow-3); border-radius:50%; transform:translate(-50%, -50%); box-shadow: 0 0 10px var(--glow-3);"></div>
                                </div>
                            </div>
                        </div>
                        <div>
                            <ul class="timeline-list">
                                <li><strong>1. 이미지 분할 (Grid 시스템)</strong><br>전체를 바둑판(Grid) 형태로 나눕니다.</li>
                                <li><strong>2. 중심점 확인</strong><br>물체의 중심이 어느 특정 격자(Grid cell) 안에 존재하는지 찾고, 그 격자가 예측을 책임집니다.</li>
                                <li><strong>3. 기준 상자 (Anchor Box)</strong><br>대략적인 크기(예: 길쭉한 사람, 납작한 자동차)를 기준으로 상자를 늘립니다.</li>
                                <li><strong>4. 신뢰도 판별 (Confidence Score)</strong><br>"이 안에 물체가 확실히 있는가?", "그 물체가 고양이일 확률"을 더해 최종 라벨을 박스 위에 띄웁니다!</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 7: 실습 도구 소개 (활동 리스트) -->
        <div class="slide" id="slide7">
            <div class="browser-card">
                <div class="browser-content">
                    <h2><span style="color:var(--glow-3);">5.</span> 오늘 우리가 사용할 마법 도구 (ml5.js)</h2>
                    
                    <div class="highlight-box" style="text-align:center;">
                        <h3 style="margin-top:0;">ml5.js 란? 🤔</h3>
                        <p style="font-size:1.1rem;">"누구나 웹 브라우저에서 인공지능을 쉽게 접근할 수 있게 하자!"</p>
                    </div>

                    <div class="card-grid" style="margin-top: 2rem;">
                        <div class="info-card" style="border-color: var(--glow-1);">
                            <span class="emoji">🌐</span>
                            <h3 style="color:var(--white);">설치가 필요 없어요</h3>
                            <p>파이썬이나 무거운 라이브러리를 설치할 필요 없이 웹 브라우저 하나만 있으면 준비 끝!</p>
                        </div>
                        <div class="info-card" style="border-color: var(--glow-3);">
                            <span class="emoji">🧠</span>
                            <h3 style="color:var(--white);">미리 학습된 모델 (Pre-trained)</h3>
                            <p>수백만 장의 사진을 훈련한 <strong>COCO-SSD 모델</strong>을 사용합니다. 80종류의 흔한 사물을 찾을 수 있어요.</p>
                        </div>
                        <div class="info-card" style="border-color: var(--glow-2);">
                            <span class="emoji">🎨</span>
                            <h3 style="color:var(--white);">자바스크립트 활용</h3>
                            <p>AI가 찾아낸 특징과 위치 정보를 이용해, 이미지 위에 직접 네온 박스(Bounding Box)를 그려보는 실습입니다.</p>
                        </div>
                    </div>
                    
                    <div style="text-align:center; margin-top: 3rem;">
                        <p style="font-size: 1.2rem; font-weight: bold; color: var(--glow-3);">다음 슬라이드에서 직접 경험해 봅시다!</p>
                        <p style="font-size: 0.9rem;">(다음 페이지를 넘기면 인공지능 모델 다운로드 시간이 1~3초 가량 필요합니다)</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 8: Interactive Demo (JavaScript 기반) -->
        <div class="slide" id="slide8">
            <div class="browser-card">
                <div class="browser-content">
                    <h2><span style="color:var(--glow-3);">실습:</span> 인공지능으로 사진 속 사물 찾기</h2>
                    
                    <div class="demo-layout">
                        <div class="control-panel">
                            <div>
                                <label for="imageUpload" class="btn-neon">새 사진 올리기 📸</label>
                                <input type="file" id="imageUpload" accept="image/*">
                            </div>
                            <div class="status-text" id="aiStatus">🤖 다음 장에서 모델이 연동됩니다...</div>
                        </div>
                        
                        <div class="canvas-container">
                            <canvas id="demoCanvas"></canvas>
                            <!-- Use a placeholder image initially -->
                            <img id="demoImage" src="https://images.unsplash.com/photo-1543852786-1cf6624b9987?auto=format&fit=crop&w=800&q=80" crossorigin="anonymous">
                            
                            <div id="loadingOverlay" style="position:absolute; inset:0; background:rgba(0,0,0,0.8); display:flex; align-items:center; justify-content:center; flex-direction:column; z-index:100; display:none;">
                                <div style="width: 40px; height: 40px; border: 4px solid rgba(0,255,136,0.2); border-top: 4px solid var(--glow-1); border-radius: 50%; animation: spin 1s linear infinite; margin-bottom: 1rem;"></div>
                                <span style="color:var(--glow-1); font-family:'Space Mono';" id="loadingText">AI 모델 로딩 중...</span>
                            </div>
                        </div>
                        <p style="font-size:0.9rem; color:var(--text-body); max-width: 800px; text-align:center;">
                            * COCO-SSD 모델은 80가지 종류의 일반적인 사물(cat, dog, car, person 등)을 구분할 수 있습니다.<br>위에 있는 버튼을 눌러 본인의 사진이나 저장된 이미지로 테스트해 보세요!
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Slide 9: 마무리 -->
        <div class="slide" id="slide9">
            <div class="center-slide">
                <div style="margin-bottom: 2rem;">
                    <span style="font-size: 5rem;">🚀</span>
                </div>
                <h1 class="text-gradient">수고하셨습니다!</h1>
                <div class="highlight-box" style="text-align:left; display:inline-block; max-width:800px; margin-top:2rem;">
                    <h3 style="color: var(--glow-1); margin-top:0;">오늘의 핵심 3가지</h3>
                    <ul class="timeline-list">
                        <li><strong>YOLO의 뜻:</strong> 분류와 위치 찾기를 단 한 번의 과정으로 끝내는 똑똑한 AI 모델</li>
                        <li><strong>CNN 뼈대(Backbone):</strong> 이미지 데이터에서 거시적 특징을 뽑아내는 핵심 도구</li>
                        <li><strong>가상의 바둑판 표(Grid):</strong> 각 셀(Cell)마다 자신에게 속한 물체의 Bounding Box를 계산하기 위해 협동</li>
                    </ul>
                </div>
                <div style="margin-top: 3rem; font-family:'Space Mono'; color:var(--text-body); font-size: 0.9rem;">
                    [인공지능과 피지컬컴퓨팅] 수업 자료 END.
                </div>
            </div>
        </div>
        <style>@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }</style>
"""

new_html = html_content.replace('<!-- Slides will go here -->', slides)

js_to_add = """
        // ml5.js Object Detection Logic
        let objectDetector;
        let imgElem = document.getElementById('demoImage');
        let canvasElem = document.getElementById('demoCanvas');
        let ctx = canvasElem ? canvasElem.getContext('2d', { willReadFrequently: true }) : null;
        let aiStatus = document.getElementById('aiStatus');
        let loadingOverlay = document.getElementById('loadingOverlay');
        let isModelLoaded = false;
        let modelInitialized = false;

        function checkDemoSlide() {
            if(slides && slides[currentSlide] && slides[currentSlide].id === 'slide8' && !modelInitialized) {
                modelInitialized = true;
                if(loadingOverlay) loadingOverlay.style.display = 'flex';
                initModel();
            }
        }

        // Hack into updateSlides to trigger checkDemoSlide
        const oldUpdateSlides = updateSlides;
        updateSlides = function() {
            oldUpdateSlides();
            checkDemoSlide();
        };

        function initModel() {
            if(aiStatus) aiStatus.textContent = "🤖 모델 다운로드 중... (10MB)";
            if (window.ml5 && ml5.objectDetector) {
                objectDetector = ml5.objectDetector('cocossd', modelLoaded);
            } else {
                if(aiStatus) aiStatus.textContent = "❌ 인터넷 속도가 느려 ml5.js 로드 실패";
                if(loadingOverlay) loadingOverlay.style.display = 'none';
            }
        }

        function modelLoaded() {
            isModelLoaded = true;
            if(aiStatus) aiStatus.textContent = "✨ AI 모델 준비 완료!";
            if(loadingOverlay) loadingOverlay.style.display = 'none';
            detectObjects();
        }

        function resizeCanvas() {
            if(!canvasElem || !imgElem) return;
            // Get original natural dimensions
            let nw = imgElem.naturalWidth;
            let nh = imgElem.naturalHeight;
            if(nw === 0 || nh === 0) return;
            
            // Set canvas size back to 0 temporarily to get image displayed size
            canvasElem.style.width = '100%';
            canvasElem.style.height = 'auto';
            let ratio = nw / nh;
            
            let containerWidth = canvasElem.parentElement ? canvasElem.parentElement.clientWidth : nw;
            let displayHeight = Math.min(containerWidth / ratio, 400); 
            
            // Set actual canvas bounds to natural for high resolution drawing
            canvasElem.width = nw;
            canvasElem.height = nh;
            ctx.drawImage(imgElem, 0, 0, canvasElem.width, canvasElem.height);
            
            // Set inline display size
            canvasElem.style.maxHeight = '50vh';
        }

        function detectObjects() {
            if (!isModelLoaded) return;
            if(aiStatus) aiStatus.textContent = "🔍 화면 내 사물 탐색 중...";
            if(loadingOverlay) { loadingOverlay.style.display = 'flex'; document.getElementById('loadingText').textContent = '분석 중...'; }
            
            // Make sure the image is drawn first
            resizeCanvas();
            
            if(objectDetector) {
                objectDetector.detect(canvasElem, (err, results) => {
                    if(loadingOverlay) loadingOverlay.style.display = 'none';
                    if (err) { console.error(err); return; }
                    
                    drawResults(results);
                    if(aiStatus) aiStatus.innerHTML = `✅ 분석 완료 (찾아낸 사물: <strong style="color:var(--glow-1); font-size:1.2em;">${results.length}</strong>개)`;
                });
            }
        }

        function drawResults(results) {
            ctx.drawImage(imgElem, 0, 0, canvasElem.width, canvasElem.height);
            for (let i = 0; i < results.length; i++) {
                let object = results[i];
                // Draw bound box
                ctx.strokeStyle = '#00FF88'; // Neon Green
                ctx.lineWidth = Math.max(3, canvasElem.width * 0.005);
                ctx.strokeRect(object.x, object.y, object.width, object.height);
                
                // Draw text bg
                ctx.fillStyle = '#1A1A2E'; // panel bg
                let text = object.label + " " + Math.round(object.confidence * 100) + "%";
                ctx.font = `bold ${Math.max(20, canvasElem.width * 0.03)}px "Space Mono", Noto Sans KR`;
                let textWidth = ctx.measureText(text).width;
                let textHeight = Math.max(30, canvasElem.width * 0.04);
                
                ctx.fillRect(object.x, object.y - textHeight, textWidth + parseInt(textHeight*0.4), textHeight);
                
                // Draw label text
                ctx.fillStyle = '#00FF88';
                ctx.fillText(text, object.x + parseInt(textHeight*0.2), object.y - parseInt(textHeight*0.2));
            }
        }

        // Image upload handling
        let uploadBtn = document.getElementById('imageUpload');
        if(uploadBtn) {
            uploadBtn.addEventListener('change', function(e) {
                let file = e.target.files[0];
                if(!file) return;
                let reader = new FileReader();
                reader.onload = function(event) {
                    imgElem.crossOrigin = "anonymous";
                    imgElem.onload = function() {
                        if(isModelLoaded) setTimeout(detectObjects, 50);
                    }
                    imgElem.src = event.target.result;
                };
                reader.readAsDataURL(file);
            });
        }
        
        // Connect neon button to real file input
        let neonLabels = document.querySelectorAll('label[for="imageUpload"]');
        neonLabels.forEach(p => p.addEventListener('click', (e) => {
             // Since it's a label, clicking it automatically triggers the input, but we can prevent double triggers.
             // Just let label feature handle it
        }));
        
        // Let's make sure initial image works
        if(imgElem) {
            imgElem.onload = () => { if(isModelLoaded) setTimeout(detectObjects, 50); };
        }
"""

new_html = new_html.replace('window.onload = () => { initNav(); };', 'window.onload = () => { initNav(); };\n' + js_to_add)

with codecs.open('c:/Users/chani/presentation/인공지능과피지컬컴퓨팅/YOLO/index.html', 'w', 'utf-8') as f:
    f.write(new_html)
print("done")
