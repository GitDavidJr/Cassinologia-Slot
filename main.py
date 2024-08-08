from game import Game

new_game = Game(slots = [])

jogos = 1000

derrotas = 0
horizontais = 0
verticais = 0
diagonais = 0


for r in range(jogos):

    new_game.girar_roleta()
    new_game.desenhar()
    result = new_game.verificar()

    if not result:
        derrotas +=1
    elif result.startswith("horizontal"):
        horizontais+=1
    elif result.startswith("vertical"):
        verticais+=1
    elif result.startswith("diagonal"):
        diagonais+=1

print(f"Horizontais: {horizontais}")
print(f"Verticais: {verticais}")
print(f"Diagonais: {diagonais}")
print(f"Derrotais: {derrotas}")        