
print("University No: SJC22MCA-2021 \nName: Christin Benny \nBatch: S3 MCA \n______________________________________\n")
def gen_ngrams(text,WordsToCombine):
    words=text.split()
    output=[]
    for i in range(len(words)-WordsToCombine+1):
        output.append(words[i:i+WordsToCombine])
    return output

x=gen_ngrams(
    text='The data set given satisfies the requirement for model generation., This is used in Data Science Lab',
    WordsToCombine=3
)
print(x)