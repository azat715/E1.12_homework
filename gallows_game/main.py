from gallows_game.game import Game
import fire


def main():
    game = Game()
    print(f"Отгадайте слово: {game.get()}")
    print(game.word)
    while True:
        letter = input("Введите букву:")
        riddle = game.get(letter=letter)
        if game.finished:
            if game.status == "win":
                print("Поздравляю вы выиграли")
                print(f"Загаданное слово: {game.word}")
                break
            elif game.status == "lost":
                print("Вы проиграли, попробуйте еще")
                break
        print(f"Отгадайте слово {riddle}")


def cli():
    """игрa виселица"""
    fire.Fire(main)
