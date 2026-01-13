# 🧠 UzDct  
### Uzbek WordSet & Lightweight NLP Toolkit

> A fast, local, WordNet-style toolkit for exploring Uzbek lexical data — built for hackers, linguists, and NLP experimenters.

UzDct is a **minimal but powerful** Python toolkit that lets you explore an Uzbek WordNet-style dataset using simple, clean APIs.  
No heavy frameworks. No remote APIs. Just JSON, Python, and control.

---

## ✨ Why UzDct?

- 🇺🇿 Focused on the **Uzbek language**
- ⚡ Fast, **JSON-backed** word & synset lookups
- 🧩 WordNet-style **senses, synsets, and relations**
- 🧪 Perfect for **NLP experiments**, bots, and research
- 📦 Small, hackable, and easy to extend

---

## 🚀 Features

✔ Word → senses → definitions  
✔ Synsets with relations (hypernyms, hyponyms, etc.)  
✔ Human-readable **and** programmatic outputs  
✔ Zero network dependency  
✔ Bilingual documentation (EN / UZ)

---

## 📦 Installation

```bash
pip install -r UzbekWordSet/requirements.txt
```

---

## ⚡ Quick Start

```python
from UzbekWordSet.look_for_words import UzPyDictionary

d = UzPyDictionary()
print(d.meanings("kitob"))
```

---

## 🗂 Project Structure

```
UzbekWordSet/
├── wordNet_lookup.py
├── look_for_words.py
├── resources/
│   ├── entry.json
│   └── synset.json
└── requirements.txt
```

---

## 📜 License

Informal / experimental. Add a LICENSE file if publishing.

---

# 🧠 UzDct  
### O‘zbek WordSet va yengil NLP asboblari

> O‘zbek tili uchun WordNet uslubidagi leksik ma’lumotlarni o‘rganishga mo‘ljallangan tezkor va lokal Python asboblar to‘plami.

UzDct — bu **kichik, ammo kuchli** Python kutubxonasi bo‘lib, u o‘zbek tilidagi WordNet-ga o‘xshash ma’lumotlar bilan ishlash imkonini beradi.  
Og‘ir frameworklar yo‘q. Internetga bog‘liqlik yo‘q. Faqat JSON, Python va to‘liq nazorat.

---

## ✨ Nega UzDct?

- 🇺🇿 **O‘zbek tiliga** yo‘naltirilgan
- ⚡ Tezkor, **JSON asosida** ishlaydi
- 🧩 WordNet uslubidagi **ma’nolar, sinsetlar va munosabatlar**
- 🧪 NLP tajribalar, botlar va tadqiqotlar uchun qulay
- 📦 Kichik, moslashuvchan va kengaytirish oson

---

## 🚀 Imkoniyatlar

✔ So‘z → ma’nolar → ta’riflar  
✔ Sinsetlar va ularning munosabatlari (hypernym, hyponym va boshqalar)  
✔ Inson o‘qishi uchun qulay **va** dasturiy natijalar  
✔ Internet talab qilinmaydi  
✔ Ikki tilli hujjat (EN / UZ)

---

## 📦 O‘rnatish

Python **3.8+** o‘rnatilganligiga ishonch hosil qiling.

```bash
pip install -r UzbekWordSet/requirements.txt
```

---

## ⚡ Tez boshlash

```python
from UzbekWordSet.look_for_words import UzPyDictionary

d = UzPyDictionary()
print(d.meanings("kitob"))
```

---

## 🗂 Loyiha tuzilishi

```
UzbekWordSet/
├── wordNet_lookup.py      # Asosiy JSON qidiruv mexanizmi
├── look_for_words.py      # Qulay o‘ram (UzPyDictionary)
├── resources/
│   ├── entry.json         # Leksik yozuvlar
│   └── synset.json        # Sinsetlar va ta’riflar
└── requirements.txt
```

📌 **JSON fayllar — asosiy manba.**  
Qolgan hamma narsa — ular ustidagi qulay interfeys.

---

## 🧪 Nimalar qilish mumkin?

- 🤖 Telegram / Discord botlar  
- 📚 Lug‘at va til o‘rganish ilovalari  
- 🔍 Lingvistik tahlil skriptlari  
- 🧠 NLP oldindan qayta ishlash jarayonlari  
- 🧪 Ilmiy yoki shaxsiy tadqiqotlar  

Bu “katta korporativ NLP” emas.  
Bu — **aniqlik, tezlik va nazorat**.

---

## 🛠 Hissa qo‘shish

Loyihani rivojlantirmoqchimisiz?

- 🐞 Xatoliklar uchun issue oching
- 🧩 O‘zgarishlarni kichik va aniq qiling
- 🧪 Testlar yoki namuna skriptlar qo‘shing
- 📐 JSON tuzilmasini saqlab qoling

Minimalizm > murakkablik.

---

## 📜 Litsenziya

Hozircha loyiha **norasmiy va tajriba uchun** mo‘ljallangan.  
Agar ommaviy tarqatmoqchi bo‘lsangiz, LICENSE fayl qo‘shing.

---

## Xulosa

UzDct — bu **o‘rganish, tajriba va chuqur tushunish** uchun yaratilgan loyiha.  
Agar siz o‘zbek tili bilan NLP qilishni jiddiy xohlasangiz — shu yerdan boshlang.

---
