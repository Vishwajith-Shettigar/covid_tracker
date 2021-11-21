from plyer import notification
import requests
import json

def notifyme(title,message):
    message=str(message)
    notification.notify(
        title=title,
        
        
        message=message,
        app_icon='covid.ico',
        timeout=100
        
    )
    
def getreq(url):
    r=requests.get(url)
    return r.text
if __name__ == '__main__':
    
    data=getreq('https://disease.sh/v3/covid-19/all')
   
    soup=json.loads(data)
    
    
    for i in soup.items():
    
        notifyme(str(i[0]),i[1])
        
    
   