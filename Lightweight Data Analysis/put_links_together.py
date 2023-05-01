import os
import json
LINKS_DIRECTORY = "Data/Links"


def main():
    links = set()
    for filename in os.listdir(LINKS_DIRECTORY):
        with open(os.path.join(LINKS_DIRECTORY, filename), 'r') as f:
            # text = f.read()
            data = json.load(f)
            links.update(data)
    links = list(links)
    print(links)
    print(len(links))
    json.dump(links, open('all_links.json', 'w'))


if __name__ == '__main__':
    main()

