import json

FILENAME = "all_reviews.json"


def main():
    filtered_data = []
    vocal_features = [
        "voice",
        "vocal",
        "speech",
        "sound",
        "communication",
        "communicate",
        "spoke",
        "pronunciation",
        "hoarse",
        "say",
        "speak",
        "talk",
        "present",
        "abrupt",
        "warm",
        "smooth",
        "cold",
        "tense",
        "pitch",
        "volume",
        "loud",
        "soft",
        "mumble",
        "jumble",
        "rate",
        "tone",
        "texture",
        "intonation",
        "resonance",
        "rhythm",
        "harsh",
        "monotone",
        "monotonic",
        "fast",
        "slow",
        "speed",
        "pace",
        "clear",
        "clean",
        "repeat",
        "clarity",
        "vague",
        "clean",
        "gentle",
        "quiet",
        "verbal",
        "tic",
        "fluency",
        "enunciation",
        "articulation",
        "phonation",
        "pause",
        "fluent"
    ]

    with open(FILENAME) as f:
        data = json.load(f)
        for review in data:
            review = review.lower()
            for vocal_feature in vocal_features:
                if vocal_feature in review:
                    filtered_data.append(review)
                    break;
        json.dump(filtered_data, open('filtered_data.json', 'w'))


if __name__ == '__main__':
    main()

    # The actual vocal_features list had different elements depending upon what I wanted to filter.