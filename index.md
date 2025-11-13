---
title: Home
layout: home
slide_id: 0
---

{% if site.data.conference.proceedings_path %}
The proceedings of the symposium are now available.
<a href="{{site.data.conference.proceedings_path}}" target="_blank" rel="noopener noreferrer">
    <span class="badge badge-primary mx-1">
        <i class="fa fa-download mr-1"></i>
        PDF
    </span>
</a>
{% endif %}

Read about the history of ISCLS [here](/history.html).

{% if site.data.conference.show_about_logo %}
Read about the logo of ISCLS [here](/logo.html).
{% endif %}