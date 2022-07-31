# updated for new table


from tarfile import LNKTYPE
from db_generic_util import *

BADGE_INFO_FIELDS = ['imageURL','hackathon','date','hackathonLink','issuedBy','message']
BADGE_INFO_TYPE_FIELDS = [LINK_TYPE,STR_TYPE,STR_TYPE,LINK_TYPE,STR_TYPE,STR_TYPE]

# badges data
def insert_badge_info(items, commit=True):
    setHeaders(BADGE_INFO_FIELDS)
    setHeaderTypes(BADGE_INFO_TYPE_FIELDS)
    setTable('badge_info')

    if not type(items) is list: return
    upsert_many(items, commit=commit, table_name='badge_info')
    
def update_badge_info(img_url, issued_by=None, description=None, date="July 30 2022", hackathon_link=""):
    if issued_by: 
        field = 'issuedBy'
        val = issued_by
    elif description: 
        field = 'message'
        val = description
    else: print('this should not happen.')
    
    update_item_where(get_condition('imageURL',img_url),field,val,table_name='badge_info')

def get_badge_info():
    return get_items('badge_info',BADGE_INFO_FIELDS)

# get user information for search later -> same as get badges actually

# now working
# now we want writing and inserting and deleting and getting methods for badge
def get_badges(screenName):
    print(screenName)
    return get_items_where(get_condition('devpostScreenName', screenName),table_name='badges',fields=['devpostScreenName','imageURL'])
    
def insert_badge(items, commit=True):
    setHeaders(['devpostScreenName','imageURL'])
    setHeaderTypes([STR_TYPE,LINK_TYPE])
    setTable('badges')

    if not type(items) is list: return
    upsert_many(items, commit=commit, table_name='badges')
    
def cancel(badge_url):
    delete_where(get_condition('imageURL', badge_url),table_name='badges')
    delete_where(get_condition('imageURL', badge_url),table_name='badge_info')

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
    link1 = 'https://images.credly.com/images/c29c7aef-da17-43ca-8c35-2778df197480/Hack-credly-badges-600px-participant.png'
    link2 = 'https://images.credly.com/size/680x680/images/3260b53a-d24e-4afc-9957-58f9db70a4e3/MICROSOFT_HACKATHON.png'
    link3 = 'https://images.credly.com/images/4ae74655-a8ba-4721-a075-e3ebcddd4657/hackathon_CHAMPION.png'
    link4 = 'https://miro.medium.com/max/788/1*RGO7fo_6_x5e2wGYFzpzxA.png'
    insert_badge_info(items=[
                     {'imageURL':link1,'hackathon':'Microsoft Hacks','date':'30 July 2022','hackathonLink':'https://microsoft-did.devpost.com/','issuedBy':'Hackathon Organizer','message':'Congratulations!'},
                     {'imageURL':link2,'hackathon':'Microsoft Hacks','date':'30 July 2022','hackathonLink':'https://microsoft-did.devpost.com/','issuedBy':'Hackathon Organizer','message':'Congratulations!'},
                     {'imageURL':link3,'hackathon':'Microsoft Hacks','date':'30 July 2022','hackathonLink':'https://microsoft-did.devpost.com/','issuedBy':'Hackathon Organizer','message':'Congratulations!'},
                     {'imageURL':link4,'hackathon':'Microsoft Hacks','date':'30 July 2022','hackathonLink':'https://microsoft-did.devpost.com/','issuedBy':'Hackathon Organizer','message':'Congratulations!'},
                  ])
    insert_badge(items=[
        {'devpostScreenName':'bl3321','imageURL':link1},
        {'devpostScreenName':'bl3321','imageURL':link2},
        {'devpostScreenName':'bl3321','imageURL':link3},
        {'devpostScreenName':'bl3321','imageURL':link4}
    ])
    print(get_badges('bl3321'))

def main():
    drop_table('users')
    drop_table('badges')
    drop_table('badge_info')
    
    # all it needs to call is to create the tables if not exists
    create_table('users',['name','devpostScreenName'],[STR_TYPE,STR_TYPE])
    create_table('badges',['devpostScreenName','imageURL'],[STR_TYPE,LINK_TYPE])
    create_table('badge_info',BADGE_INFO_FIELDS,BADGE_INFO_TYPE_FIELDS)
    
    # if you want to do setting up, you can
    setHeaders(['devpostScreenName','imageURL'])
    setHeaderTypes([STR_TYPE,LINK_TYPE])
    setTable('badges')
    
    # comment out for tests
    # return
    insert_badge_info(items=[{'imageURL':'testurl','hackathon':'some','date':'testdate','hackathonLink':'testlink','issuedBy':'testissue','message':'testmessage'}])
    insert_badge_info(items=[{'imageURL':'testurl2','hackathon':'somer','date':'testdate','hackathonLink':'testlink','issuedBy':'testissue','message':'testmessage'}])
    print(get_badge_info())
    insert_badge(items=[{'devpostScreenName':'bl3321','imageURL':'testurl'}])
    print(get_badges('bl3321'))
    update_badge_info('testurl','someissues')
    print(get_badge_info())
    update_badge_info('testurl',description='somedesc')
    print(get_badge_info())
    cancel('testurl')
    print(get_badges('bl3321'))
    cancel('testurl2')
    

# main()
# initBadges()
# print(get_badge_info())
# print(get_badges('bl3321'))