from django.shortcuts import render
import feedparser, time

def youth(request):
	# strips last 10 posts from RSS feed
	posts = feedparser.parse('https://groups.google.com/forum/feed/cbcgn-youth-group/topics/rss.xml?num=50').entries[:10]
	# formats the date and time of each post
	for post in posts:
		post['published'] = (time.strftime('%B %-d', post.published_parsed), time.strftime('%-I:%M %p', post.published_parsed))
	# sends all 10 posts to be rendered in the webpage
	return render(request, 'cbcgn_announcements/cbcgn_youth.html', {'posts':posts})