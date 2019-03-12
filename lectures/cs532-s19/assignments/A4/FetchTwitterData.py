import twitter
import csv
import math

'''
Create Twitter Instance. All the fields can be collected from the developer site of Twitter
'''


def create_twitter_instance():
    api = twitter.Api(consumer_key='5Q3CFnvq02nKj6kI9gRpGNHXH',
                      consumer_secret='4OBnuBjedjwZUZmtslwzzPmWxeQtN7LHUeYHf4jsqZjQkEyW4v',
                      access_token_key='907341293717737473-for4ikiKhPAHxD54pnRqhJSPpr1QmNB',
                      access_token_secret='jV6TplxXfCQOu8C8zArB2wzlwGisq2Y0kRHUtrvuKYQNr',
                      sleep_on_rate_limit=True)
    return api


'''
Function to fetch Twitter followers list 
'''


def fetch_twitter_followers():
    api = create_twitter_instance()
    file_object = open("TwitterData.csv","w")
    fieldnames = ["Name", "Followers", "Friends"]
    writer = csv.DictWriter(file_object, fieldnames=fieldnames)
    writer.writeheader()
    response = api.GetFollowers(screen_name="phonedude_mln")
    for friend in response:

        insert_row = {"Name": friend.name, "Followers": math.log(friend.followers_count + 1, 2),
                      "Friends": math.log(friend.friends_count + 1, 2)}
        writer.writerow(insert_row)
    file_object.close()


'''
Function to fetch Twitter following list 
'''


def fetch_twitter_following():
    api = create_twitter_instance()
    file_object = open("TwitterDataFollowing.csv","w")
    fieldnames = ["Name", "Followers", "Friends"]
    writer = csv.DictWriter(file_object, fieldnames=fieldnames)
    writer.writeheader()
    response = api.GetFriends(screen_name="phonedude_mln")
    for friend in response:

        insert_row = {"Name": friend.name, "Followers": math.log(friend.followers_count + 1, 2),
                      "Friends": math.log(friend.friends_count + 1, 2)}
        writer.writerow(insert_row)
    file_object.close()


fetch_twitter_followers()
fetch_twitter_following()
