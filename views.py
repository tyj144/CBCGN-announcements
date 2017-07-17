from django.shortcuts import render
import feedparser, time

def display_posts(request):
	url = 'https://groups.google.com/forum/feed/cbcgn-youth-group/topics/rss.xml?num=50'
	# strips last 10 posts from RSS feed
	posts = feedparser.parse(url).entries[:10]
	# formats the date and time of each post
	for post in posts:
		post['published'] = (time.strftime('%B %-d', post.published_parsed), time.strftime('%-I:%M %p', post.published_parsed))
	# sends all 10 posts to be rendered in the webpage
	return render(request, 'google_group_posts.html', {'posts':posts})
