class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int,):
        s = characters
        n = combinationLength
        self.words = self.calc(s, n, txt='')
        self.hasnext = True
        self.data = next(self.words)

    def calc(self, s, n, txt):
        if n == 0:
            yield txt
        else:
            for idx in range(len(s)):
                yield from self.calc(s[idx+1:], n-1, txt+s[idx])

    def next(self) -> str:
        data = self.data
        try:
            self.data = next(self.words)
        except:
            self.hasnext = False
        return data

    def hasNext(self) -> bool:
        return self.hasnext


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
