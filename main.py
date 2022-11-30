import feedparser
import re
import time

genres = ['Adventure', 'Action', 'Role Playing', 'Visual Novel', 'Platformer', 'Puzzle', 'Simulation', 'Interactive Fiction', 'Survival', 'Shooter', 'Strategy', 'Fighting', 'Card Game', 'Educational', 'Racing', 'Rhythm', 'Sports', 'Other']
result = {x:0 for x in genres}
total = 0

pages = input("How many pages do you want to check? ")

try:
    pages = int(pages)
except ValueError:
    print("That's not a valid number!")
    quit()

start = time.time()
for i in range(pages):
    feed = feedparser.parse(f'https://itch.io/games.xml?page={i}')
    for i in feed.entries:
        title = i['title']
        genre = re.search(rf"\[({'|'.join(genres)})\]", title)
        if genre != None:
            result[genre.group()[1:-1]] += 1
            total += 1

print(dict(sorted(result.items(), key=lambda item: item[1], reverse=True)))
for key, val in dict(sorted(result.items(), key=lambda item: item[1], reverse=True)).items():
    if val != 0:
        print(f'{key}{" "*(20-len(key))}| {total/val:.2f}% ({val} games)')
    else:
        print(f'{key}{" "*(20-len(key))}| 0% (0 games)')
print(f"Results in {time.time()-start:.2f} seconds")
