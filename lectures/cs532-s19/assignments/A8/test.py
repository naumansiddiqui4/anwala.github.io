import Assignment8.docclass
import os


'''
# remove previous db file
if os.path.exists("/home/msiddique/WSDL_Work/WebScience/Assignment8/SpamClassifier.db"):
    os.remove("/home/msiddique/WSDL_Work/WebScience/Assignment8/SpamClassifier.db")

cl.setdb('SpamClassifier.db')
Assignment8.docclass.spamTrain(cl)

#classify text: "the banking dinner" as spam or not spam
print( cl.classify('the banking dinner'))
'''


def classify_emails():
    cl = Assignment8.docclass.naivebayes(Assignment8.docclass.getwords)
    cl.setdb('SpamClassifier.db')
    sample_train(cl)
    testing_data = "/home/msiddique/WSDL_Work/WebScience/Assignment8/Dataset/testing/"
    # classify_document(cl, testing_data + "/spam/" + "2.txt")
    calculate_confusion_matrix(cl)


def sample_train(cl):
    training_data = "/home/msiddique/WSDL_Work/WebScience/Assignment8/Dataset/training/"
    for dir, path, files in os.walk(training_data):
        for file_name in files:
            with open(dir + "/" + file_name, "r") as file_object:
                file_content = file_object.read()
                print(file_content)
                file_tag = dir.split("/")[-1]
                if file_tag == "notspam":
                    file_tag = "not spam"
                cl.train(file_content, file_tag)


def classify_document(cl, file_path):
    with open(file_path, "r")as file_object:
        file_content = file_object.read()
        return cl.classify(file_content)


def calculate_confusion_matrix(cl):
    fn = 0
    fp = 0
    tn = 0
    tp = 0
    testing_data = "/home/msiddique/WSDL_Work/WebScience/Assignment8/Dataset/testing/"
    for dir, path, files in os.walk(testing_data):
        for file_name in files:
            classifier_result = classify_document(cl, dir + "/" + file_name)
            file_tag = dir.split("/")[-1]
            if file_tag == "notspam":
                file_tag = "not spam"
            if file_tag == "spam" and classifier_result == "spam":
                tp += 1
            elif file_tag == "spam" and classifier_result == "not spam":
                fp += 1
            elif file_tag == "not spam" and classifier_result == "spam":
                fn += 1
            elif file_tag == "not spam" and classifier_result == "not spam":
                tn += 1

            print(classifier_result)
    print("TP: " + str(tp))
    print("FP: " + str(fp))
    print("TN: " + str(tn))
    print("FN: " + str(fn))
    print("Recall: " + str(tp/(tp + fn)))
    print("Precision: " + str(tp / (tp + fp)))
    print("Accuracy: " + str((tp + tn) / (tn + tp + fn + fp)))


classify_emails()
