from flask import request, Flask
from wa_bot_util import *
#
route = 0

last_image_url = None

hackathon = "FreyHacks"

HELP_STRING = '''
this is a help message.
Send the image of a badge or certificate you wish to give your participants!


you are an organizer for the hackathon: *FreyHacks*
type 'quit' to change your organizer account. 
'''

CANCEL_STRING = '''
type 'cancel' to remove the last badge you created.
If badges were given out to hackers, the badges will be deleted.
'''

def whatsapp_img_bot():
    global route
    global last_image_url
    last_image_url = last_image_url
    # get the message
    sender_phone_number = request.form.get('From')
    message_body = request.form.get('Body')
    img_url = request.form.get('MediaUrl0') 

    # if the user asks to help or cancel
    if 'help' in message_body or 'image' in message_body:
        route = 0
        response = str(f'{HELP_STRING}')
        print(response)
        return respond(str(response))
    if 'cancel' in message_body or 'delete' in message_body:
        response = f"you asked to cancel or delete the previously added image.\n"
        route = 0
        deleted = deleteLastImage(last_image_url)
        if not deleted: 
            response = 'there is no previous image to delete.\n'
        return respond(response)
    
    # if the user sends an image
    if img_url:
        # we now need the csv data from the user on who to give the image to. no need to store any data yet
        # then an optional description
        route = 1
        last_image_url = img_url
        # print(getLastImage(sender_phone_number), 1)
        # print(f"\nnAdd\n a name if you want to!")
        # return respond(f"We got your image! Who do you want to give this to? Add a *CSV* list of all *Devpost Screen Names*. This is required. \n{CANCEL_STRING}")
        return respond(f"We got your image! What prize is this for? \n Type the prize (ex. 'First Overall') \n{CANCEL_STRING}")

    # give badges to all users
    if route == 1:
        route = 2
        # updateImageDetails(users=message_body)
        part = '''
            All done! We found the prize and the badge have been given to all listed users!
            Here are the users who received it:
        '''
        
        # get users + add to their account
        # do beautiful soup parse here
        users = ['bl3321', 'mk101', 'raghavnautiyal26', 'melioraho9']
        print(1, last_image_url)
        storeBadges(last_image_url, users)
        usersString = '\n'.join(users)
        
        other_str = "\nThe badge is currently issued by the title 'Hackathon Organizer'. Change the badge's set recepient optionally by typing your title/name."
        
        response = '\n'.join([part,usersString,other_str,CANCEL_STRING])
        
        return respond(response)
        

    # add the issued_by
    if route == 2:
        route = 3
        # updateImageDetails(last_image_url,issued_by=message_body)
        response = f"Hackers can see that {message_body} sent the badge. Add a description or personalized message to the recepients if you'd like."
        return respond(response)
    
    # add the image description
    if route == 3:
        route = 1
        # updateImageDetails(last_image_url,description=message_body)
        return respond("The badge's description has been saved as:\n '{message_body}'. \nType 'help' to learn how to send another message.")
    
    # default response
    return respond("Sorry. please try again.")