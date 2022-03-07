import json


def write_order_to_json(item, quantity, price, buyer, date):

    with open("orders.json", "r", encoding="utf-8") as f_r:
        data = json.load(f_r)

    with open(
        "orders.json",
        "w",
        encoding="utf-8",
    ) as f_w:
        orders = data["orders"]

        dict_info = {
            "item": item,
            "quantity": quantity,
            "price": price,
            "buyer": buyer,
            "date": date,
        }
        orders.append(dict_info)
        json.dump(data, f_w, indent=4, ensure_ascii=False)


write_order_to_json("xerox", "100", "50000", "Ромашка", "1.02.2022")
write_order_to_json("notebook", "20", "100000", "Max", "14.02.2022")
write_order_to_json("компьютер", "5", "140000", "IMB", "2.2.2022")
