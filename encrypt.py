from Crypto.Hash import SHA256
from trie_mod import Trie,save_hashed_trie_to_json


def hash_keyword(words):
    hash_object = SHA256.new()
    #print(type(words))
    words = bytes(words, 'utf-8')
    #print((words))
    hash_object.update(words)
    return (hash_object.hexdigest())

def read_file(keyword_filepath):
    with open(keyword_filepath) as keyword_file:
        keyword_file = (keyword_file.read())
        
        # Remove the parentheses and split the string into individual tuples
        tuple_strings = keyword_file.split(')(')

        # Extract words from the tuples
        words = [tuple_string.split(',')[0].strip("('") for tuple_string in tuple_strings]
    
    return (words)




""" 
words = read_file('output.txt')
trie = Trie()
count = 0
for word in words:
    #if(count == 3):
    #    break
    #count += 1

    hash_value = hash_keyword(word)
    print(hash_value)
    trie.insert(hash_value)

# Save the hashed Trie to a JSON file
save_hashed_trie_to_json(trie, "hashed_trie.json")  """



#print(trie.search("9285827b8031a1dbe7d1d04eb8a08c8891ee424a8002cfc7dd2df3d82cbff611"))




