#import script_downloader
import nltk
import urllib3
from urllib3 import request

url = "http://www.chakoteya.net/doctorwho/31-1.htm"

if __name__ == "__main__":
    sentences = nltk.Text(
                    nltk.word_tokenize(
                    open('../resources/raw-scripts/34_1__Deep_Breath.txt',"r").read()))
    words = [w for w in sentences]
    print(set(words))
    fdist = nltk.FreqDist([word for word in words if word.isalpha()])
    print fdist.most_common(10)