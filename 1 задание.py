def find_estate(db):
    with open('was_sold.csv', 'w') as answer:
        with open(db, 'r') as database:
            my_dict = {}
            # Описание не получилось открыть, наверное столбцы 8-13 это адрес объекта
            for row in database:
                cols = row.strip().split(',')
                items = [cols[i] for i in range(7, 13)]
                address = ", ".join(items).replace('"', '') + "\n"

                if address not in my_dict:
                    my_dict[address] = 1
                elif my_dict[address] == 1:
                    my_dict[address] += 1
                    answer.write(address)
                else:
                    continue


if __name__ == "__main__":
    find_estate('pp-complete.csv')