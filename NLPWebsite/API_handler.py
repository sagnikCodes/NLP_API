import paralleldots

class APIHandler(object):

    def __init__(self):
        self.API_key="eoT0faYru3VR3svRleSVpac37PlgfdVF71h4xbtAlYE"

    def sentiment_analysis(self,text):
        paralleldots.set_api_key(self.API_key)
        text=text
        lang_code="en"
        response=paralleldots.sentiment(text,lang_code)
        sentiment=sorted(response['sentiment'].items(),key=lambda x : x[1],reverse=True)[0][0]
        return sentiment.capitalize()
    
    def named_entity_recognition(self,text):
        paralleldots.set_api_key(self.API_key)
        text=text
        lang_code="en"
        response=paralleldots.ner(text,lang_code)
        answer=[]
        for names in response['entities']:
            answer.append(names['category'].capitalize()+" : "+names['name'])
        return answer
    
    def abuse_detection(self,text):
        paralleldots.set_api_key(self.API_key)
        text=text
        response=paralleldots.abuse(text)
        is_abusive=sorted(response.items(),key=lambda x : x[1],reverse=True)[0][0]
        return is_abusive.capitalize()