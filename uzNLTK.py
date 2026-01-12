import json
import html
from pathlib import Path
from typing import Any, Dict, List, Optional, Iterable


class UzPyDictionary:
    _entry_cache: Optional[List[Dict[str, Any]]] = None
    _synset_cache: Optional[List[Dict[str, Any]]] = None

    def __init__(self, entry_path: str = "UzbekWordSet/entry.json", synset_path: str = "UzbekWordSet/synset.json"):
        if UzPyDictionary._entry_cache is None:
            with open(entry_path, "r", encoding="utf-8") as f:
                UzPyDictionary._entry_cache = json.load(f)

        if UzPyDictionary._synset_cache is None:
            with open(synset_path, "r", encoding="utf-8") as f:
                UzPyDictionary._synset_cache = json.load(f)

        self.entry = UzPyDictionary._entry_cache
        self.synset = UzPyDictionary._synset_cache

        # ---- Indexes (the big win) ----
        self.entry_by_id: Dict[str, Dict[str, Any]] = {e["@id"]: e for e in self.entry if "@id" in e}
        self.synset_by_id: Dict[str, Dict[str, Any]] = {s["@id"]: s for s in self.synset if "@id" in s}

        self.entries_by_lemma: Dict[str, List[Dict[str, Any]]] = {}
        for e in self.entry:
            lemma = (e.get("lemma") or {}).get("writtenForm")
            if lemma:
                self.entries_by_lemma.setdefault(lemma, []).append(e)

    # ---------- Helpers ----------
    @staticmethod
    def _clean_target(target: str) -> str:
        # dataset can contain weird targets like "uzwordnet-4475, 00007347-n"
        # Keep the first token that looks like an id
        return target.split(",")[0].strip()

    @staticmethod
    def _join(items: Iterable[str]) -> str:
        return ", ".join([i for i in items if i])

    # ---------- Lookups ----------
    def lemma_by_word_id(self, wId: str) -> Optional[str]:
        e = self.entry_by_id.get(wId)
        if not e:
            return None
        return (e.get("lemma") or {}).get("writtenForm")

    def synset(self, synset_id: str) -> Optional[Dict[str, Any]]:
        return self.synset_by_id.get(synset_id)

    def definition(self, synset_id: str) -> Optional[Dict[str, Any]]:
        s = self.synset_by_id.get(synset_id)
        if not s:
            return None

        members = [self.lemma_by_word_id(wid) for wid in s.get("members", [])]
        members = [m for m in members if m]  # drop missing

        definitions = [
            html.unescape(d.get("gloss", ""))
            for d in s.get("definition", [])
            if isinstance(d, dict)
        ]

        relations = self.get_relations(s.get("relations", []))

        return {
            "synset_id": synset_id,
            "partOfSpeech": s.get("partOfSpeech"),
            "members": members,
            "definitions": definitions,
            "relations": relations,
        }

    def get_relations(self, relation_list: List[Dict[str, Any]]) -> Dict[str, List[str]]:
        rels: Dict[str, List[str]] = {}
        for r in relation_list or []:
            rel_type = r.get("relType")
            target = r.get("target")
            if not rel_type or not target:
                continue

            target_id = self._clean_target(target)
            rels.setdefault(rel_type, []).append(target_id)

        return rels

    def sense_ref_ids(self, entry_obj: Dict[str, Any]) -> List[str]:
        return [s.get("synsetRef") for s in entry_obj.get("sense", []) if s.get("synsetRef")]

    def lookup(self, word: str) -> List[Dict[str, Any]]:
        # returns list because a lemma can map to multiple entries/POS
        return self.entries_by_lemma.get(word, [])

    # ---------- High-level API ----------
    def meanings(self, word: str) -> Dict[str, Any]:
        entries = self.lookup(word)
        if not entries:
            raise KeyError(f"No such word: {word}")

        results = []
        for e in entries:
            ref_ids = self.sense_ref_ids(e)
            senses = [self.definition(sid) for sid in ref_ids]
            senses = [s for s in senses if s]  # drop missing synsets

            results.append({
                "lemma": (e.get("lemma") or {}).get("writtenForm"),
                "partOfSpeech": e.get("partOfSpeech"),
                "senses": senses,
            })

        return {"word": word, "entries": results}


d =UzPyDictionary()

print(d.meanings(word="uka"))