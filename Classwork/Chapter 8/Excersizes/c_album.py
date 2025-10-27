# 8-7 Album
# def make_album(artist_name, album_title, num_songs=None):
#     """Build a dictionary describing a music album"""
#     album = {
#         'artist': artist_name.title(),
#         'title': album_title.title(),
#     }

#     if num_songs:
#         album['songs'] = num_songs
#     return album

# album1 = make_album('fatman', 'kamp kommedant')
# album2 = make_album('coldplay', 'viva la vida')
# album3 = make_album('eminem', 'lose yourself')
# album4 = make_album('system of a down', 'toxicity', 11)

# print(album1)
# print(album2)
# print(album3)
# print(album4)

# 8-8 User albums
def make_album(artist_name, album_title, num_songs=None):
    """Build a dictionary describing a music album"""
    album = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }

    if num_songs:
        album['songs'] = num_songs
    return album

while True:
    print("\nEnter Album information (or type 'q' to quit)")

    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break

    title = input("Album title: ")
    if title.lower() == 'q':
        break

    songs = input("Number of songs (Press 'Enter to skip): ")
    if songs.lower() == 'q':
        break

    if songs:
        album = make_album(artist, title, int(songs))
    else:
        album = make_album(artist, title)

    print(f"\nAlbum information: {album}")

print("\nThank for using the album maker!")