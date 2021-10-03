import animeworld as aw
import numpy as np

index = 0
animeUrl = ''

print('Anime downloader')
animeSelection = str(input('Type the anime name: '))

res = aw.find(animeSelection)

# what if no res found

print('Results: ')
for el in res:
    index += 1
    print(str(index) + ') ' + el)

try:
    selection = int(input('Type the number of the anime you want: '))
except:
    print('Your selection is not a number')
    exit(1)

index = 0

data = list(res.items())
anime_list = np.array(data)

for el in res:
    index += 1
    if str(index) == str(selection):
        animeUrl = anime_list[index-1][1]
        break

'''
try:
    howManyEpisodes=int(input('How many episodes do you want to download? (ALL): '))
except:
    print('All episodes selected')
    howManyEpisodes = -1
'''
downloadConfirmation = str(input('Do you want to start the download? (Y,n): '))

anime = aw.Anime(link=animeUrl)
if(downloadConfirmation == '' or downloadConfirmation.upper() == 'Y'):
    print('You can stop the process by pressing (CTRL+C)')
    for episodio in anime.getEpisodes():
        print('Episode (' + episodio.number + ')')

        if(episodio.download()):
            print("Downloaded")
        else:
            print("Error")

        """
        if howManyEpisodes not == -1:
            if howManyEpisodes == howManyEpisodes:
                break
        """