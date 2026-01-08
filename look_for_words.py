import json

class UzPyDictionary:
    _entry_cache = None
    _synset_cache = None

    def __init__(self, entry_path="UzbekWordSet/entry.json", synset_path="UzbekWordSet/synset.json"):
        if UzPyDictionary._entry_cache is None:
            with open(entry_path, "r", encoding="utf-8") as f:
                UzPyDictionary._entry_cache = json.load(f)

        if UzPyDictionary._synset_cache is None:
            with open(synset_path, "r", encoding="utf-8") as f:
                UzPyDictionary._synset_cache = json.load(f)

        self.entry = UzPyDictionary._entry_cache
        self.synset = UzPyDictionary._synset_cache

    def find_words_by_wId(self, wId:str):
        for item in self.entry:
            if item["@id"] == wId:
                return item["lemma"]["writtenForm"]
            
    def definition(self, word_id: str):
        for item in self.synset:
            if item["@id"] == word_id:
                result= f"""{item["partOfSpeech"]} synonyms: {[self.find_words_by_wId(wId=wid) for wid in item["members"]]} definitions: {[gloss["gloss"] for gloss in item["definition"]]} 
                    """
                return result
    
    def get_all_ref_ids(self, ref_list):
        # returns a list of synsetRef ID
        ref_ids =list()
        for item in ref_list:
           ref_ids.append(item["synsetRef"])
        
        return ref_ids


    
    def look_for_word(self, word: str):
        # looks for an object of a word and returns obj
        for item in self.entry:
            if item["lemma"]["writtenForm"] == word:
                return item
        return None
    
    
    
    def demo_meaning(self, word: str):
        obj = self.look_for_word(word)
        ref_list = self.get_all_ref_ids(obj["sense"])

        print(f"""
{obj["lemma"]["writtenForm"]}
{obj["partOfSpeech"]}""")
        for definition in [self.definition(word_id=word_id) for word_id in ref_list]:
            print(definition)


    


d = UzPyDictionary()
# print(d.look_for_word("kitob"))

# print("all ids")
# sense= [{'@id': 'uzwordnet-2870092-n-1', 'synsetRef': 'uzwordnet-2870092-n'}, {'@id': 'uzwordnet-2870526-n-1', 'synsetRef': 'uzwordnet-2870526-n'}, {'@id': 'uzwordnet-6394865-n-1', 'synsetRef': 'uzwordnet-6394865-n'}, {'@id': 'uzwordnet-6410904-n-1', 'synsetRef': 'uzwordnet-6410904-n'}, {'@id': 'uzwordnet-6636524-n-1', 'synsetRef': 'uzwordnet-6636524-n'}, {'@id': 'uzwordnet-7009946-n-3', 'synsetRef': 'uzwordnet-7009946-n'}, {'@id': 'uzwordnet-7954211-n-1', 'synsetRef': 'uzwordnet-7954211-n'}, {'@id': 'uzwordnet-7954441-n-1', 'synsetRef': 'uzwordnet-7954441-n'}, {'@id': 'uzwordnet-9812068-n-2', 'synsetRef': 'uzwordnet-9812068-n'}, {'@id': 'uzwordnet-13404248-n-1', 'synsetRef': 'uzwordnet-13404248-n'}, {'@id': 'uzwordnet-1111418-s-1', 'synsetRef': 'uzwordnet-1111418-s'}]
# print(d.get_all_ref_ids(ref_list=sense))

# print("definition")
# print(d.definition(word_id="uzwordnet-2870092-n"))

d.demo_meaning(word="kitob")