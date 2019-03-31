import json
import csv


def read_users_table():
    path_data_set = "/home/msiddique/WSDL_Work/WebScience/Assignment6/ml-100k/"
    file_open = open(path_data_set + "u.user", "r")
    list_json = []
    reader = csv.reader(file_open, delimiter="|")
    for row in reader:
        insert_row = {'user': row[0],'age': row[1],'gender': row[2],'occupation': row[3],'zip': row[4]}
        list_json.append(insert_row)
    file_json = open("Users.json", "w")
    json.dump(list_json, file_json)
    file_open.close()
    file_json.close()


def read_items_table():
    path_data_set = "/home/msiddique/WSDL_Work/WebScience/Assignment6/ml-100k/"
    # ratings = pd.read_table(path_dataset + 'u.data',sep='::',names=['user','movie','rating','time'])
    file_open = open(path_data_set + "u.item", "r", encoding = "ISO-8859-1")
    list_json = []
    reader = csv.reader(file_open, delimiter="|")
    for row in reader:
        print(row)
        insert_row = {"movie id": row[0], "movie title": row[1], "release date": row[2], "video release date": row[3],
                      "IMDb URL": row[4], "unknown": row[5], "Action": row[6], "Adventure": row[7], "Animation":row[8],
                      "Children's": row[9], "Comedy": row[10], "Crime": row[11], "Documentary": row[12],
                      "Drama": row[13], "Fantasy": row[14], "Film-Noir": row[15], "Horror": row[16], "Musical": row[17],
                      "Mystery": row[18], "Romance": row[19], "Sci-Fi": row[20], "Thriller": row[21], "War": row[22],
                      "Western": row[23]}
        list_json.append(insert_row)
    file_json = open("Items.json", "w")
    json.dump(list_json, file_json)
    file_open.close()
    file_json.close()


def read_users_data_table():
    path_data_set = "/home/msiddique/WSDL_Work/WebScience/Assignment6/ml-100k/"
    file_open = open(path_data_set + "u.data", "r")
    list_json = []
    reader = csv.reader(file_open, delimiter="\t")
    for row in reader:
        insert_row = {"user_id": row[0], "item_id": row[1], "rating": row[2], "timestamp": row[3]}
        list_json.append(insert_row)
    file_json = open("Data.json", "w")
    json.dump(list_json, file_json)
    file_open.close()
    file_json.close()


# read_users_data_table()
# read_items_table()
read_users_table()