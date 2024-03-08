import pandas as pd
import json

df = pd.read_excel("./l10n.xlsx", sheet_name=0)
languages = {}
for row in df.itertuples():
    for key, val in row._asdict().items():
        if str(key) == "Index" or str(key) == "key":
            continue
        if languages.get(str(key)) is None:
            languages[str(key)] = {}
        languages[str(key)][row.key] = val

for lang in languages.keys():
    file_name = "app_" + lang + ".arb"
    with open(file_name, "x", encoding="utf-8") as f:
        json.dump(languages[lang], f, indent=1, sort_keys=True, ensure_ascii=False)