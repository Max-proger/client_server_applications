import yaml

DATA_IN = {
    "items": ["xerox", "notebook", "office"],
    "cnt": 100000,
    "currency": {
        "USD": "1$",
        "EUR": "1€",
        "RUR": "1₽",
    },
}

with open("test.yaml", "w", encoding="utf-8") as f_w:
    yaml.dump(DATA_IN, f_w, default_flow_style=False, allow_unicode=True)

with open("test.yaml", "r", encoding="utf-8") as f_r:
    DATA_OUT = yaml.load(f_r, Loader=yaml.SafeLoader)

print(DATA_IN == DATA_OUT)
