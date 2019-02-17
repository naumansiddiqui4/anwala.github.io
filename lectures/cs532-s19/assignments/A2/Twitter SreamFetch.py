import twitter
import ast
import re
import requests
import csv

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
Fetch Twitter Stream
'''


def fetch_twitter_stream():
    file_write = open("StreamOutput2.txt", "w")
    api = create_twitter_instance()
    stream_response = api.GetStreamFilter(track="Jussie, #HTGAWM, Nadia")
    for i in stream_response:
        file_write.write(str(i) + "\n")
    file_write.close()


'''
Parse Stream Output
'''


def parse_stream_output():
    file_open = open("StreamOutput1.txt", "r")
    file_write = open("Urls.txt", "w")
    for line in file_open:
        tweet_output = ast.literal_eval(line)
        print(tweet_output)
        if "limit" in tweet_output:
            continue
        tweet_text = (tweet_output["text"])
        tweet_url = parse_url_from_text(tweet_text)
        if tweet_url is not None:
            file_write.write(tweet_url + "\n")
    file_write.close()
    file_open.close()


'''
Check Urls fetched from tweets
'''


def check_urls():
    file_open = open("Urls_Uniq.txt", "r")
    file_urls_expand = open("Urls_Uniq_Expanded.txt", "a+")
    for line in file_open:
        print(line)
        try:
            url = line.rstrip()
            count = 0
            while True:
                if count > 10:
                    break
                response = requests.head(url)
                print(response.status_code)
                if 300 < response.status_code < 400:
                    url = response.headers['location']
                    count += 1
                else:
                    file_urls_expand.write(url + "|||" + str(response.status_code) + "\n")
                    break
        except Exception as e:
            print(e)
            print(line.rstrip())
    file_open.close()
    file_urls_expand.close()


'''
Parse Url from a Text
'''


def parse_url_from_text(text_string):
    tweet_url = re.search("(?P<url>https?://[^\s]+)", text_string)
    if tweet_url is not None:
        tweet_url = tweet_url.group("url")
    return tweet_url


'''
Utility function to convert ||| separated file to csv
'''


def convert_to_csv():
    file_timemaps = open("Urls_carbondate.txt", "r")
    file_csv = open("Urls_carbondate.csv", "w")
    fieldnames = ["Url", "CarbonDate"]
    csv_object = csv.DictWriter(file_csv, fieldnames=fieldnames)
    csv_object.writeheader()
    for line in file_timemaps:
        line_split = line.rstrip().split("|||")
        if int(line_split[1]) == -1:
            line_split[1] = 0
        insert_row = {"Url": line_split[0], "CarbonDate": line_split[1]}
        csv_object.writerow(insert_row)
    file_timemaps.close()
    file_csv.close()


convert_to_csv()
# check_urls()
# parse_stream_output()
# fetch_twitter_stream()
