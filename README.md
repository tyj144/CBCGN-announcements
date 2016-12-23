# cbcgn-announcements
A quick way to show posts from a Google Group on a webpage using feedparser and Django.

## Demonstration
![Demo](https://github.com/tyj144/cbcgn-announcements/blob/master/demo.png)

## Files
#### views.py
Sends an array of the 10 most recent posts in the Google Group to the template, which will then be rendered.

#### cbcgn_youth.html
A jinja template which extends off of an original "header.html" file. It takes the title, author name, info, and link for each post and displays it on the page.
