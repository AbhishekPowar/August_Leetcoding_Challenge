class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = set()
        self.ans = dict()
       

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.words.add(word)
        self.ans = dict()
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        
        ans = self.ans.get(word,None)
        if ans !=None:
            return ans
        
        for w in self.words:
            if re.search(f'^{word}$',w)!=None:
                self.ans[word] = True
                return True
        self.ans[word]=False
        return False

# Trie solution will be uploaded soon
# class Node():
#     def __init__(self, data):
#         self.val = data
#         self.child = {}


# class Trie():
#     def __init__(self, data='/'):
#         self.root = Node(data)

#     def insert(self, data):
#         if not data:
#             return
#         head = data[0]

#         if head in self.root.child:
#             self.root.child[head].insert(data[1:])
#         else:
#             self.root.child[head] = Trie(head)
#             self.root.child[head].insert(data[1:])

#     def display(self, lvl=1,last=False,disable=set()):
        
#         base     = '\t|'*lvl
#         print(base)
#         print(base,'_', self.root.val)
#         for idx,i in enumerate(self.root.child,start=1):
#             self.root.child[i].display(lvl+1)

#     def search(self, data):

#         if not data:
#             return True
#         head = data[0]
#         if head in self.root.child:
#             return self.root.child[head].search(data[1:])
#         else:
#             return False


# if __name__ == "__main__":
#     t = Trie()
#     t.insert('bat')
#     t.insert('cat')
#     t.insert('ball')
#     t.insert('cot')
#     t.insert('ant')
#     t.display()
