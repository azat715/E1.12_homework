from random import choice
from typing import List


class Game:
    WORDS = ["skillfactory", "testing", "blackbox", "pytest", "unittest", "coverage"]

    def __init__(self):
        self.word = None
        self.riddle = None
        self.error = 1
        self.finished = False
        self.status = None
        self.start()

    def _generate_riddle(self, word):
        res = []
        for _ in word:
            res.append("_")
        return res

    def _check(self, word: str, riddle: List[str], letter: str):
        if letter not in word:
            self.error += 1
            return riddle
        res = []
        length = len(word)
        index = 0
        while index < length:
            i = word.find(letter, index)
            if i == -1:
                break
            res.append(i)
            print(res)
            index = i + 1
        for i in res:
            riddle[i] = letter
        return riddle

    def get(self, letter):
        """
        return возвращает загадку формата ( _ _ _ _ _ _ _)"""
        if self.finished:
            return None
        if self.error == 4:
            self.finished = True
            self.status = "lost"
            return None
        self._check(self.word, self.riddle, letter)
        if "".join(self.riddle) == self.word:
            self.finished = True
            self.status = "win"
            return None
        return " ".join(self.riddle)

    def start(self):
        self.word = choice(Game.WORDS)
        self.riddle = self._generate_riddle(self.word)
