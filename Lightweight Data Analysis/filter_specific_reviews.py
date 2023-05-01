import json
import os

FILENAME = "all_reviews.json"

def main():
    # Count how many times the words fast and slow occurs
    fast = 0
    slow = 0
    with open(FILENAME) as f:
        data = json.load(f)
        for review in data:
            slow += review.count("slow")
            fast += review.count("fast")
    print("Word Count")
    print("fast : " + str(fast))
    print("slow : " + str(slow))

    # Count how many people use the words fast and slow
    fast = 0
    slow = 0
    either = 0
    with open(FILENAME) as f:
        data = json.load(f)
        for review in data:
            if "slow" in review:
                slow += 1
            if "fast" in review:
                fast += 1
            if "fast" in review or "slow" in review:
                either += 1
    print("Number of people who use the words")
    print("fast : " + str(fast))
    print("slow : " + str(slow))
    print("either : " + str(either))

    # Took out the following:
    # fast slow say tense rate speed pace warm cold tone
    vocal_features = [
        "voice",
        "vocal",
        "speech",
        "sound",
        "pronunciation",
        "hoarse",
        "pitch",
        "volume",
        "loud",
        "soft",
        "mumble",
        "jumble",
        "texture",
        "intonation",
        "monotone",
        "monotonic",
        "quiet",
        "verbal",
        "fluency",
        "enunciation",
        "articulation",
        "articulate",
        "phonation",
        "pause",
        "fluent",
        "slur"
    ]

    adjectives = [
        "pronunciation",
        "hoarse",
        "pitch",
        "loud",
        "soft",
        "mumble",
        "jumble",
        "mumbling",
        "intonation",
        "monotone",
        "monotonic",
        "quiet",
        "fluency",
        "pause",
        "fluent",
        "slur"
    ]

    filename = "vocal_feature_filter.json"
    filter_reviews(adjectives, filename)




    filename = "soft_voice_filter.json"
    filtered_data = []
    with open(FILENAME) as f:
        data = json.load(f)
        for review in data:
            if "soft" in review:
                filtered_data.append(review)

    i = 0
    while i != len(filtered_data):
        review = filtered_data[i]
        if review.count("soft") == review.count("software"):
            filtered_data.pop(i)
            i -= 1
        i += 1

    #
    # for i in range(len(filtered_data)):
    #     print(i)
    #     print(len(filtered_data))
    #     review = filtered_data[i]
    #     if review.count("soft") == review.count("software"):
    #         filtered_data.pop(i)
    #         i -= 1
    json.dump(filtered_data, open(filename, 'w'))
    print("Number of reviews in " + str(filename) + ": " + str(len(filtered_data)))




def filter_reviews(vocal_features, filename):
    filtered_data = []
    with open(FILENAME) as f:
        data = json.load(f)
        for review in data:
            for vocal_feature in vocal_features:
                if vocal_feature in review:
                    filtered_data.append(review)
                    break
        json.dump(filtered_data, open(filename, 'w'))
    print("Number of reviews in " + str(filename) + ": " + str(len(filtered_data)))


if __name__ == '__main__':
    main()