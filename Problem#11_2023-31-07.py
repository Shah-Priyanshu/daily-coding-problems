""" 
Problem :
Implement an autocomplete system. 
That is, given a query string s and a set of all possible query strings, 
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        return self._get_all_words_with_prefix(node, prefix)

    def _get_all_words_with_prefix(self, node, prefix):
        result = []
        if node.is_end_of_word:
            result.append(prefix)

        for char, child in node.children.items():
            result.extend(self._get_all_words_with_prefix(child, prefix + char))

        return result

class Solution:
    def autocomplete(query, word_set):
        trie = Trie()
        for word in word_set:
            trie.insert(word)

        return trie.search_prefix(query)


#__main__
query_string = "de"
query_set = ["dog", "deer", "deal"]
autocomplete_results = Solution.autocomplete(query_string, query_set)
print(autocomplete_results)  # Output: ['deer', 'deal']