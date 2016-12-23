from django.shortcuts import render
import feedparser, time

def youth(request):
	posts = feedparser.parse('https://groups.google.com/forum/feed/cbcgn-youth-group/topics/rss.xml?num=50').entries[:10]
	for post in posts:
		post['published'] = (time.strftime('%B %-d', post.published_parsed), time.strftime('%-I:%M %p', post.published_parsed))
	return render(request, 'cbcgn_announcements/cbcgn_youth.html', {'posts':posts})