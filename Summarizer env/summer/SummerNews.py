from newspaper import Article
from transformers import pipeline


def extract_text(url):
    my_article=Article(url,language="en")
    my_article.download()
    my_article.parse()
    return {
        "title":my_article.title,
        "text":my_article.text,
        "summary":summarizeURL(my_article.text)
    }

def summarizeURL(content):
    summarizer=pipeline("summarization")
    out=summarizer(content,max_length=130,min_length=30,do_sample=False)
    return out[0]['summary_text']
