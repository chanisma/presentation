
    // Navigation Logic
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;
    let currentSlide = 0;
    const progress = document.getElementById('progressBar');
    const input = document.getElementById('slideInput');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    document.getElementById('totalSlides').textContent = totalSlides;

    function updateNav() {
      slides.forEach((s, i) => {
        if (i === currentSlide) {
          s.classList.add('active');
        } else {
          s.classList.remove('active');
        }
      });
      progress.style.width = ((currentSlide + 1) / totalSlides * 100) + '%';
      input.value = currentSlide + 1;
      prevBtn.disabled = currentSlide === 0;
      nextBtn.disabled = currentSlide === totalSlides - 1;
    }

    function nextSlide() {
      if (currentSlide < totalSlides - 1) {
        currentSlide++;
        updateNav();
      }
    }

    function prevSlide() {
      if (currentSlide > 0) {
        currentSlide--;
        updateNav();
      }
    }

    function goToSlide(n) {
      if (n >= 0 && n < totalSlides) {
        currentSlide = n;
        updateNav();
      }
    }

    // Keyboard navigation (skip if inside textarea or input)
    document.addEventListener('keydown', (e) => {
      // Input 필드에서 처리 방지
      if (e.target.tagName.toLowerCase() === 'textarea' || e.target.tagName.toLowerCase() === 'input') {
        return; 
      }
      
      if (['ArrowRight', 'ArrowDown', ' ', 'PageDown'].includes(e.key)) {
        e.preventDefault();
        nextSlide();
      } else if (['ArrowLeft', 'ArrowUp', 'PageUp'].includes(e.key)) {
        e.preventDefault();
        prevSlide();
      } else if (e.key === 'Home') {
        e.preventDefault();
        goToSlide(0);
      } else if (e.key === 'End') {
        e.preventDefault();
        goToSlide(totalSlides - 1);
      }
    });
    
    // Prevent propagating keystrokes from code editors to document
    document.querySelectorAll('.code-editor').forEach(editor => {
      editor.addEventListener('keydown', e => {
        e.stopPropagation();
      });
    });

    // Input jump logic
    input.addEventListener('keydown', (e) => {
      e.stopPropagation();
      if (e.key === 'Enter') {
        let val = parseInt(input.value) - 1;
        if (!isNaN(val)) goToSlide(Math.max(0, Math.min(val, totalSlides - 1)));
      } else if (e.key === 'Escape') {
        input.value = currentSlide + 1;
        input.blur();
      }
    });

    // Mouse wheel navigation
    let wheelLocked = false;
    document.addEventListener('wheel', (e) => {
      // 코드 에디터 내부 스크롤 시에는 슬라이드 넘김 방지
      if (e.target.closest('.code-editor') || e.target.closest('.preview-pane')) return;

      e.preventDefault();
      if (wheelLocked) return;
      wheelLocked = true;
      if (e.deltaY > 0) nextSlide();
      else if (e.deltaY < 0) prevSlide();
      setTimeout(() => { wheelLocked = false; }, 600);
    }, { passive: false });

    // Live Code Editor Logic
    function updatePreview(id) {
      const htmlEditor = document.getElementById(`html-${id}`);
      const cssEditor = document.getElementById(`css-${id}`);
      const iframe = document.getElementById(`preview-${id}`);
      
      if(!htmlEditor || !cssEditor || !iframe) return;

      const htmlCode = htmlEditor.value;
      const cssCode = cssEditor.value;
      
      const content = `
        <!DOCTYPE html>
        <html>
        <head>
          <style>
             body { font-family: 'Noto Sans KR', sans-serif; padding: 15px; margin: 0; box-sizing: border-box; }
             ${cssCode}
          </style>
        </head>
        <body>
          ${htmlCode}
        </body>
        </html>
      `;
      
      // Use srcdoc which is robust and doesn't throw null reference errors
      iframe.srcdoc = content;
    }

    // Add event listeners and init
    document.querySelectorAll('.html-editor, .css-editor').forEach(editor => {
      editor.addEventListener('input', (e) => {
        const id = e.target.getAttribute('data-id');
        updatePreview(id);
      });
    });

    // Initial render
    [1, 2, 3, 4].forEach(id => updatePreview(id));
    updateNav();
  