from urllib.request import urlopen

def read_files():
    contents = open("C:\\Users\\HP\\Desktop\\cursewords\\movie_quotes1.txt")
    quotes = contents.read()
    print(quotes)
#read_files()


def check_badwords(word_tocheck):
    #connection = urlopen("http://www.wdylike.appspot.com/?a=", + word_tocheck)
    connection = urlopen("http://www.wdylike.appspot.com/?q=shit")
    output = connection.read()
    print(output)
check_badwords("abc")

#read_files()
