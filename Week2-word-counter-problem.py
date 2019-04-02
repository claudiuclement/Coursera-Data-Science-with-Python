#Word counter problem - Week 2 
#This code is much simpler than the code provided by the course tutor
#Code used below
from collections import Counter

#opens the file. the with statement here will automatically close it afterwards.
with open("/Users/Claudiu/Downloads/word_cloud/98-0.txt") as input_file:
    #build a counter from each word in the file
    count = Counter(word for line in input_file
                         for word in line.split())

print(count.most_common(10))
