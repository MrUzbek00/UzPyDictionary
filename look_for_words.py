from wordnet_lookup import WordNetLookup

class UzPyDictionary(WordNetLookup):   

    """Dictionary wrapper around WordNetLookup with helper output methods."""

    def demo_meaning(self, word: str):
        """Print a detailed human-readable listing of senses for `word`.

        Parameters:
            word (str): the query word.

        Returns:
            None -- results are printed to stdout.
        """
        obj = self.look_for_word(word)
        if obj!=False:
            ref_list = self.get_all_ref_ids(obj["sense"])
            print(f"""
    {obj["lemma"]["writtenForm"]}({obj["partOfSpeech"]})""")
            counter=1
            for definition in [self.definition(word_id=word_id) for word_id in ref_list]:
                print(counter)    
                if definition["partOfSpeech"] != obj["partOfSpeech"]:
                    print(definition["partOfSpeech"])
                print("members: ", self.unlisting(members_list = definition["members"]))
                print("definition: ", self.unlisting(definition["definitions"]))
                print("=======================================================")
                counter+=1
        
        else:
            print(f"There is no such word: ",word)
    
    def _meanings_core(self, word: str, limit: int | None = None):
        """Return structured meanings for `word`.

        Parameters:
            word (str): the query word.
            limit (int|None): max number of senses to return; None = all.

        Returns:
            dict: {
                'word': str,
                'part_of_speech': str|None,
                'senses': list of { 'sense_id', 'partOfSpeech', 'members', 'definition' },
                'error': str (only present if word not found)
            }
        """
        obj = self.look_for_word(word)
        if not obj:
            return {
                "word": word,
                "part_of_speech": None,
                "senses": [],
                "error": f"There is no such word: {word}"
            }

        ref_list = self.get_all_ref_ids(obj["sense"])
        if limit is not None:
            ref_list = ref_list[:limit]

        result = {
            "word": obj["lemma"]["writtenForm"],
            "part_of_speech": obj["partOfSpeech"],
            "senses": []
        }

        for idx, word_id in enumerate(ref_list, start=1):
            definition = self.definition(word_id=word_id)

            # POS (fallback to main POS if missing)
            pos = definition.get("partOfSpeech", obj["partOfSpeech"])

            # members normalize
            members = definition.get("members") or []
            if not isinstance(members, list):
                members = [members]
            members_list = [str(m).strip() for m in members if str(m).strip()]

            # definitions normalize (handle list/string/dict)
            defs = definition.get("definitions") or definition.get("definition") or ""
            if isinstance(defs, list):
                parts = []
                for x in defs:
                    if isinstance(x, dict):
                        parts.append(str(x.get("gloss", "")).strip())
                    else:
                        parts.append(str(x).strip())
                definition_text = "; ".join([p for p in parts if p])
            elif isinstance(defs, dict):
                definition_text = str(defs.get("gloss", "")).strip()
            else:
                definition_text = str(defs).strip()

            result["senses"].append({
                "sense_id": idx,
                "partOfSpeech": pos,
                "members": members_list,
                "definition": definition_text
            })

        return result


    def meanings(self, word: str):
        """Return all senses for `word`.

        Parameters:
            word (str): the query word.

        Returns:
            dict: same structure as returned by _meanings_core with limit=None.
        """
        # all senses
        return self._meanings_core(word, limit=None)


    def meaning(self, word: str):
        """Return the first sense for `word`.

        Parameters:
            word (str): the query word.

        Returns:
            dict: same structure as _meanings_core but containing at most one sense.
        """
        # first sense only
        return self._meanings_core(word, limit=1)


d = UzPyDictionary()

# d.demo_meaning(word="singil")
print(d.meanings("kitob"))