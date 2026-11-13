async (page) => {
  return await page.evaluate(() => ({
    url: location.href,
    title: document.title,
    html: document.documentElement.outerHTML,
    text: document.body.innerText,
  }));
}
