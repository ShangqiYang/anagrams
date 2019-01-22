"""
Here is the core function of this application.

Used data structure Trie to stroe all the words in dictionary, cause Trie is very good and fast way to check if this word exist in the dictionary. And this way will save Time Complexity and Space Complexity (if we store all the words in list, and compare one by one to find it this word exist in this dictionay)

Advantage: use dictionary_path as argument to init Trie, add word to Trie and at the same time append the sorted word to the anagrams_group dictionary. It's convenient to query the word's anagrams group.

What I want to do in the future: 1. create detail page for every dictionary and pre-process the data of the dictionary. So you can repeatedly query words in the same dictionary. 2. Use AJAX to show the result, do not neet refresh page every time.

For Big data, like a billion words, I will choose Hadoop or Spark to process these big data, cause they can provide powerful Map-Reduce job to handle these data. And I think Trie will still be a good way to implement this function.

For real product: 1. Add user auth to make users register, login and check their own data 2. build secruity layer 3. Integrate with 3rd party framework like React, PostegreSQL to extent functionality and enrich content.

"""

# create a class name TrieNode to create 
class TrieNode(object):
    def __init__(self):
        # judge if it is or not a word
        self.is_word = False
        self.children = [None] * 26

class Trie(object):
    def __init__(self, dictionary_path):
        self.root = TrieNode()
        self.anagrams_group = {}
        
        with open(dictionary_path, 'r') as dictionary:
            for word in dictionary:
                word = word.strip('\n')
                self.add(word)
    
    def add(self, word):
        # Add a word to anagrams group
        word_sorted = "".join(sorted(word))
        if word_sorted in self.anagrams_group:
            self.anagrams_group[word_sorted].append(word)
        else:
            self.anagrams_group[word_sorted] = [word]
            
        # Add a word to this trie
        p = self.root
        n = len(word)
        for i in range(n):
            if p.children[ord(word[i]) - ord('a')] is None:
                new_node = TrieNode()
                if i == n - 1:
                    new_node.is_word = True
                p.children[ord(word[i]) - ord('a')] = new_node
                p = new_node
            else:
                p = p.children[ord(word[i]) - ord('a')]
                if i == n - 1:
                    p.is_word = True
                    return
    
    def search(self, word):
        # Judge whether s is in this tire
        p = self.root
        for c in word:
            p = p.children[ord(c) - ord('a')]
            if p is None:
                return False
        if p.is_word:
            return True
        else:
            return False
        
    def check(self, word):
        if(self.search(word)):
            word_sorted = "".join(sorted(word))
            group = self.anagrams_group[word_sorted]
            group.sort(key = lambda w : w[1])
            return group
        else:
            return None

"""
if __name__ == '__main__':
    trie_test = Trie('dictionary_test.txt')
    trie = Trie('dictionary.txt')
    
    print(trie_test.check('word'))
    print(trie.check('word'))
"""