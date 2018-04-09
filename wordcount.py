# put your code here.
#get lines to iterate over from file

import sys

FILE_NAME = sys.argv[1]


def get_words(file_name):
    """Splits each line in file by space and returns list of words"""

    words = {}
    c = Counter()

    with open(file_name) as read_file:
        one_line = read_file.read().lower().strip().replace("\n", " ").split(" ")
        for i in range(len(one_line)):
            word = one_line[i]
            for char in one_line[i]:
                if not char.isalnum():
                    one_line[i] = one_line[i].replace(char, "")

            print c[word]

    #     for line in read_file:
    #         split_words = line.lower().strip().split(" ")
    #         for item in split_words:
    #             for char in item:
    #                 if not char.isalnum():
    #                     item = item.replace(char, "")
    #             words[item] = words.get(item, 0) + 1

    # for word, count in words.iteritems():
    #     print "{} {}".format(word, count)

get_words(FILE_NAME)
