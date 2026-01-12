import json
class WordNetLookup:
    _entry_cache = None
    _synset_cache = None

    def __init__(self, entry_path="UzbekWordSet/resources/entry.json", synset_path="UzbekWordSet/resources/synset.json"):
        """
        Initialize WordNetLookup by loading entry and synset data from JSON files.
        Returns: None
        """
        if WordNetLookup._entry_cache is None:
            with open(entry_path, "r", encoding="utf-8") as f:
                WordNetLookup._entry_cache = json.load(f)

        if WordNetLookup._synset_cache is None:
            with open(synset_path, "r", encoding="utf-8") as f:
                WordNetLookup._synset_cache = json.load(f)

        self.entry = WordNetLookup._entry_cache
        self.synset = WordNetLookup._synset_cache

    def find_words_by_wId(self, wId:str):
        """
        Find and return the written form of a word given its word ID from entry data.
        Args:
            wId (str): The word ID to look up.
        Returns:
            str: The written form of the word if found, else None.
        """
        for item in self.entry:
            if item["@id"] == wId:
                return item["lemma"]["writtenForm"]
    
    def find_synset_by_wId(self, wId:str):
        """
        Find and return the written form of a synset given its ID from synset data.
        Args:
            wId (str): The synset ID to look up.
        Returns:
            str: The written form of the synset if found, else None.
        """
        for item in self.synset:
            if item["@id"] == wId:
                return item["lemma"]["writtenForm"]
            
    def definition(self, word_id: str):
        """
        Return the definition record for a given synset (word) ID.
        Args:
            word_id (str): The synset ID to look up.
        Returns:
            dict: Contains 'partOfSpeech', 'members', and 'definitions' for the synset.
        """
        for item in self.synset:
            if item["@id"] == word_id:
                partOfSpeech = item["partOfSpeech"]
                members=[self.find_words_by_wId(wId=wid) for wid in item["members"]]
                definitions = [gloss["gloss"] for gloss in item["definition"]]
                
                
                result = {
                    "partOfSpeech" : partOfSpeech,
                    "members": members,
                    "definitions": definitions,
                    # "relations" : relations
                }
                return result
            
    def get_relations(self, relation_list: list):
        """
        Extract hypernym and hyponym relations from a list of relations.
        Args:
            relation_list (list): List of relation dicts.
        Returns:
            dict: {'hypernym': list, 'hyponym': list} of related words.
        """
        hypernym = []
        hyponym= []
        for item in relation_list:
            if item["relType"] == "hypernym":
                print(self.find_synset_by_wId(item["target"]))
                # hypernym.append(self.find_words_by_wId(item["target"]))
            else: 
                hyponym.append(self.find_words_by_wId(item["target"]))
        result = {  "hypernym" : hypernym,
                    "hyponym" : hyponym,
                      }
        return result
    
    def get_all_ref_ids(self, ref_list):
        """
        Return a list of synsetRef IDs from a list of references.
        Args:
            ref_list (list): List of reference dicts with 'synsetRef' keys.
        Returns:
            list: List of synsetRef IDs.
        """
        ref_ids = list()
        for item in ref_list:
           ref_ids.append(item["synsetRef"])
        
        return ref_ids


    
    def look_for_word(self, word: str):
        """
        Search for a word in the entry data and return its object if found.
        Args:
            word (str): The word to look up.
        Returns:
            dict: The entry object if found, else False.
        """
      
        for item in self.entry:
            if item["lemma"]["writtenForm"] == word:
                return item
        
        return False
    
    def unlisting(self, members_list:list):
        """
        Convert a list of members to a comma-separated string.
        Args:
            members_list (list): List of members.
        Returns:
            str: Comma-separated string of members.
        """
        result =str()
        for item in members_list:
            result += str(item) + ", "
        return result


