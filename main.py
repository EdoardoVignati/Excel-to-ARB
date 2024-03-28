import pandas as pd
import json

df = pd.read_excel("./l10n.xlsx", sheet_name=0)
languages = {}
keys = {}
for index, value in df.to_dict().items():
    if str(index) == "key":
        keys = value
        continue
    languages[str(index)] = value

for lang, values in languages.items():
    current_lang_map = {}
    for i in range(0, len(keys)):
        current_lang_map.update({keys[i]: values[i]})
    file_name = "app_" + lang + ".arb"
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(current_lang_map, f, indent=1, sort_keys=True, ensure_ascii=False)
