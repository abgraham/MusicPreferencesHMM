
# we want this to take in the big file of user data
# to make it just into a list of song IDs
# and then to make another file that's just a list of user ID's split up by spaces (so that the webppl file can use the .split() method on it)

file = open('userdata2.txt')
listOfSongIDs = []
for line in file:
    #print (line.split())[2]
    songID = (line.split())[-1]
    listOfSongIDs.append(songID)

listOfUniqueIDs = set(listOfSongIDs)

print listOfSongIDs
stringOfIDs = ''
for song in listOfSongIDs:
    stringOfIDs += (song + ' ')

print 'final string: ' + stringOfIDs
# TODO: make this specific to the file it had been before
file = open('parsed_user_data.txt', 'w')
for song in listOfSongIDs:
    file.write(song + ' ')
file.close()

file = open('parsed_unique_user_data.txt', 'w')
for song in listOfUniqueIDs:
    file.write(song + ' ')
file.close()

