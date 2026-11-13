async (page) => {
  const sources = [
    'https://smith.langchain.com/public/5e17b93a-17af-4386-ada0-9bd033f98a74/r',
    'https://smith.langchain.com/public/aeddf201-687b-4389-acdb-137dd9683000/r',
    'https://smith.langchain.com/public/416d3c74-4b43-4883-b189-92a57431a819/r',
  ];
  const results = [];
  for (const url of sources) {
    const share = url.split('/public/')[1].split('/')[0];
    const pending = page.waitForResponse(response =>
      response.url().includes('/v2/public/' + share + '/runs/query') &&
      response.request().method() === 'POST', { timeout: 20000 }).catch(() => null);
    await page.goto(url);
    const response = await pending;
    const result = await page.evaluate(() => ({
      url: location.href,
      html: document.documentElement.outerHTML,
      text: document.body.innerText,
    }));
    if (response) {
      result.query_url = response.url();
      result.http_status = response.status();
      result.query_body = response.request().postData();
      result.response_body = await response.text();
    }
    results.push(result);
  }
  return results;
}
