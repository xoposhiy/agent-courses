"""Inspect the public CMU course page bundle without executing its code."""

import re
import requests

response = requests.get('https://www.cmu-agents.com/assets/index-B2wnGLzC.js', timeout=30)
response.raise_for_status()
text = response.text
print('Bundle bytes:', len(response.content))
print('\n'.join(sorted(set(re.findall(r'https?://[^\s"<>]+', text))))[:18000])
print(text[-22000:])
