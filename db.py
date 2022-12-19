import sqlite3

def save_game(game_to_save):
    print("saving game")
    name = game_to_save[0]
    description = game_to_save[1]
    players = game_to_save[2]
    playing_time = game_to_save[3]
    cooperative = game_to_save[4]
    min_age = game_to_save[5]
    categories = game_to_save[6]
    primary_designer = game_to_save[7]
    primary_publisher = game_to_save[8]

    print(game_to_save[0])
    print(game_to_save[1])
    con = sqlite3.connect('games.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS mygames (name TEXT, description TEXT, players INT, playing_time INT, cooperative TEXT,min_age INT)""")
    cur.execute("""INSERT INTO mygames VALUES (?,?,?,?,?,?) , name, description, players, playing_time, cooperative, min_age""")
    cur.execute("""SELECT * FROM mygames""")
    print(cur.fetchall())
    con.close()

