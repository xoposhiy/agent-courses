# Project code: stanford-oval/Churro: docs/_templates/sidebar-nav-full.html

[Course index](../../../../../README.md) · [Original source](https://github.com/stanford-oval/Churro/blob/HEAD/docs/_templates/sidebar-nav-full.html) · [Raw file](../../../../../raw/repositories/stanford-oval-churro/docs/_templates/sidebar-nav-full.html)

Retrieved: 2026-11-13T17:04:51.902331+00:00

{# Render the full site toctree in the primary sidebar on every page. #}
{% set show\_nav\_level = meta['html\_theme.show\_nav\_level'] if (meta is defined and meta is not none and 'html\_theme.show\_nav\_level' in meta) else theme\_show\_nav\_level %}
