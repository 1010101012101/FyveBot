import requests
import credentials


class SummaryExternalClient:

    def pullSummaryForUrl(self, artUrl, title):
        url = "https://api.aylien.com/api/v1/summarize"
        headers = {"X-AYLIEN-TextAPI-Application-Key": credentials.AYLIEN_APP_KEY,
                   "X-AYLIEN-TextAPI-Application-ID" : credentials.AYLIEN_APP_ID}
        params = {"url" : artUrl,
                  "title" : title,
                  "sentences_number": 7}
        summary = requests.get(url=url, headers=headers, params=params)
        try:
            sentences = summary.json()['sentences']
        except:
            sentences = []
        return sentences

    def pullSummaryForText(self, text, title):
        url = "https://api.aylien.com/api/v1/summarize"
        headers = {"X-AYLIEN-TextAPI-Application-Key": credentials.AYLIEN_APP_KEY,
                   "X-AYLIEN-TextAPI-Application-ID" : credentials.AYLIEN_APP_ID}
        params = {"text": text,
                  "title": title,
                  "sentences_number": 7}
        summary = requests.get(url=url, headers=headers, params=params)
        try:
            sentences = summary.json()['sentences']
        except:
            sentences = []
        return sentences

