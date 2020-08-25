class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = set(words)
        self.maxx = len(max(self.words, key=len))
        self.tails = {word[-1] for word in words}
        self.qs = ''

    def query(self, letter: str) -> bool:
        self.qs += letter
        if len(self.qs) > self.maxx:
            self.qs = self.qs[1:]
        if letter not in self.tails:
            return False
        N = len(self.qs)
        return any((self.qs[i:N] in self.words for i in range(N-1, -1, -1)))


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
