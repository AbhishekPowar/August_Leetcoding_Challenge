class Solution:
    def toGoatLatin(self, S: str) -> str:
        answer = []
        vowels = set('aeiouAEIOU')
        for idx, word in enumerate(S.split(' '), start=1):
            tail = 'a'*idx
            latinWord = word
            if word[0] not in vowels:
                latinWord = word[1:]+word[0]
            answer.append(latinWord+'ma'+tail)
        return ' '.join(answer)
