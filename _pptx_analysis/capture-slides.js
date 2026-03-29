const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('file:///E:/presentation/정보/이미지생성의기초개념/index.html', { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);

  const totalSlides = await page.evaluate(() => document.querySelectorAll('.slide').length);
  console.log('Total slides: ' + totalSlides);

  for (let i = 0; i < totalSlides; i++) {
    await page.evaluate((idx) => {
      if (typeof goToSlide === 'function') goToSlide(idx);
    }, i);
    await page.waitForTimeout(600);
    await page.screenshot({ path: `_pptx_analysis/slide-preview-${String(i+1).padStart(2,'0')}.png` });
    console.log('Captured slide ' + (i+1));
  }

  await browser.close();
  console.log('Done!');
})();
