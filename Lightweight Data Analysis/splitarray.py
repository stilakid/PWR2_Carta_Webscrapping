import json

FILENAME = "all_links.json"


def main():
    with open(FILENAME) as f:
        data = json.load(f)
        new_data_1 = data[5500:6500]
        new_data_2 = data[6500:7500]
        new_data_3 = data[7500: 8500]
        new_data_4 = data[8500:]
        json.dump(new_data_1, open('links_part_1.json', 'w'))
        json.dump(new_data_2, open('links_part_2.json', 'w'))
        json.dump(new_data_3, open('links_part_3.json', 'w'))
        json.dump(new_data_4, open('links_part_4.json', 'w'))



if __name__ == '__main__':
    main()