import json
from Assignment6.Recommendations import *


'''
Create a json file of users to mimic the critic dictionary from Recommendation.py
'''


def create_critics_json():
    file_json = open("Data.json", "r")
    list_json = json.load(file_json)
    critic ={}
    for row in list_json:
        if row["user_id"] in critic.keys():
            critic[row["user_id"]].update({row["item_id"]: int(row["rating"])})
        else:
            critic[row["user_id"]] = {row["item_id"]: int(row["rating"])}
    file_json.close()
    file_correlated_users = open("Critic.json", "w")
    json.dump(critic, file_correlated_users)
    file_correlated_users.close()


'''
Use Recommendation.py function to calculate correlation and get top 5 and last five
'''


def find_correlated_users(user_id):
    create_critics_json()
    file_json = open("Critic.json", "r")
    list_json = json.load(file_json)
    list_correlation = []
    list_user = []
    for user in list_json:
        list_user.append(user)
        list_correlation.append(sim_pearson(list_json, user_id, user))
    file_json.close()
    list_correlation, list_user = zip(*sorted(zip(list_correlation, list_user)))
    print("Top 5 correlated users")
    print(list_user[:5])
    print("Last 5 correlated users")
    print(list_user[-5:])
    get_recommended_list(user_id, list_json)
    choose_real_you(list_json)


'''
Function to get recommendation list for user
'''


def get_recommended_list(user_id, list_json):
    list_recommendation = getRecommendations(list_json, user_id)
    print("Top 5 recommendation")
    print(list_recommendation[:5])
    print("Last 5 recommendation")
    print(list_recommendation[-5:])


def choose_real_you(list_json):
    list_json.update({"Me":{"161": 5, "162": 1}})
    list_transformed = transformPrefs(list_json)
    list_correlation_161 = []
    list_correlation_162 = []
    list_movies_161 = []
    list_movies_162 = []
    for movies in list_transformed:
        list_movies_161.append(movies)
        list_movies_162.append(movies)
        list_correlation_161.append(sim_pearson(list_transformed, "161", movies))
        list_correlation_162.append(sim_pearson(list_transformed, "162", movies))
    list_correlation_161, list_movies_161 = zip(*sorted(zip(list_correlation_161, list_movies_161)))
    list_correlation_162, list_movies_162 = zip(*sorted(zip(list_correlation_162, list_movies_162)))
    print("Top 5 correlated movies for my Least favourite movie")
    print(list_movies_162[:5])
    print("Last 5 correlated movies for my least favourite movie")
    print(list_movies_162[-5:])
    print("Top 5 correlated movies for my favourite movie")
    print(list_movies_161[:5])
    print("Last 5 correlated movies for my favourite movie")
    print(list_movies_161[-5:])


find_correlated_users("174")

