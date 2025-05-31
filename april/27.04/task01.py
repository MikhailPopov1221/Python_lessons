bsk ={
    
}

pl = {
    "name": "Макс",
    "fname": "Максимов",
    "height": 198
}

def create_player():
    name = input("Введите имя игрока: ")
    fname = input("Введите фамилию игрока: ")
    height = int(input("Введите рост игрока: "))
    return {"name": name, "fname": fname, "height": height}

def add_player(player: dict):
    id = tuple(player.values())
    bsk[id] = player

def del_player(player: dict):
    id = tuple(player.values())
    del bsk[id]
    print(f"{player["name"]} {player["fname"]} успено удален из списка")

def find_player(text: str):
    for player in bsk.values():
        if text in player.values():
            print(player)

def change_player(old_player: dict, new_player: dict):
    pass



# print(bsk)
# pl_1 = create_player()
# add_player(pl_1)
# print(bsk)
# add_player(create_player())
# print(bsk)

add_player(pl)
print(bsk)
find_player("Макс")
