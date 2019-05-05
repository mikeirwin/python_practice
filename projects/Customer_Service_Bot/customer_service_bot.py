# name = input("What is your Name?")
# print(name)2


def cs_service_bot():
    welcome = "Hello! Welcome to the DNS Cable Company's Service Portal. Are you a new or existing customer?"
    print(welcome)
    choice = input("[1] New Customer \n"
                   "[2] Existing Customer")
    if choice == "1":
        new_customer()
    elif choice == "2":
        existing_customer()
    else:
        print("Sorry, we didn't understand your selection.")
        cs_service_bot()


def existing_customer():
    # Replace `pass` with your code
    print("What kind of support do you need?")
    choice = input("[1] Television Support \n"
                   "[2] Internet Support \n"
                   "[3] Live Representative")
    if choice == "1":
        television_support()
    elif choice == "2":
        internet_support()
    elif choice == "3":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        cs_service_bot()


def new_customer():
    # Replace `pass` with your code
    print("We're excited to have you join the DNS family, how can we help you?")
    choice = input("[1] Sign up for service. \n"
                   "[2] Schedule for a home visit. \n"
                   "[3] Speak to a sales representative.")
    if choice == "1":
        sign_up()
    elif choice == "2":
        home_visit()
    elif choice == "3":
        live_rep("sales")
    else:
        print("Sorry, we didn't understand your selection.")
        cs_service_bot()


def television_support():
    # Replace `pass` with your code
    print("What is the nature of your problem?")
    choice = input("[1] I can't access certain channels. \n"
                   "[2] My picture is blurry. \n"
                   "[3] I keep losing service. \n"
                   "[4] Other issues")
    if choice == "1":
        print("Please check the channel lists at DefinitelyNotSinister.com. \n"
              "If the channel you cannot access is there, please contact a live representative.")
        did_that_help()
    elif choice == "2":
        print("Try adjusting the antenna above your television set.")
        did_that_help()
    elif choice == "3":
        print("Is it raining outside? If so, wait until it is not raining and then try again.")
        did_that_help()
    elif choice == "4":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        television_support()


def internet_support():
    # Replace `pass` with your code
    print("What is the nature of your problem?")
    choice = input("[1] I can't connect to my internet. \n"
                   "[2] My connection is very slow. \n"
                   "[3] I can't access certain sites. \n"
                   "[4] Other issues")
    if choice == "1":
        print("Unplug your router, then plug it back in, then give it a good whack, like the Fonz.")
        did_that_help()
    elif choice == "2":
        print("Make sure that all cell phones and other peoples computers are not connected to the internet, \n"
              "so that you can have all the bandwidth.")
        did_that_help()
    elif choice == "3":
        print("Move to a different region or install a VPN. Some areas block certain sites.")
        did_that_help()
    elif choice == "4":
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        internet_support()


def did_that_help():
    # Replace `pass` with your code
    choice = input("Did this solve your problem? Y/N")
    if choice == "Y":
        print("Happy to be of service!")
    elif choice == "N":
        next_choice = input("Would you like to: \n"
                            "[1] talk to a representative \n"
                            "[2] schedule a home visit?")
        if next_choice == "1":
            live_rep("support")
        elif next_choice == "2":
            home_visit("support")
        else:
            print("Sorry, we didn't get that. Try again.")
            did_that_help()
    else:
        print("Sorry, we didn't get that. Try again")
        did_that_help()


def sign_up():
    # Replace `pass` with your code
    print("Great choice, friend! \n"
          "We're excited to have you join the DNS family! \n "
          "Please select the package you are interested in signing up for.")
    choice = input("[1] Bundle Deal (Internet + Cable) \n"
                   "[2] Internet \n"
                   "[3] Cable")
    if choice == "1":
        print("You've selected the Bundle Package! \n"
              "Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    elif choice == "2":
        print("You've selected the Internet Only Package! \n"
              "Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    elif choice == "3":
        print("You've selected the Cable Only Package! \n"
              "Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    else:
        print("Sorry, we didn't understand your selection. Try again.")
        sign_up()


def home_visit(purpose="none"):
    # Replace `pass` with your code
    if purpose == "none":
        print("What is the purpose of your visit?")
        choice = input("[1] New service installation. \n"
                       "[2] Existing service repair. \n"
                       "[3] Location scouting for unserviced region.")
        if choice == "1":
            home_visit("new install")
        if choice == "2":
            home_visit("support")
        if choice == "3":
            home_visit("scout")

        else:
            print("Sorry, we didn't understand your selection.")
            home_visit()
    if purpose == "new install":
        pst = "begin installation"
        visit_date = input("Please enter a date below in MM/DD/YY:")
        print("Wonderful! A technical will come visit you on {} and {}. \n"
              "Please be available between the hours of 1:00 am and 11:00 pm.".format(visit_date, pst))
    if purpose == "support":
        pst = "provide you with professional support"
        visit_date = input("Please enter a date below in MM/DD/YY:")
        print("Wonderful! A technical will come visit you on {} and {}. \n"
              "Please be available between the hours of 1:00 am and 11:00 pm.".format(visit_date, pst))
    if purpose == "scout":
        pst = "examine your area"
        visit_date = input("Please enter a date below in MM/DD/YY:")
        print("Wonderful! A technical will come visit you on {} and {}. \n"
              "Please be available between the hours of 1:00 am and 11:00 pm.".format(visit_date, pst))


def live_rep(purpose):
    # Replace `pass` with your code
    if purpose == "sales":
        print("Please hold while we connect you with a live sales representative. \n"
              "The wait time will be between two minutes and six hours. We thank you for your patience.")
    elif purpose == "support":
        print("Please hold while we connect you with a live support representative. \n"
              "The wait time will be between two minutes and six hours. We thank you for your patience.")


cs_service_bot()
""" END OF FILE"""

