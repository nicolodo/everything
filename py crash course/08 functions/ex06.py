
# ex6 city country
def cityCountry(city="Paris",country="France"):
    return f"{city}, {country}"

print(cityCountry())

# ex7 Album maker
def makeAlbum(artist,album,tracks=None):
    albumInfo = {
            'artist':artist,
            'album':album
        }
    if tracks != None:
        albumInfo['tracks'] = tracks
    return albumInfo

# print(makeAlbum('Beatles','revolver','8'))

# ex8 User Albums
def ex8():
    active = True
    while active:
        artistName = "Please enter the name of the artist: "
        album = "Please enter the name of the album: "
        tracks = "Please enter the number of tracks if you want: "
        
        artist = input(artistName)
        album = input(album)
        tracks = input(tracks)

        if tracks == '':
            tracks = None
        print(makeAlbum(artist,album,tracks))
        againPrompt = "do you want to continue y/n: "
        again = input(againPrompt)

        if again.lower() == 'n':
            break
    
ex8()