import csv
import random
import os

os.makedirs("data", exist_ok=True)

labels = {
    "praise": [
        "Amazing work! Loved the animation.",
        "This is fantastic, great job!",
        "So creative, I loved it!"
    ],
    "support": [
        "Keep going, you're doing great!",
        "We support you, keep it up!",
        "Bravo! More content like this please."
    ],
    "constructive": [
        "The animation is good but the voiceover felt off.",
        "I like the idea, but the pacing needs work.",
        "Nice effort — maybe use a clearer font next time."
    ],
    "hate": [
        "This is trash, quit now.",
        "Worst thing I've seen.",
        "You should stop, this is awful."
    ],
    "threat": [
        "I'll report you if this continues.",
        "If you don't remove this, I'll take action.",
        "This is illegal — expect consequences."
    ],
    "emotional": [
        "This reminded me of my childhood, thank you.",
        "I cried watching this, such memories.",
        "This hit me hard, so nostalgic."
    ],
    "spam": [
        "Follow me for followers",
        "Check out my profile for free gifts",
        "Visit my site for freebies!"
    ],
    "question": [
        "Can you make one on topic X?",
        "How long did it take to make this?",
        "Which software did you use?"
    ]
}

rows = []

# base rows
for label, examples in labels.items():
    for ex in examples:
        rows.append((ex, label))

# create more variations
for _ in range(250):
    label = random.choice(list(labels.keys()))
    base = random.choice(labels[label])
    text = base + random.choice(["!!", " 👍", " please", ""])
    rows.append((text, label))

random.shuffle(rows)

with open("data/labeled_comments.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "label"])
    writer.writerows(rows)

print("Dataset created: data/labeled_comments.csv")
