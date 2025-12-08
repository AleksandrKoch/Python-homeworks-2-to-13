# Iterating over Dictionaries

# Given the list of movies below, please use view objects (keys(), values(), items() - where necessary) to answer
# the questions:

# - Is Black Panther in the list of movies?
# - Is there any movie for the year 2021?
# - Print a message for each element that shows the year, the title and the position in the dictionary (1-5).
#   Hint: use a counter.

films = {
   2016: "Star Wars: Episode VII - The Force Awakens",
   2017: "Star Wars: Episode VIII - The Last Jedi",
   2018: "Black Panther",
   2019: "Avengers: Endgame",
   2020: "Bad Boys for Life"
}
# - Is Black Panther in the list of movies?
for film in films.values():
    if film == "Black Panther":
        print("Black Panther is in the list")
        break
    else:
        if film == list(films.values())[-1]:
            print("Black Panther is not the list")

# - Is there any movie for the year 2021?
for year in films.keys():
    if films[year] == 2021:
        print("year 2021 is in the list of films")
        break
    else:
        if year == list(films.keys())[-1]:
            print("year 2021 is not in the list of films")

# - Print a message for each element that shows the year, the title and the position in the dictionary (1-5).
#   Hint: use a counter.
counter = 0
for year, film in films.items():
    counter += 1
    print(f"{counter}: {year} - {film}")