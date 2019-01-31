import requests
import bs4
import sys
import re

'''
Function to request pages
'''


def make_network_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if "application/pdf" in response.headers['content-type'] and url in list_extracted_links:
                file_pdf_links.write(url + "\n")
                print(response.text)
            if url not in list_extracted_links:
                extract_links(response.text)
        elif response.status_code == 301 or response.status_code == 302:
            for resp in response.history:
                list_extracted_links.append(resp.url)
    except requests.exceptions.MissingSchema as err:
        print("error: " + str(err) + "URL: " + url)
    except Exception as err:
        print("error: " + str(err))


'''
Function to extract links from Web Page 
'''


def extract_links(content):
    soup = bs4.BeautifulSoup(content, "html.parser")
    link_a_tags = soup.find_all('a', href=True)
    for tags in link_a_tags:
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if re.match(regex, tags["href"]) is not None:
            list_extracted_links.append(tags["href"])


'''
Function to check if queue is empty
'''


def check_list():
    while True:
        item = list_base_links[0]
        file_pdf_links.write("Links: " + item + "\n")
        file_pdf_links.write("PDF Links" + "\n")
        make_network_request(item)
        del list_base_links[0]
        if len(list_base_links) == 0:
            break
    while True:
        item = list_extracted_links[0]
        make_network_request(item)
        del list_extracted_links[0]
        if len(list_extracted_links) == 0:
            break


if __name__ == "__main__":
    list_base_links = []
    list_extracted_links = []
    file_pdf_links = open("PDF_Links.txt", "w")
    if len(sys.argv) > 1:
        argument_length = 0
        while argument_length < len(sys.argv):
            if argument_length > 0:
                list_base_links.append(sys.argv[argument_length])
                print("The arguments is: " + sys.argv[argument_length])
            argument_length += 1
    else:
        list_base_links.append("http://www.cs.odu.edu/~mln/teaching/cs532-s17/test/pdfs.html")
    check_list()
    file_pdf_links.close()
