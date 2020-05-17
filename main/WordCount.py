#Finding top 5 used words from Sample.txt and it's count. Print bar chart for top 5 most popular words.

from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

with open(r'Sample.txt') as f:
    lines = f.read()

file_tokenizer = RegexpTokenizer(r'\w+')
tokens = file_tokenizer.tokenize(lines)

total_words = len(tokens)
type1 = type(tokens)
print("Total number of words in the file : {0}".format(total_words))

#finding top 5 words from text file
main_list = FreqDist(tokens)
top_five = main_list.most_common(5)


#printing word and wordcount
count = 0
for i in top_five:
    count += 1
    print("Number {0} word and total wordcount is {1}".format(count,i))


# code to split it into 2 lists for chart purpose
wlist = [i[0] for i in top_five]
clist = [i[1] for i in top_five]

#For bar chart
y_pos = np.arange(len(wlist))
plt.bar(y_pos, clist, align='center', alpha=0.5)
plt.xticks(y_pos, wlist)
plt.ylabel('Total words in text')
plt.title('Word')

plt.show()