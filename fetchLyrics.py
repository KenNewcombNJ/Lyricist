import os
import commands
import dbus
import urllib
import re
import time
import sys

def nopunc(s):
    return ''.join(e for e in s if e.isalnum())

def getLyrics(song):
	"""Attempts to gather lyrics from various sources."""
	if(AZLyrics(song) != True):
		SongLyrics(song)

def AZLyrics(song):
	"""Fetches lyrics from AZLyrics.com"""

	# Prepare artist and title for lyrics search.
	artist = nopunc(song[0].replace('The', '')).lower()
	title = nopunc(song[1]).lower()
	
	# construct the lyrics URL
	urlstring = "http://www.azlyrics.com/lyrics/{0}/{1}.html".format(artist, title)
	
	# get the HTML at the proper URL
	lyrics = urllib.urlopen(urlstring)

	try:
		raw_lyrics = lyrics.read().split('<!-- start of lyrics -->')[1]
	except IndexError:
		print "AZLyrics: No lyrics found..."
		return False
	
	raw_lyrics = raw_lyrics.split('<!-- end of lyrics -->')[0]
	
	processed_lyrics = re.sub('<.*?>', '', rawlyrics)

	print processed_lyrics
	return True

def SongLyrics(song):
	"""Fetches lyrics from SongLyrics.com"""

	artist = song[0].replace('The', '').replace(" ", "-").lower()
        title = song[1].replace(" ", "-").lower()
	
	# Construct the lyrics URL
	urlstring = "http://www.songlyrics.com/{0}/{1}-lyrics".format(artist,title)
	# Fetch the HTML at the URL
	lyrics = urllib.urlopen(urlstring)

	try:
		raw_lyrics = lyrics.read().split("<p id=\"songLyricsDiv\"  class=\"songLyricsV14 iComment-text\">")[1]
	except IndexError:
		print "SongLyrics: No lyrics found..."
		return False

	raw_lyrics = raw_lyrics.split("</div>")[0]
	
	processed_lyrics = re.sub('<.*?>', '', raw_lyrics)

	print processed_lyrics
	return True

def cleanLyrics(lyrics):
	"""Cleans up lyrics, removing HTML tags"""
	# remove HTML tags
	lyrics = re.sub('<.*?>', '', lyrics)
	return lyrics
	
	
	title = "{0} by {1}".format(Title, Artist)
	print title
	
	for characters in title:
		sys.stdout.write('-')		

