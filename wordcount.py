# put your code here.
#get lines to iterate over from file

import sys
import collections
from operator import itemgetter

FILE_NAME = sys.argv[1]


def get_words(file_name):
    """Splits each line in file by space and returns list of words"""

    c = collections.Counter()

    with open(file_name) as read_file:
        one_line = read_file.read().lower().strip().replace("\n", " ").split(" ")
        for i in range(len(one_line)):
            word = one_line[i]
            for char in one_line[i]:
                if not char.isalnum():
                    one_line[i] = one_line[i].replace(char, "")
            c[one_line[i]] += 1

    # print "c: ", c

    # for word, count in sorted_c.iteritems():
    #     print word, count

    # #sort output to show words alphabetically
    # sorted_c = sorted(c)

    # for word in sorted_c:
    #     print word, c[word]

    # sort output by word count
    sort_by_word = sorted(c.items(), key=itemgetter(1))
    for word, count in sort_by_word:
        print "{}: {}".format(word, count)

get_words(FILE_NAME)
