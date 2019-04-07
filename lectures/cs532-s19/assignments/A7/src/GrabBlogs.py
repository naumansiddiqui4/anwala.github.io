import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import os
import sys
import clusters
#import generatefeedvector


'''
Function to fetch Blogger profiles and pass profiles to get their blogs
'''


def fetch_blogs(query, limit):
    list_blogger_profiles = []
    list_blogger_urls = []
    output_directory = "Outputs/"
    blogger_url = "http://www.blogger.com/profile-find.g?t=m&q=" + query
    if not os.path.isdir(output_directory):
        os.mkdir(output_directory)
    while len(list_blogger_urls) < limit:
        response = requests.get(blogger_url)
        print(blogger_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            profiles_tag_selector = soup.find_all('dl')
            for tags in profiles_tag_selector:
                profile_url_selector = tags.find('a', href=True)
                blogger_profile_url = "http://www.blogger.com/" + profile_url_selector['href'][1:]
                list_blogger_profiles.append(blogger_profile_url)
            list_blogger_urls.extend(fetch_blog_urls(list_blogger_profiles, limit))
            print(list_blogger_urls)
            list_blogger_profiles = []
            blogger_url_selector = soup.find('a', {'id': 'next-btn'},
                                             href=True)
            if blogger_url_selector:
                blogger_url = blogger_url_selector['href']
            else:
                break
            print(len(list_blogger_urls))
    print(len(list_blogger_urls))
    if os.path.isfile(output_directory + "BlogUrls1.txt"):
        file_blog_urls = open(output_directory + "BlogUrls.txt", "a+")
    else:
        file_blog_urls = open(output_directory + "BlogUrls.txt", "w")
    for urls in list_blogger_urls:
        file_blog_urls.write(urls + "\n")
    file_blog_urls.close()


'''
Function to fetch blog urls from Blogger profiles 
'''


def fetch_blog_urls(list_blogger_profiles, limit):
    count = 0
    list_blogger_urls = []
    for profile in list_blogger_profiles:
        if count < limit:
            response = requests.get(profile)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                profile_blog_link_selector = soup.find_all('span', dir=True)
                for profile_blog_links in profile_blog_link_selector:
                    # print(profile_blog_links)
                    if profile_blog_links['dir'] == 'ltr':
                        blog_links_selector = profile_blog_links.find_all('a', href=True)
                        # print(blog_links_selector)
                        for blog_links in blog_links_selector:
                            print(blog_links['href'])
                            try:
                                response = requests.head(blog_links['href'], timeout=60)
                                print(response.headers)
                                if response.encoding and (response.encoding == 'ISO-8859-1' or response.encoding == 'UTF-8'):
                                    list_blogger_urls.append(blog_links['href'])
                                    print()
                                    count += 1
                            except Exception as e:
                                print(e)
    print(list_blogger_urls)
    return list_blogger_urls


def write_blogs():
    if not os.path.isdir("Outputs/blogs/"):
        os.mkdir("Outputs/blogs/")
    file_urls = open("Outputs/BlogUrls.txt", "r")
    file_list = open("Outputs/BlogList.txt", "w")
    count = 0
    for line in file_urls:
        response = requests.get(line.rstrip())
        if response.status_code == 200:
            filename = "blog_" + str(count) + ".txt"
            file_blog = open("Outputs/blogs/" + filename, "w")
            file_blog.write(response.text)
            file_blog.close()
            count += 1
            file_list.write(filename + " " + line.rstrip() + "\n")
    file_list.close()
    file_urls.close()
'''
Create Blog Matrix for blogger urls 
'''

'''
def create_blog_matrix():
    apcount = {}
    word_counts = {}
    feed_list = [line.rstrip() for line in open('Outputs/BlogUrls.txt')]
    for feed_url in feed_list:
        print(feed_url)
        (title, wc) = generatefeedvector.getwordcounts(feed_url)
        if title and wc:
            word_counts[title] = wc
            for (word, count) in wc.items():
                apcount.setdefault(word, 0)
                if count > 1:
                    apcount[word] += 1
    print(len(apcount))
    wordlist = []
    for (w, bc) in apcount.items():
        frac = float(bc) / len(feed_list)
        if frac > 0.1 and frac < 0.5:
            wordlist.append(w)

    out = open('Outputs/blogdata.txt', 'w')
    out.write('Blog')
    for word in wordlist:
        out.write('\t%s' % word)
    out.write('\n')
    print(len(word_counts))
    for (blog, wc) in word_counts.items():
        print(blog)
        out.write(blog)
        for word in wordlist:
            if word in wc:
                out.write('\t%d' % wc[word])
            else:
                out.write('\t0')
        out.write('\n')


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
'''

'''
Replicate code from Programming-Collective-Intelligence/blob/master/chapter3/generatefeedvector.py
'''

'''
def get_word_count(url):

    # Parse the feed
    print("Word Count")
    try:
        response = requests.get(url, timeout=60)
        wc = {}
        if response.status_code == 200:
            # Loop over all the entries
            soup = BeautifulSoup(response.text, 'html.parser')
            texts = soup.findAll(text=True)
            visible_texts = filter(tag_visible, texts)
            title = soup.title.string
            summary = " ".join(t.strip() for t in visible_texts)
            # Extract a list of words
            words = get_words(title + ' ' + summary)
            for word in words:
                wc.setdefault(word, 0)
                wc[word] += 1
            print(title.rstrip())
            print(wc)
            return title.rstrip(), wc
    except Exception as e:
        print(e)
        print(url)
        return None, None
    return None, None


def get_words(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']





def draw_acii_dendogram():
    blognames, words, data = clusters.readfile('Outputs/blogdata.txt')
    clust = clusters.hcluster(data)
    clusters.printclust(clust, labels=blognames)


def draw_dendogram():
    blognames, words, data = clusters.readfile('Outputs/blogdata.txt')
    clust = clusters.hcluster(data)
    clusters.drawdendrogram(clust, blognames, jpeg='blogclust.jpg')

def text():
    blognames, words, data = clusters.readfile('Outputs/blogdata.txt')
    coords = clusters.scaledown(data)
    kclust = clusters.kcluster(data, k=4)


# fetch_blogs("Twitter", 100)
# fetch_blogs("Cricket", 56)
# fetch_blogs("Patna", 16)
# fetch_blogs("Manchester", 13)
# fetch_blogs("India", 6)
'''
'''
fetch_blogs("Music", 100)
file_open = open("Outputs/BlogUrls.txt", "a+")
file_open.write("http://f-measure.blogspot.com/" + "\n")
file_open.write("http://ws-dl.blogspot.com/" + "\n")
file_open.close()
'''

def createDendrogram():
    blogs, colnames, data = clusters.readfile('Outputs/blogdata.txt')
    cluster = clusters.hcluster(data)
    clusters.drawdendrogram(cluster, blogs, jpeg='../docs/q2Dendrogram.jpg')
    f = open("Outputs/q2ASCII.txt", 'w')
    sys.stdout = f
    clusters.printclust(cluster, labels=blogs)
    f.close()
    sys.stderr.close()


def kmeans():
    karr = [5, 10, 20]
    blogs, colnames, data = clusters.readfile('Outputs/blogdata.txt')
    for i in karr:

        kclust, itercount = clusters.kcluster(data, k=i)
        print(kclust)
        f = open("Outputs/kclust_%d.txt" % i, 'w')
        f.write("Iteration count: %d \n" % itercount)
        print(len(kclust))
        for cluster in kclust:
            f.write("****************************\n")
            f.write("[")
            for blogid in cluster:
                f.write(blogs[blogid] + ", ")
            f.write("]\n")


def mds():
    blognames, words, data = clusters.readfile('Outputs/blogdata.txt')
    coords, itercount = clusters.scaledown(data)
    clusters.draw2d(coords, labels=blognames, jpeg='../docs/q4Mds.jpg')
    print ('Iteration count: %d' % itercount)

createDendrogram()
# write_blogs()
# create_blog_matrix()
# draw_acii_dendogram()
# draw_dendogram()
# text()