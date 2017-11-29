import os
import sys
import musixmatch
from musixmatch import track as TRACK
from musixmatch import artist as ARTIST
from musixmatch import tracking as TRACKING

#MUSIXMATCH_API_KEY = "437f020971788f570fb9683878c740e8"

#tracks = TRACK.search(q='Rick Astley Never Gonna Give You Up')
#print '********** LIST OF TRACKS ACQUIRED ************'
#for k in range(min(3,len(tracks))):
#   print tracks[k]

# track = TRACK.Track('e0140a67-e4d1-4f13-8a01-364355bee46e', True, False, None);
# print track


# track = TRACK.Track('e0140a67-e4d1-4f13-8a01-364355bee46e', True, False, None);
# print track

# track = TRACK.Track('118800c2-c0d9-4560-bef4-e9fc85d0d036', True, False, None);
# print track

#s = "a426ebab-2000-4e1b-9e4c-bcbe62f69bb4"
s = "a426ebab20004e1b9e4cbcbe62f69bb4"
u = unicode(s, "utf-8")

# track = TRACK.Track("a426ebab20004e1b9e4cbcbe62f69bb4", True, False, None);
# print track

# track = TRACK.Track("a426ebab-2000-4e1b-9e4c-bcbe62f69bb4", True, False, None);
# print track

#artist = ARTIST.Artist("cc197bad-dc9c-440d-a5b5-d52ba2e14234, True, None);
#artist = ARTIST.Artist("cc197bad-dc9c-440d-a5b5-d52ba2e14234, True, None);
artist = ARTIST.Artist("cc197baddc9c440da5b5d52ba2e14234", True, None);
print artist

# artist = ARTIST.Artist(10832)
# print '*********** ARTIST 10832 ACQUIRED ************'
# print artist