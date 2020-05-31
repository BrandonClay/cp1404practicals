import wikipedia

user_search = input("What would you like to search: \n>>> ")

while user_search != "":
    try:
        #user_search_title = wikipedia.page("".format(user_search), pageid=1, auto_suggest = True)
       # print(user_search_title.title)

        print(wikipedia.summary("{}".format(user_search)))
        user_search = input("What would you like to search: \n>>> ")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)