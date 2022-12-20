"""program to keep track of cgames collection ,
query api for game data, and save it to a database"""

import requests
import json
import db


# function to remove any html tags left over from the json
def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif (c == '"' or c == "'") and tag:
            quote = not quote
        elif not tag:
            out = out + c
    return out

def api_request():
    print('api request')
    # try statment to check if game exists
    try:
        # requesting the data from the api
        game = input("Enter a games title\n>")
        url = 'https://api.boardgameatlas.com/api/search?name=' + game +'&client_id=eC1Q7Wqrxk'
        response = requests.get(url)
        data = response.json()
        datajson = json.dumps(data, indent=4)
        print(type(data))
        print(type(datajson))

        cleaned = remove_html_markup(datajson)
        data = json.loads(cleaned)

        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

        name = data['games'][0]['name']
        description = data['games'][0]['description']
        min_age = int(data['games'][0]['min_age'])
        mechanics_json = (data['games'][0]['mechanics']) # extracting the data 
        mechanics = [d['id'] for d in mechanics_json] # putting it in a list
        categories_json = (data['games'][0]['categories'])
        categories = [d['id'] for d in categories_json]
        min_players = (str(data['games'][0]['min_players']))
        max_players = (str(data['games'][0]['max_players']))
        min_playtime = (str(data['games'][0]['min_playtime']))
        max_playtime = (str(data['games'][0]['max_playtime']))
        primary_designer = (data['games'][0]['primary_designer']['name'])
        primary_publisher = (data['games'][0]['primary_publisher']['name'])

        game_info = [name,
                    description, 
                    min_age, 
                    mechanics,
                    categories, 
                    min_players,
                    max_players, 
                    min_playtime, 
                    max_playtime,
                    primary_designer, 
                    primary_publisher]

    except Exception as e:
        print(e)
        print('Sorry Game not found, check your spelling')
    return game_info

# function to find out if game is cooperative
#def iscoop(mechanics):

# main loop

choice = int(input("1. Add a game, 2. Get a game, 3. Exit\n>"))   

while choice == 1:   
    print("choice 1")
    game_info = api_request()
    print(type(game_info))
    db.save_game(game_info)

    choice = int(input("1. Add a game, 2. Get a game, 3. Exit\n>"))

if choice == 2:
    coop_query = db.get_game( True )
    print(f"Co-op games: {coop_query}")

# try statment to check if game exists
    # try:
    #     # requesting the data from the api
    #     game = input("Enter a games title\n>")
    #     url = 'https://api.boardgameatlas.com/api/search?name=' + game +'&client_id=eC1Q7Wqrxk'
    #     response = requests.get(url)
    #     data = response.json()
    #     datajson = json.dumps(data, indent=4)
    #     print(type(data))
    #     print(type(datajson))

    #     cleaned = remove_html_markup(datajson)
    #     data = json.loads(cleaned)

    #     with open('data.json', 'w') as f:
    #         json.dump(data, f, indent=4)

        #uncomment this to see the returned json
        # print(data) 

        # accessing the useful information from the json
        # d_name = f"Name: {data['games'][0]['name']}"
        # d_description = f"Description: {data['games'][0]['description']}"
        # mechanics_json = (data['games'][0]['mechanics']) # extracting hte data 
        # mechanics = [d['id'] for d in mechanics_json] # putting it in a list
        # #description = f"Description {(data['games'][0]['description'])}"
        # d_min_age = f"min age: {data['games'][0]['min_age']}"
        # d_categories = f"categories: {(data['games'][0]['categories'])}"
        # d_primary_designer = f"designer: {(data['games'][0]['primary_designer']['name'])}"
        # d_primary_publisher = f"publisher:  {(data['games'][0]['primary_publisher']['name'])}"
        # #description = 'Description: ' + (datajson['games'][0]['description'])

        # # section to figure out if the fgame is co-op or competitive
        # d_mechanics_json = (data['games'][0]['mechanics']) # extracting hte data 
        # d_mechanics = [d['id'] for d in d_mechanics_json] # putting it in a list

        # for s in d_mechanics: # loop through the list and see if it matches the mechanics id
        #     if '9mNukNBxfZ' in s:
        #         print(s)
        #         cooperative = True
                
        #     elif 'Khp7U5pHZi' in s:
        #         print(s)
        #         cooperative = False
                
        #     else:
        #         print(s)
        #         cooperative = 'No data available'

        # d_coop = 'Co-op: ' + cooperative
        # coop = cooperative


                
            
        #casting to a string to go into our function 
        #(not sure this is nessessary as the returned data should be only ints?)
        # min_players = (str(data['games'][0]['min_players']))
        # max_players = (str(data['games'][0]['max_players']))

        #tydying up the resuly so its a bit easier to read 
        # if min_players == max_players:
        #     players = min_players + ' players'
        # else:
        #     players = min_players + ' - ' + max_players + ' players' 

        # min_playtime = (str(data['games'][0]['min_playtime']))
        # max_playtime = (str(data['games'][0]['max_playtime']))

        # if min_playtime == max_playtime:
        #     playing_time = min_playtime + ' minutes'
        # else:
        #     playing_time = 'Playing time: ' + min_playtime  + '-' + max_playtime + ' minutes'

        #puttting all of our usefull info into a list to be printed out
        #print(description)
        #game_info = remove_html_markup(name), remove_html_markup(description), remove_html_markup(players), remove_html_markup(playing_time), remove_html_markup(coop)
        # game_info = [name,
        #             description, 
        #             min_players,
        #             max_players, 
        #             playing_time, 
        #             cooperative, 
        #             min_age, 
        #             primary_designer, 
        #             primary_publisher]

        # for i in game_info:
        #     print(i)

    # if no game was found
    # except Exception as e:
    #     print(e)
    #     print('Sorry Game not found, check your spelling')

    # this next section is testing for the db 
