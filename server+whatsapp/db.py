
from db_generic_util import *

# badges data


# get user information for search later -> same as get badges actually

# now working
# now we want writing and inserting and deleting and getting methods for badge
def get_badges(screenName):
    return get_items_where(get_condition('devpostScreenName', screenName),table_name='badges')
    
def insert_badge(items, commit=True):
    setHeaders(['devpostScreenName','imageURL','date','hackathonLink','issuedBy','message'])
    setHeaderTypes([STR_TYPE,LINK_TYPE,STR_TYPE,LINK_TYPE,STR_TYPE,STR_TYPE])
    setTable('badges')

    if not type(items) is list: return
    upsert_many(items, commit=commit, table_name='badges')
    
def cancel(badge_url):
    delete_where(get_condition('imageURL', badge_url))

# this would be in the badgeinfo table instead if I do that
def update_badge(img_url, issued_by=None, description=None, date="July 30 2022", hackathon_link=""):
    if issued_by: 
        field = 'issuedBy'
        val = issued_by
    elif description: 
        field = 'message'
        val = description
    else: print('this should not happen.')
    
    update_item_where(get_condition('imageURL',img_url),field,val)
    
def initBadges():
    insert_badge(items=[
                     {'devpostScreenName':'bl3321','imageURL':'Badge1','date':'30 July 2022','hackathonLink':'https://microsoft-did.devpost.com/','issuedBy':'Hackathon Organizer','message':'Congratulations!'},
                     {'devpostScreenName':'bl3321','imageURL':'Badge2','date':'30 July 2022','hackathonLink':'https://microsoft-did.devpost.com/','issuedBy':'Hackathon Organizer','message':'Congratulations!'},
                     {'devpostScreenName':'bl3321','imageURL':'Badge3','date':'30 July 2022','hackathonLink':'https://microsoft-did.devpost.com/','issuedBy':'Hackathon Organizer','message':'Congratulations!'},
                     {'devpostScreenName':'bl3321','imageURL':'Badge4','date':'30 July 2022','hackathonLink':'https://microsoft-did.devpost.com/','issuedBy':'Hackathon Organizer','message':'Congratulations!'},
                  ])
    print(get_badges('bl3321'))

def main():
    drop_table('users')
    drop_table('badges')
    # all it needs to call is to create the tables if not exists
    create_table('users',['name','devpostScreenName'],[STR_TYPE,STR_TYPE])
    create_table('badges',['devpostScreenName','imageURL','date','hackathonLink','issuedBy','message'],[STR_TYPE,LINK_TYPE,STR_TYPE,LINK_TYPE,STR_TYPE,STR_TYPE])
    
    # if you want to do setting up, you can
    setHeaders(['devpostScreenName','imageURL','date','hackathonLink','issuedBy','message'])
    setHeaderTypes([STR_TYPE,LINK_TYPE,STR_TYPE,LINK_TYPE,STR_TYPE,STR_TYPE])
    setTable('badges')
    
    # comment out for tests
    # pass
    insert_badge(items=[{'devpostScreenName':'testname','imageURL':'testurl','date':'testdate','hackathonLink':'testlink','issuedBy':'testissue','message':'testmessage'}])
    print(get_badges('testname'))
    update_badge('testurl','someissues')
    print(get_badges('testname'))
    update_badge('testurl',description='somedesc')
    print(get_badges('testname'))
    cancel('testurl')
    print(get_badges('bl3321'))
    

# main()
initBadges()