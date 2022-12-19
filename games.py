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

# function to find out if game is cooperative
#def iscoop(mechanics):
    

    

# my game list
mygames = []

# try statment to check if game exists
##try:
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

#uncomment this to see the returned json
# print(data) 

# accessing the useful information from the json
name = f"Name: {data['games'][0]['name']}"
description = f"Description: {data['games'][0]['description']}"
#description = f"Description {(data['games'][0]['description'])}"
min_age = f"min age: {data['games'][0]['min_age']}"
categories = f"categories: {(data['games'][0]['categories'])}"
primary_designer = f"designer: {(data['games'][0]['primary_designer']['name'])}"
primary_publisher = f"publisher:  {(data['games'][0]['primary_publisher']['name'])}"
#description = 'Description: ' + (datajson['games'][0]['description'])

# section to figure out if the fgame is co-op or competitive
mechanics_json = (data['games'][0]['mechanics']) # extracting hte data 
mechanics = [d['id'] for d in mechanics_json] # putting it in a list

for s in mechanics: # loop through the list and see if it matches the mechanics id
    if '9mNukNBxfZ' in s:
        print(s)
        cooperative = 'Co-operative Play'
        break
    elif 'Khp7U5pHZi' in s:
        print(s)
        cooperative = 'Competitive Play'
        break
    else:
        print(s)
        cooperative = 'No data available'

coop = 'Co-op: ' + cooperative


        
    
#casting to a string to go into our function (not sure this is nessessary as the returned data should be only ints?)
min_players = (str(data['games'][0]['min_players']))
max_players = (str(data['games'][0]['max_players']))

#tydying up the resuly so its a bit easier to read 
if min_players == max_players:
    players = min_players + ' players'
else:
    players = min_players + ' - ' + max_players + ' players' 

min_playtime = (str(data['games'][0]['min_playtime']))
max_playtime = (str(data['games'][0]['max_playtime']))

if min_playtime == max_playtime:
    playing_time = min_playtime + ' minutes'
else:
    playing_time = 'Playing time: ' + min_playtime  + '-' + max_playtime + ' minutes'

#puttting all of our usefull info into a list to be printed out
#print(description)
#game_info = remove_html_markup(name), remove_html_markup(description), remove_html_markup(players), remove_html_markup(playing_time), remove_html_markup(coop)
game_info = [name,
            description, 
            players, 
            playing_time, 
            coop, 
            min_age, 
            categories, 
            primary_designer, 
            primary_publisher]

for i in game_info:
    print(i)
# if no game was found
#except:
#    print('Sorry Game not found, check your spelling')

# this next section is testing for the db 
db.save_game(game_info)


