# def city_country():
#     country = input("请输入你的国家：")
#     city = input("请输入你的城市：")
#     return country,city
# print(city_country())

# def city_country(city, country):
#  """返回一个类似于'Santiago, Chile'的字符串。"""
#  return f"{city.title()}, {country.title()}"
# city = city_country('santiago', 'chile')
# print(city)


# def make_album(artist, title, tracks=0):
#     album_dict = {'artist': artist.title(),'title': title.title(),}
#     if tracks:
#         album_dict['tracks'] = tracks
#     return album_dict
# album = make_album('metallica', 'ride the lightning')
# print(album)
# album = make_album('beethoven', 'ninth symphony')
# print(album)
# album = make_album('willie nelson', 'red-headed stranger')
# print(album)
# album = make_album('iron maiden', 'piece of mind', tracks=8)
# print(album)

def make_album(artist,titles,tracks=0):
    albun_dict = {
        'artist':artist.title(),
        'title':titles.title(),
    }
    if tracks:
        albun_dict['tracks'] = tracks
    return albun_dict
print("Enter 'quit' at any time to stop.")
while True:
    artist = input("请输入你喜欢的歌手名：")
    if artist == "quit":
        break
    titles = input("请输入你喜欢的专辑名：")
    if titles == "quit":
        break
    album = make_album(artist,titles)
    print(album)