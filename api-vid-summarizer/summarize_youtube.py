import youtube_transcript_api
from youtube_transcript_api import YouTubeTranscriptApi
import nltk
import re
from nltk.corpus import stopwords
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk.tokenize import sent_tokenize
import transformers
from transformers import BartTokenizer, BartForConditionalGeneration
from transformers import pipeline
def summarize_youtube_model(youtubeLink):
    nltk.download('punkt')
    link = youtubeLink
    unique_id = link.split("=")[-1]
    sub = YouTubeTranscriptApi.get_transcript(unique_id)  
    subtitle = " ".join([x['text'] for x in sub])
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    input_tensor = tokenizer.encode( subtitle, return_tensors="pt", max_length=512)
   # print(tokenizer.decode(outputs_tensor[0]))
    print(len(subtitle))
    summarizer = pipeline('summarization')
    n = 1000
    splitSummary = []
    i = 0
    for i in range(0, int(len(subtitle)+1), 1000):
        print(i)
        if i+1000 > len(subtitle):
            split = subtitle[i : ]
            summary = summarizer(split, max_length = 180, min_length =  30)
            splitSummary.append(summary)
        else:
            split = subtitle[i : i+1000]
            summary = summarizer(split, max_length = 180, min_length =  30)
            splitSummary.append(summary)
    print(splitSummary)
    summaryText = ""
    for i in range(len(splitSummary)):
        summaryText = summaryText + splitSummary[i][0]['summary_text']
    print(summaryText)
    print("Summarizing Text:")
    print("Before Summarization Length:" + str(len(subtitle)))
    print("After Summariztion Length:" + str(len(summaryText)))
    return summaryText