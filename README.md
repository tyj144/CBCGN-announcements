# Google Groups for Django
A quick way to show posts from a Google Group on a webpage using feedparser and Django.

*This requires Django and is therefore not available on my actual page.*

![Demo](https://github.com/tyj144/cbcgn-announcements/blob/master/demo.png)

## Files
#### views.py
Sends an array of the 10 most recent posts in the Google Group to the template, which will then be rendered.

#### google_group_posts.html
A Jinja template which extends off of an original "header.html" file. It takes the title, author name, info, and link for each post and displays it on the page.
