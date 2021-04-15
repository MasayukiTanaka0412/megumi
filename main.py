import sys
from sklearn.feature_extraction.text import CountVectorizer
import csv
import pandas as pd

print('Started')
inputfile = sys.argv[1]
print('input file = {}'.format(inputfile))

idffile = sys.argv[2]
print('idf file = {}'.format(idffile))

outfile = sys.argv[3]
print('out file = {}'.format(outfile))

print('Loading idf file...')
idfdict = {}
with open(idffile, 'r',encoding="utf-8") as data: 
    for line in csv.DictReader(data):
        idfdict[line['token']] = line['idf'] 
print('Loaded')


print('Loading source file...')
txt_vec = CountVectorizer(input='filename',stop_words='english')
txt_vec.fit([inputfile])
word = txt_vec.transform([inputfile])
 
vector = word.toarray()
tokens = []
tfidfs = []
for word,count in zip(txt_vec.get_feature_names()[:], vector[0, :]):
    idf = 0.0000000000000000000000000000000001
    if word in idfdict:
        idf = idfdict[word]
    tfidf = count * idf
    #print("{},{},{}".format(word,count,tfidf))
    tokens.append(word)
    tfidfs.append(tfidf)

df = pd.DataFrame({'token': tokens,'tfidf': tfidfs})
df.sort_values('tfidf', ascending=False,inplace=True)
df.to_csv(outfile,encoding="utf-8",header=True,index=False)

print('end')