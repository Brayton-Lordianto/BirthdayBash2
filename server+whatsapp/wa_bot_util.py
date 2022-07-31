from twilio.twiml.messaging_response import MessagingResponse
from db_v2 import *

def respond(message):
    response = MessagingResponse()
    print("hello", message, "world")
    response.message(message)
    # print((f"you sent a response : \n\nhi"))
    return str(response)

def deleteLastImage(url):
    if not url: return False
    
    # todo: add db functionality √√
    cancel(url)
    url = ''
    return True
    
def create_badge(img_url):
    return {'imageURL':img_url,'date':'July 31 2022','hackathon':'FreyHacks','hackathonLink':'https://freyhacks.devpost.com','issuedBy':'Hackathon Organizer','message':'Congrats!'}
    
def storeBadges(img_url, screenNames):
    if not img_url: return False
    
    # screenNames is a csv string
    # screenNameArr = screenNames.split(',')
    
    # screenNames is the array
    screenNameArr = screenNames
    
    # add into db for each 
    items = [create_badge(img_url)]
    insert_badge_info(items)
    
    items = [{'devpostScreenName':screenName, 'imageURL':img_url} for screenName in screenNameArr]    
    insert_badge(items=items)

def updateImageDetails(img_url, issued_by=None, description=None, date="July 30 2022", hackathon_link=""):
    # print('you called this')
    # print(1, img_url, 2, lastImageUrl, name, description, category)
    # print('method')
    if not img_url: return False
    update_badge(img_url,issued_by,description)
    pass
    
def main():
    # setting up stuff 
    
    drop_table('users')
    drop_table('badges')
    # all it needs to call is to create the tables if not exists
    create_table('users',['name','devpostScreenName'],[STR_TYPE,STR_TYPE])
    create_table('badges',['devpostScreenName','imageURL','date','hackathonLink','issuedBy','message'],[STR_TYPE,LINK_TYPE,STR_TYPE,LINK_TYPE,STR_TYPE,STR_TYPE])
    
    # if you want to do setting up, you can
    setHeaders(['devpostScreenName','imageURL','date','hackathonLink','issuedBy','message'])
    setHeaderTypes([STR_TYPE,LINK_TYPE,STR_TYPE,LINK_TYPE,STR_TYPE,STR_TYPE])
    setTable('badges')
    
    # tests
    storeBadges('somelink', 'u1,u2,u3,u4,u5')
    print(get_items())
    updateImageDetails('somelink',issued_by='heh')
    print(get_items())
    updateImageDetails('somelink',description='hehr')
    print(get_items())
    
# uncomment to test methods in this class
# main()

