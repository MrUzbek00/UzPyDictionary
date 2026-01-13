# UzDct — Uzbek WordSet & NLP Tools

A small, local toolkit for exploring an Uzbek WordNet-style dataset and simple NLP helpers.

This repository contains a lightweight WordNet lookup implementation, helper functions to query words and senses, and an example script that introspects an UzbekNLP package.

---

## Features

- Fast JSON-backed lookup of word entries and synsets
- Friendly helpers to get definitions, members, and relations
- Example scripts to print human-readable meanings and programmatic outputs
- Bilingual README and clear structure for quick experimentation

---

## Quickstart

1. Ensure you have Python 3.8+ and dependencies installed (if any listed in requirements.txt):

```bash
pip install -r UzbekWordSet/requirements.txt
```

2. Run the example lookup script:

```bash
python "UzbekWordSet/look_for_words.py"
```

3. Import the lookup class in your own code:

```python
from UzbekWordSet.look_for_words import UzPyDictionary

d = UzPyDictionary()
print(d.meanings('kitob'))
```

---

## File layout (important files)

- UzbekWordSet/
  - wordNet_lookup.py — core JSON-backed lookup (entry & synset readers, helpers)
  - look_for_words.py — UzPyDictionary wrapper with human-friendly output and structured meanings
  - resources/entry.json — lexical entries
  - resources/synset.json — synset records and definitions
  - requirements.txt — minimal dependencies

---

## Usage tips

- Use `UzPyDictionary.meanings(word)` to get all senses in a structured dict.
- Use `UzPyDictionary.meaning(word)` to get only the first sense.
- `look_for_words.demo_meaning(word)` prints a human-readable breakdown.
- The JSON files are the source of truth — you can inspect them directly for more context.

---

## Contributing

- Add issues describing bugs or feature requests.
- Keep changes small and focused; prefer adding tests or example scripts.
- If you expand the dataset, keep the same structure for entry.json and synset.json.

---

## License & Contact

This project is informal and intended for learning / experimentation. Add a LICENSE file if you intend to share or publish.

For questions or quick help, open an issue or contact the repository owner.

---

# O'zbekcha (Uzbek)

UzDct — Oʻzbek soʻz toʻplami va oddiy NLP yordamchilari uchun kichik asbob toʻplami.

Ushbu loyiha WordNet uslubidagi Oʻzbek lugʻat maʼlumotlarini JSON formatida saqlaydi va ulardan foydalanish uchun qulay yordamchi funksiyalarni taqdim etadi.

## Xususiyatlar

- JSON fayllarga asoslangan tezkor soʻz va sinset qidiruvi
- Taʼriflar, aʼzolar va munosabatlarni qaytaruvchi yordamchilar
- Namuna skriptlar: inson oʻqishi uchun chiqarish va dasturiy natija olish

## Boshlash

1. Python 3.8+ oʻrnatilganligiga ishonch hosil qiling va kerakli kutubxonalarni oʻrnating:

```bash
pip install -r UzbekWordSet/requirements.txt
```

2. Namuna skriptni ishga tushiring:

```bash
python "UzbekWordSet/look_for_words.py"
```

3. Kutubxonani o'z loyihangizda ishlating:

```python
from UzbekWordSet.look_for_words import UzPyDictionary

d = UzPyDictionary()
print(d.meanings('kitob'))
```

## Fayl tuzilishi

- UzbekWordSet/
  - wordNet_lookup.py — asosiy JSON qidiruv kodi
  - look_for_words.py — UzPyDictionary o'rab oluvchi va formati berilgan natija
  - resources/entry.json — leksik yozuvlar
  - resources/synset.json — sinset yozuvlari va ta'riflari
  - requirements.txt — minimal bog'liqliklar

## Foydalanish bo'yicha maslahatlar

- Barcha ma'nolar uchun: `UzPyDictionary.meanings(word)`
- Faqat birinchi maʼno uchun: `UzPyDictionary.meaning(word)`
- Inson o'qishi uchun: `demo_meaning(word)`
- JSON fayllarni to'g'ridan-to'g'ri tekshirib, qo'shimcha kontekst oling.

---

Rahmat! Loyihani rivojlantirish yoki savollar uchun issue oching yoki egasi bilan bog'laning.