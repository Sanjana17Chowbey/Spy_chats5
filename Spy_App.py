from Spy_detail import spy

#Time to code
#Starting the spychat application
#Welcome Spy to our app
STATUS_MESSAGES = ['Don ko pakadna mushkil nahi namumkin hai!', 'Na Investor ki fatkar se, na competitor ki lalkar se, Developer toh darta hai bus Customer ki Dissatisfaction se!!', 'Kahin pe pahunchne k liye kahin se nikalna bahut zaroori hota hai!']
friends= []
print "Importing done...Lets Start!"
#Asking to continue as default user
counter = 0
while True:
    if counter>2:
        print "Too many attempts"
        sys.exit()
        #This exits the program, you also need to have sys imported for it to work
        question= "Do you wish to continue as"+ spy_salutation+ " "+ spy_name+ "(Y/ N)?"
        existing= raw_input(question)
        if existing.lower()=="y":
            default_password="Doremon"
            password=raw_input("Please enter your password")
            if password == default_password:
        	    start_to_chat(spy_name,spy_salutation,spy_rating)
            break


        else:
            print "Login failed! Re-enter the credentials"
            counter+=1
    else:
            # Add the new spy
        break
            # passw.append(password)



def add_your_status(recent_status_message):
    updated_status_message = None

    if recent_status_message != None:
        print 'Your status message is %s \n' % (recent_status_message)
    else:
        print 'You have not updated any status currently \n'

    default = raw_input("Do you wish to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = input("Have you thought something creative to set? ")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
        elif default.upper()=='Y':

            item_position = 1

            for message in STATUS_MESSAGES:
                print '%d. %s' % (item_position, message)
                item_position = item_position + 1

            message_selection = int(raw_input("\nChoose from the above messages "))

            if len(STATUS_MESSAGES) >= message_selection:
                updated_status_message = STATUS_MESSAGES[message_selection - 1]

        else:
            print 'The option you chose is not valid! Press either y or n.'

        if updated_status_message:
            print 'Your updated status message is: %s' % (updated_status_message)
        else:
            print 'You did not update your status message'

        return updated_status_message
        def add_friend():
            new_friend = {
                'name': '',
                'salutation': '',
                'age': 0,
                'rating': 0.0
            }
            new_friend['name'] = input("Please add your friend's name: ")
            new_friend['salutation'] = input("Are they Mr. or Ms.?: ")

            new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

            new_friend['age'] = input("What is their Age?")

            new_friend['rating'] = input("What is their Spy rating?")

            if len(new_friend['name']) > 0 and new_friend['age'] > 17 and new_friend['rating'] >= spy['rating']:
                friends.append(new_friend)
                print 'Friend Added!'
            else:
                print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

        return len(friends)

        def start_to_chat(spy):
            current_status = None


            spy['name'] = spy['salutation'] + " " + spy['name']

            if spy['age'] > 17 and spy['age'] < 50:
                print "Authentication complete. Hello " + spy['name'] + " age: " + str(
                    spy['age']) + " and rating of: " + str(spy['rating']) + " Glad to have You!"

                display_menu=True
                while display_menu:
                    menu_choices = "What do you wish to do? \n 1. Add a status update \n 2. Add a friend spy \n  3.Choose a friend \n 4. Send a Secret Message \n 5.Read the Secret Message \n 6. Read Older chats \n 7.Close my Application \n"
                    menu_choice = raw_input(menu_choices)
                if len(menu_choice) > 0:
                    menu_choice = int(menu_choice)

                    if menu_choice == 1:
                        current_status = add_your_status(recent_status_message)
                    elif menu_choice == 2:
                        number_of_friends = add_friend()
                        print 'You have %d friends' % (number_of_friends)


                    else:
                        display_menu = False
                else:
                    print 'Sorry you are not of the correct age to be a spy!'
                    if existing == "Y":
                        start_to_chat(spy)
                    else:

                        spy = {
                            'name': '',
                            'salutation': '',
                            'age': 0,
                            'rating': 0.0,
                            'is_online': False
                        }

        spy['name'] = raw_input("welcome to spy chat,tell me your spy name first:")
        if len(spy['name']) > 0:
            spy['salutation']= input("Should I call you Mr. or Ms.?: ")

            spy['age']= input("What is your age?")

            spy['rating'] = input("What is your spy rating?")

            spy['is_online'] = True

            start_to_chat(spy)
        else:
            print 'You don\'t have a valid spy name'