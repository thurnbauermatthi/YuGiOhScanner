import json
import yaml
names = []

with open("id_class.json", "r", encoding="iso-8859-1") as f:
    for line in f:
        c = json.loads(line)
        name = c.get("id")
        names.append(str(name))
data = {"train": "data/train/images",
        "val": "data/valid/images",
        "nc": 12759,
        "names": names}

with open("data.yaml", "w", encoding="iso-8859-1") as f:
    yaml.dump(data, f)