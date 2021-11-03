import requests

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
#uncomment this to see the returned json
#    print(data) 

# accessing the useful information from the json
name = 'Name: ' + (data['games'][0]['name'])
description = 'Description: ' + (data['games'][0]['description'])

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
game_info = remove_html_markup(name), remove_html_markup(description), remove_html_markup(players), remove_html_markup(playing_time), remove_html_markup(coop)

print(game_info[0])
print(game_info[1])
print(game_info[2])
print(game_info[3])
print(game_info[4])
# if no game was found
#except:
#    print('Sorry Game not found, check your spelling')

# this next section is testing for the db 
'''
 ("INSERT INTO mygames (name, min_players, max_players, min_time, max_time, cooperative")
 '''