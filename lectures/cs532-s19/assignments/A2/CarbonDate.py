import requests
import ast
import datetime


'''
Function to carbondate urls 
'''


def carbondate_urls():

    file_urls_expand = open("Urls_Uniq_Expanded.txt", "r")
    file_carbondate = open("Urls_carbondate.txt", "w")
    current_date = datetime.datetime.now()
    for line in file_urls_expand:
        try:
            command = "http://localhost:8888/cd/"
            command = command + line.rstrip().split("|||")[0]
            print(command)
            response = requests.get(command)
            if response.status_code == 200:
                print(response.text)
                carbon_date_result = ast.literal_eval(response.text)
                creation_date = carbon_date_result["estimated-creation-date"]
                creation_date = datetime.datetime.strptime(creation_date, "%Y-%m-%dT%H:%M:%S")
                print(creation_date)
                print(current_date)
                print((current_date - creation_date).days)
                file_carbondate.write(line.rstrip().split("|||")[0] + "|||" + str((current_date - creation_date).days) + "\n")
        except Exception as e:
            continue
    file_carbondate.close()
    file_urls_expand.close()


carbondate_urls()