import pytest
from gallows_game.game import Game


def test_init_game():
    game = Game()
    assert game.word in Game.WORDS
    assert game.error == 0
    assert not game.finished
    assert game.status == "started"


@pytest.fixture(name="test")
def fixture_test():
    game = Game()
    game.word = "test"
    game.riddle = game._generate_riddle("test")
    return game


def test_win(test):
    assert test.get() == "_ _ _ _"
    assert test.get(letter="t") == "t _ _ t"
    assert test.get(letter="e") == "t e _ t"
    assert test.get(letter="s") == test.word
    assert test.finished is True
    assert test.status == "win"


def test_err_game(test):
    assert test.get(letter="w") == "_ _ _ _"
    assert test.error == 1
    assert test.get(letter="w") == "_ _ _ _"
    assert test.error == 2
    assert test.get(letter="w") == "_ _ _ _"
    assert test.error == 3
    assert test.get(letter="w") == "_ _ _ _"
    assert test.error == 4
    assert test.finished is True
    assert test.status == "lost"
    assert test.get(letter="w") is None
