# Movie Rating Analysis

movies = ["Dangal", "3 Idiots", "Jawan", "Pathaan"]
ratings = [9, 10, 8, 7]

print("MOVIE RATING ANALYSIS")
print("---------------------")

for i in range(len(movies)):
    print(movies[i], ":", ratings[i])

average = sum(ratings) / len(ratings)

print("---------------------")
print("Average Rating:", average)

highest = ratings.index(max(ratings))

print("Highest Rated Movie:", movies[highest])
print("Highest Rating:", ratings[highest])