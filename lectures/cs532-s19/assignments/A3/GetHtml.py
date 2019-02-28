import requests
import hashlib
from boilerpipe.extract import Extractor
import os
import math
import scipy.stats as stats

'''
Function to fetch URLs
'''


def get_raw_html():
    file_urls = open("Urls_Uniq_Expanded.txt", "r")
    file_urls_downloaded = open("Urls_downloaded.txt", "w")
    count = 0
    for line in file_urls:
        url = line.rstrip().split("|||")[0]
        url_digest = hashlib.sha3_256(url.encode()).hexdigest()
        try:
            response = requests.get(url)
            if response.status_code == 200 and count < 1000:
                count += 1
                file_urls_downloaded.write(url + ": " + url_digest + "\n")
                file_raw_html = open("rawHTML/" + url_digest, "w")
                file_raw_html.write(response.text)
                file_raw_html.close()
            elif count == 1000:
                break
        except Exception as e:
            print(e)
    file_urls_downloaded.close()
    file_urls.close()


'''
Function boilerpipe code
'''


def boilerpipe_code():
    files_urls = open("Urls_Uniq_Expanded.txt", "r")
    for line in files_urls:
        url = line.rstrip().split("|||")[0]
        try:
            extractor = Extractor(extractor='ArticleExtractor', url= url)
            url_digest = hashlib.sha256(url.encode()).hexdigest()
            file_open = open("boilerHTML/" + url_digest, "w")
            response = extractor.getText()
            file_open.write(response)
            file_open.close()
        except Exception as e:
            print(e)


'''
Link urls to sha256 
'''


def urls_to_hash():
    files_urls = open("Urls_Uniq_Expanded.txt", "r")
    file_hash = open("Urls_hash.txt", "w")
    for line in files_urls:
        url = line.rstrip().split("|||")[0]
        try:
            url_digest = hashlib.sha256(url.encode()).hexdigest()
            file_hash.write(str(url_digest) + "|||" + url + "\n")
        except Exception as e:
            print(e)
    file_hash.close()
    files_urls.close()


'''
Find term frequency and inverse term frequency from Corpus
'''


def find_tf_idf():

    words_list = ["Twitter", "Facebook", "Sports", "America", "Trump", "President", "Friends", "Tweet", "Post", "Senate"]
    list_outputs = []
    for i in range(0, len(words_list)):
        list_outputs.append([])
    for word in words_list:
        for files in os.listdir("boilerHTML"):
            file_open = open("boilerHTML/" + files, "r")
            count = 0
            count_total = 0
            for line in file_open:
                words_in_line = line.split(" ")
                for word_in_line in words_in_line:
                    count_total += 1
                    if word.lower() == word_in_line.lower():
                        count += 1
            if count > 0:
                list_temp = []
                list_temp.append(files)
                list_temp.append(str(count / count_total))
                list_outputs[words_list.index(word)].append(list_temp)
            file_open.close()
    print(list_outputs)

    total_corpus = 0
    for files in os.listdir("boilerHTML"):
        total_corpus += 1

    for i in range(0, len(list_outputs)):
        for j in range(0, len(list_outputs[i])):
            idf = math.log((total_corpus/ len(list_outputs[i])), 2)
            list_outputs[i][j].append(str(idf))
            list_outputs[i][j].append(str(idf * float(list_outputs[i][j][1])))

    file_hashes = open("Urls_hash.txt", "r")
    list_hash = []
    list_url = []
    for line in file_hashes:
        line_split = line.split("|||")
        list_hash.append(line_split[0])
        list_url.append(line_split[1])
    file_hashes.close()

    for i in range(0, len(list_outputs)):
        file_words = open("wordFrequency/" + words_list[i] + ".txt", "w")
        for j in range(0, len(list_outputs[i])):
            for k in range(0, len(list_outputs[i][j])):
                if k == 0:
                    file_words.write(list_url[list_hash.index(list_outputs[i][j][k])].rstrip() + "|||")
                else:
                    file_words.write(list_outputs[i][j][k] + "|||")
            file_words.write("\n")
        file_words.close()


'''
Calculate Kendel Tau
'''


def kendel_tau():
    a = [0.03, 0.027, 0.051, 0.07, 0.021, 0.018, 0.124, 0.026, 0.058, 0.031, 0.048, 0.096]
    b = [0.9, 0.2, 0, 0, 0, 0, 0,0.6, 0.9, 0, 0.8, 0]
    tau, p_value = stats.kendalltau(a, b)
    print(tau)
    print(p_value)


kendel_tau()
#find_tf_idf()
# urls_to_hash()
# boilerpipe_code()
# get_raw_html()


