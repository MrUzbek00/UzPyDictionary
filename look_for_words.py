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

    def meaning(self, word: str):
        for item in self.entry:
            if item["lemma"]["writtenForm"] == word:
                return item
        return None


d = UzPyDictionary()
print(d.meaning("kitob"))