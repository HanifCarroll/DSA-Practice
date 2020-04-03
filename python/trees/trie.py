class TrieNode(object):
    def __init__(self, value):
        self.is_word = False
        self.children = {}
        self.value = value

    def __repr__(self):
        return self.value

class Trie(object):
    def __init__(self):
        self.root = TrieNode('')

    def levelorder(self):
        q = []
        q.append(self.root)
        while len(q):
            current = q.pop()
            print(current)
            for value in current.children.values():
                q.append(value)
    
    def get_words(self):
        stack = []
        visited = []
        path = []
        stack.append(self.root)                  
        visited.append(self.root)                
        while stack:                         
            current = stack.pop()            
            path.append(current)
            if current.is_word:
                print("FOUND WORD:", path)
            for neigh in current.children.values():        
                if neigh not in visited:       
                    visited.append(neigh)       
                    stack.append(neigh)         
                    # if neigh.is_word:            


    def insert(self, word):
        # Loop through letters in the word
        current = self.root

        for letter in word:

        # Check if letter exists in current.children
            if not letter in current.children:
                current.children[letter] = TrieNode(letter)

        # If it does, update current.
            current = current.children[letter]

        # When at the last letter, place 'is_word' to be true.
        current.is_word = True
    
    def contains_prefix(self, word):
        current = self.root

        for letter in word:
            if not letter in current.children:
                return False
            current = current.children[letter]
        return bool(current)
    
    def contains_word(self, word):
        current = self.root

        for letter in word:
            if not letter in current.children:
                return False
            current = current.children[letter]
        return current.is_word
    

trie = Trie()

trie.insert('hello')
trie.insert('help')
# trie.levelorder()
trie.get_words()
