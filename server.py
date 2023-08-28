from flask import Flask,Response,request,jsonify
from trie import Trie
from encrypt import hash_keyword
import json

app = Flask(__name__)


@app.route("/")
def hello():
  return "Hello World!"


@app.route('/search',methods = ['POST'])
def search_keyword():
    keyword = request.json
    
    if 'input' in keyword:
        input_text = keyword['input']
        
        hashed_keyword_ = hash_keyword(input_text)
        result = trie.search(hashed_keyword_)

        return jsonify({"response": result})
    else:
        return jsonify({"error": "Input not provided"}), 400

@app.route('/update_index', methods = ['POST'])
def update_keyword():
    keyword = request.json
    #metadata = keyword['metadata']
    
    for i in keyword:
        existing_values = trie.search(i)
        if existing_values:
            if keyword[i] not in existing_values:
                trie.insert(i, keyword[i])
                #trie.save_to_json_file("../trienew.json")
            else:
                pass
        else:
            trie.insert(i, keyword[i])
    trie.save_to_json_file("../trienew.json")
    return "Index Updated"




@app.route('/connect')
def connect():
    
    global trie
    trie = load_index()
    Response("Index Loaded")
    return "connected"

def load_index():
    try:
        with open("../trienew.json", "r") as f:
            trie_data = json.load(f)
            trie = Trie.from_json(trie_data)
    except FileNotFoundError:
        trie = Trie()
    
    return trie


if __name__ == "__main__":
  trie = load_index()
  app.run(debug=True)