import urllib

def check_contents():

    quotes = open("/Users/hgi/PycharmProjects/Python_course/movie_quotes.txt")

    contents_of_file = quotes.read()

    print("This is my notes" +contents_of_file)

    quotes.close()

    check_profanity(contents_of_file)


def check_profanity(text_to_check):

    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q='+text_to_check)

    output = connection.read()

    print("")
    print("-----Checking for profanity-----")

    if "true" in output:

        print("Profanity exists!! Please correct your statements asap!!")

    elif "false" in output:

        print("No profanity!! You are safe!! text is good to go!")

    else:

        print("Could not scan the document!!!!")

    connection.close()

check_contents()