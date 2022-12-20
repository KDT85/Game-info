import sqlite3

def save_game(game_to_save):
    name = game_to_save[0]
    description = game_to_save[1]
    min_age = game_to_save[2]
    mechanic = game_to_save[3]
    categories = game_to_save[4]
    min_players = game_to_save[5]
    max_players = game_to_save[6]
    min_playtime = game_to_save[7]
    max_playtime = game_to_save[8]
    primary_designer = game_to_save[9]
    primary_publisher = game_to_save[10]

    print("saving game")

    con = sqlite3.connect('games.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS mygames ( name TEXT, description TEXT, min_age INTEGER, mechanic TEXT, categories TEXT, min_players INTEGER, max_players INTEGER, min_playtime INTEGER, max_playtime INTEGER, primary_designer TEXT, primary_publisher TEXT)""")
    cur.execute("""INSERT INTO mygames VALUES (?,?,?,?,?,?,?,?,?,?,?)""" , (name, description, min_age, mechanic, categories, min_players, max_players, min_playtime, max_playtime, primary_designer, primary_publisher))
    cur.execute("""SELECT * FROM mygames""")
    print(cur.fetchall())
    con.commit()
    con.close()

def get_game(coop):
    con = sqlite3.connect('games.db')
    cur = con.cursor()
    cur.execute("""SELECT * FROM mygames WHERE cooperative = ?""", (coop,))
    game = cur.fetchone()
    con.close()
    return game
