from random import choice
from typing import List, Optional


class Game:
    WORDS: List[str] = [
        "skillfactory",
        "testing",
        "blackbox",
        "pytest",
        "unittest",
        "coverage",
    ]

    def __init__(self):
        self.word: str = choice(Game.WORDS)
        self.riddle: List[str] = self._generate_riddle(self.word)
        self.error: int = 0
        self.finished: bool = False
        self.status: str = "started"

    def _generate_riddle(self, word: str) -> List[str]:
        res: List[str] = []
        for _ in word:
            res.append("_")
        return res

    def _check(self, word: str, riddle: List[str], letter: str) -> Optional[List[str]]:
        if letter not in word:
            self.error += 1
            if self.error == 4:
                self.finished = True
                self.status = "lost"
                return None
            return riddle
        res: List[int] = []
        length: int = len(word)
        index: int = 0
        while index < length:
            i = word.find(letter, index)
            if i == -1:
                break
            res.append(i)
            index = i + 1
        for i in res:
            riddle[i] = letter
        return riddle

    def get(self, letter: str = None) -> Optional[str]:
        """
        return возвращает загадку формата ( _ _ _ _ _ _ _)"""
        if self.finished:
            return None
        if not letter:
            return " ".join(self.riddle)
        self._check(self.word, self.riddle, letter)
        if "".join(self.riddle) == self.word:
            self.finished = True
            self.status = "win"
            return self.word
        return " ".join(self.riddle)
