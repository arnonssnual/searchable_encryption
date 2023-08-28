import json

class TrieNode:
    def __init__(self):
        self.children = {}
        self.values = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, keyword, value):
        node = self.root
        for char in keyword:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.values.append(value)

    def search(self, keyword):
        node = self.root
        for char in keyword:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.values

    def to_json(self, node=None):
        if node is None:
            node = self.root

        data = {
            "values": node.values,
            "children": {}
        }

        for char, child_node in node.children.items():
            data["children"][char] = self.to_json(child_node)

        return data

    def save_to_json_file(self, filename):
        with open(filename, "w") as f:
            json.dump(self.to_json(), f, indent=2)

    @classmethod
    def from_json(cls, data):
        trie = cls()
        trie.root = TrieNode()
        trie.root.values = data["values"]
        for char, child_data in data["children"].items():
            trie.root.children[char] = cls._build_from_json(child_data)
        return trie

    @staticmethod
    def _build_from_json(data):
        node = TrieNode()
        node.values = data["values"]
        for char, child_data in data["children"].items():
            node.children[char] = Trie._build_from_json(child_data)
        return node