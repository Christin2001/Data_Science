from nltk import ngrams
print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")
sentence='I reside in Bengaluru'
n=3
unigrams=ngrams(sentence.split(),n)
for grams in unigrams:
    print(grams)