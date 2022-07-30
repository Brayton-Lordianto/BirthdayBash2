
from db_generic_util import *

# get user information for search later

# now working
# now we want writing and inserting and deleting and getting methods for badge
def get_badges(name):
    return get_items_where(get_condition('devpostScreenName', name))
    
def insert_badge(items, commit=True):
    if not type(items) is list: return
    upsert_many(items, commit=commit)
    
def cancel(badge_url):
    delete_where(get_condition('imageURL', badge_url))

def main():
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
    cancel('testurl')
    print(get_badges('testname'))
    

main()