async (page) => {
  const pages = [];
  for (const route of ['home', 'schedule', 'assignments', 'project', 'syllabus', 'staff', 'sponsorship']) {
    const url = 'https://www.cmu-agents.com/' + (route === 'home' ? '#/' : '#/' + route);
    await page.goto(url);
    await page.locator('#content').waitFor();
    const result = await page.evaluate(() => ({
      html: document.documentElement.outerHTML,
      text: document.querySelector('#content').textContent,
      links: Array.from(document.querySelectorAll('#content a[href]')).map(a => ({ title: a.textContent.trim(), url: a.href })),
      schedule: Array.from(document.querySelectorAll('.schedule-item')).map(item => ({
        title: item.querySelector('h3')?.textContent,
        date: item.firstElementChild?.textContent,
        text: item.textContent,
        links: Array.from(item.querySelectorAll('a[href]')).map(a => ({
          title: a.textContent.trim(), url: a.href,
          category: a.closest('details') ? 'references' : (a.closest('p')?.querySelector('strong')?.textContent || 'lecturer')
        }))
      }))
    }));
    pages.push({ route, url, ...result });
  }
  return pages;
}
