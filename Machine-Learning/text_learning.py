### Text Learning

# bag of words

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
string1 = "hi Katie the self driving car will be late Best Sebastian"
string2 = "Hi Sebastian the machine learning class will be great great great Best Katie"
string3 = "Hi Katie the machime learning class will be most excellent"
email_list = [string1, string2, string3]
bag_of_words = vectorizer.fit(email_list)
bag_of_words = vectorizer.transform(email_list)
#print(bag_of_words)
# -> a tuple
# -> (1,7)  1 : means in document1 word no.7 accurs one time
# -> (1,6)  3: string2(index starts 0) great
print(vectorizer.vocabulary_.get('great'))
# -> 6 

# stopwords

from nltk.corpus import stopwords
sw = stopwords.words('english')
print(sw[0]) # -> i
for x in sw[:20]:
	print x 
# -> i me myself, we our, ours, ourself, you ...she her hers
print(len(sw))  # -> 153

# stemming

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
print(stemmer.stem('responsiveness')) # -> respons
print(stemmer.stem('unresponsive')) # -> unrespons
print(stemmer.stem('effective')) # -> effect

