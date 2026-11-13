# Project code: stanford-oval/Churro: docs/_templates/sections/sidebar-primary.html

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/Churro/blob/HEAD/docs/_templates/sections/sidebar-primary.html) · [Raw file](../../../../../../raw/repositories/stanford-oval-churro/docs/_templates/sections/sidebar-primary.html)

Retrieved: 2026-11-13T17:04:51.902331+00:00

{% block docs\_sidebar %}
{% if theme\_navbar\_center or theme\_navbar\_end or sidebars or theme\_primary\_sidebar\_end %}

{% if theme\_navbar\_center %}

{% for navbar\_item in theme\_navbar\_center %}
{% with theme\_header\_links\_before\_dropdown=999 %}

{% include navbar\_item %}

{% endwith %}
{% endfor %}

{% endif %}
{% if theme\_navbar\_end %}

{% for navbar\_item in theme\_navbar\_end %}

{% include navbar\_item %}

{% endfor %}

{% endif %}

{% include "sidebar-toggle.html" %}

{% if sidebars %}
{%- for sidebartemplate in sidebars %}

{%- include sidebartemplate %}

{%- endfor %}
{% endif %}

{%- for sidebartemplate in theme\_primary\_sidebar\_end %}

{%- include sidebartemplate %}

{%- endfor %}

{% endif %}
{% endblock docs\_sidebar %}
