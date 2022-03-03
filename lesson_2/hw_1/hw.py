import csv
import re


def get_data():
    txt_list = ["info_1.txt", "info_2.txt", "info_3.txt"]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]]

    for file in txt_list:
        datafile = open(file)

        for row in datafile:
            row = row.rstrip()
            if re.match("Изготовитель системы", row):
                os_prod_list.append(re.search(r"(Изготовитель системы).\s*(.*)", row).group(2))
            elif re.match("Название ОС", row):
                os_name_list.append(re.search(r"(Название ОС).\s*(.*)", row).group(2))
            elif re.match("Код продукта", row):
                os_code_list.append(re.search(r"(Код продукта).\s*(.*)", row).group(2))
            elif re.match("Тип системы", row):
                os_type_list.append(re.search(r"(Тип системы).\s*(.*)", row).group(2))

    for i in range(len(txt_list)):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])
    return main_data


def write_to_csv(file, data):
    with open(file, "w", encoding="utf-8") as f:
        f_writer = csv.writer(f)
        for row in data:
            f_writer.writerow(row)


if __name__ == "__main__":
    write_to_csv("data_report.csv", get_data())
