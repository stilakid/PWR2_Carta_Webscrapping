import json
import os

REVIEWS_DIRECTORY = "Data/Reviews"


def main():
    reviews = set()
    i = 1;
    for filename in os.listdir(REVIEWS_DIRECTORY):
        with open(os.path.join(REVIEWS_DIRECTORY, filename), 'r') as f:
            print(i)
            print(filename)
            if filename == ".DS_Store":
                continue
            data = json.load(f)
            reviews.update(data)
            i += 1
    reviews = list(reviews)
    print(reviews)
    print(len(reviews))
    json.dump(reviews, open('all_reviews.json', 'w'))


if __name__ == '__main__':
    main()