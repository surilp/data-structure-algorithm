from implement_trie import Trie

repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
query = "mouse"


class SearchHelper:

    def __init__(self, repository):
        self.trie = Trie()
        for word in repository:
            self.trie.insert(word)

    def customer_query(self, query):
        result = []
        if len(query) < 2:
            raise Exception("query len must be 2 or more")
        for idx in range(1, len(query)):
            result.append(self.trie.list_of_words_start_with(query[:idx + 1]))
        return result


search_helper = SearchHelper(repository)
print(search_helper.customer_query(query))
