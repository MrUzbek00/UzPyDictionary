with open("UzbekWordSet/uzwordnet_v1.0.json", "r") as f:
    data = f.read()

import json
uzwordnet = json.loads(data)

for key, item in uzwordnet.items():
    print(key)
    print(type(item))
    if key =="@graph":
        inner_list_item = item[0]
        print(type(inner_list_item))
        print(inner_list_item.keys())
        with open("UzbekWordSet/entry.json", "w") as f:
            entry= inner_list_item["entry"]
            synset = inner_list_item["synset"]
            json.dump(entry, f, indent=4, ensure_ascii=True)
        with open("UzbekWordSet/synset.json", "w") as f:
            synset = inner_list_item["synset"]
            json.dump(synset, f, indent=4, ensure_ascii=True)
        entry= inner_list_item["entry"]
        print(f"entry: {type(entry)}")
        print(len(entry))
        synset = inner_list_item["synset"]
        print(f"synset: {type(synset)}")
        print(len(synset))

# import json
# with open("UzbekWordSet/entry_synset.json", "r") as f:
#     data = f.read()
# uzwordnet = json.loads(data)
# print(uzwordnet.keys())            
