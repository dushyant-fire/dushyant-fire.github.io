---
layout:	default
title:	Blog
permalink:	/blog/
---

## Articles

<ul>
      {% for post in site.categories.blog %}
        <li>
          <a href="{{ post.permalink }}">{{ post.title }}</a>
          <!-- <p>{{ post.categories }}</p> -->
          <p>{{ post.excerpt }}</p>
        </li>
      {% endfor %}
</ul>
