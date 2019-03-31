import json


def find_closest_user(age, occupation):
    file_json = open("Users.json", "r")
    list_json = json.load(file_json)
    list_gender = []
    for row in list_json:
        if row["gender"] == "M":
            list_gender.append(row)
    list_my_age = []
    for row in list_gender:
        if age == int(row["age"]):
            list_my_age.append(row)
    list_occupation = []
    for row in list_my_age:
        if row["occupation"] == occupation:
            list_occupation.append(row)
    if len(list_occupation) < 3:
        condition_break = False
        for row in list_my_age:
            for inner_row in list_occupation:
                if row["occupation"] != inner_row["occupation"]:
                    list_occupation.append(row)
                    condition_break = True
                    break
            if condition_break:
                break
        if len(list_occupation) < 3:
            condition_break = False
            for row in list_gender:
                for inner_row in list_occupation:
                    if row["user"] != inner_row["user"]:
                        list_occupation.append(row)
                        condition_break = True
                        break
                if condition_break:
                    break
    file_json.close()
    return list_occupation


def find_list_of_movie_ratings(age, occupation):
    list_users = find_closest_user(age, occupation)
    list_user_id = []
    for row in list_users:
        list_user_id.append(row["user"])
    file_json = open("Data.json", "r")
    list_json = json.load(file_json)
    list_favorites = []
    list_least_favourite = []
    for user in list_user_id:
        list_item_id = []
        list_ratings = []
        for row in list_json:
            if row["user_id"] == user:
                list_item_id.append(row["item_id"])
            list_ratings.append(int(row["rating"]))
        list_ratings, list_item_id = zip(*sorted(zip(list_ratings, list_item_id)))
        list_favorites.append(list_item_id[-1])
        list_least_favourite.append(list_item_id[0])
    file_json.close()
    file_json = open("Items.json", "r")
    list_json = json.load(file_json)
    list_least_favourite_movies = []
    list_favorites_movies = []
    for item_id in list_favorites:
        for row in list_json:
            if row["movie id"] == item_id:
                list_favorites_movies.append(row["movie title"])
    for item_id in list_least_favourite:
        for row in list_json:
            if row["movie id"] == item_id:
                list_least_favourite_movies.append(row["movie title"])

    for i in range(0, len(list_user_id)):
        print("For user id:" + list_user_id[i])
        print("Favorite:" + list_favorites_movies[i])
        print("Favorite movie:" + list_favorites[i])
        print("Least favorite:" + list_least_favourite[i])
        print("Least favorite movie:" + list_least_favourite_movies[i])


find_list_of_movie_ratings(30, 'student')