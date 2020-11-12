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

# try statment to check if game exists
try:
    # requesting the data from the api
    game = input("Enter a games title\n>")
    url = 'https://api.boardgameatlas.com/api/search?name=' + game +'&client_id=JLBr5npPhV'
    response = requests.get(url)
    data = response.json()
    # accessing the useful information from the json
    name = 'Name: ' + (data['games'][0]['name'])
    description = 'Description: ' + (data['games'][0]['description'])
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
    game_info = remove_html_markup(name), remove_html_markup(description), remove_html_markup(players), remove_html_markup(playing_time) 

    print(game_info[0])
    print(game_info[1])
    print(game_info[2])
    print(game_info[3])

# if no game was found
except:
    print('Sorry Game not found, check your spelling')