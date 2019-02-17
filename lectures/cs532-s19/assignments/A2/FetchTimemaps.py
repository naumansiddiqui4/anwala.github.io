import requests


'''
Function to count timemaps
'''


def fetch_timemaps():

    file_urls_expand = open("Urls_Uniq_Expanded.txt", "r")
    file_timemaps = open("Urls_timemap.txt", "w")
    for line in file_urls_expand:
        try:
            command = "http://localhost:1208/timemap/json/"
            command = command + line.rstrip().split("|||")[0]
            response = requests.head(command)
            file_timemaps.write(line.rstrip().split("|||")[0] + "|||" + str(response.headers["X-Memento-Count"]) + "\n")

        except Exception as e:
            exit()
    file_timemaps.close()
    file_urls_expand.close()


fetch_timemaps()