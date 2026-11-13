async (page) => {
  await page.locator('article').waitFor({ timeout: 15000 });
  return await page.evaluate(() => ({
    url: location.href,
    title: document.querySelector('h1').innerText,
    html: document.documentElement.outerHTML,
    text: document.querySelector('article').innerText,
    images: Array.from(document.querySelectorAll('article img')).map(image => ({
      src: image.currentSrc || image.src,
      alt: image.alt,
    })),
  }));
}
