import json
import datetime
from datetime import timezone

# Test posts

test_post_1 = {
    "id": 1,
    "title": "Test post",
    "body": "Google QA department",
    "author": "Brabygg",
    "date": 1686229860.0
}

test_post_2 = {
    "id": 2,
    "title": "Test post",
    "body": "holy fucking shit. if i see ONE more en passant meme i'm going to chop my fucking balls off."
            " holy shit it is actually impressive how incredibly unfunny the entire sub is. it's not that complicated, "
            "REPEATING THE SAME FUCKING JOKE OVER AND OVER AGAIN DOES NOT MAKE IT FUNNIER. this stupid fucking meme has "
            "been milked to fucking death IT'S NOT FUNNIER THE 973RD TIME YOU MAKE THE EXACT SAME FUCKING JOKE. WHAT'S EVEN THE JOKE?????? "
            "IT'S JUST \"haha it's the funne move from chess\" STOP. and the WORST part is that en passant was actually funny for like "
            "a few years and it got fucking ruined in like a week because EVERYONE POSTED THE EXACT SAME FUCKING JOKE OVER AND OVER AGAIN. "
            "PLEASE MAKE IT STOP. SEEING ALL YOUR SHITTY MEMES IS ACTUAL FUCKING MENTAL TORTURE YOU ALL ARE NOT FUNNY. COME UP WITH A DIFFERENT FUCKING JOKE PLEASE",
    "author": "Brabygg",
    "date": 1686229860.0
}

# Returned if invalid or non-existent data is loaded

failsafe_post = {
    "id": 0,
    "title": "Error",
    "body": "Could not get requested data. The post may have been deleted or simply never existed. Make sure the link isn't broken and try again.",
    "author": None,
    "date": None
}


# f = open("post_data.txt", "a")
# f.write(json.dumps(test_post_1) + "\n")
# f.write(json.dumps(test_post_2))
# f.close()


def load(post_id):
    post_id = int(post_id)

    f = open("post_data.txt", "r")
    data = json.dumps(failsafe_post)

    i = 0
    for x in f:
        if i == post_id:
            break
        i += 1
        data = x

    f.close()
    print(i)

    # Failsafe in case invalid data is loaded
    try:
        json.loads(data)
    except json.decoder.JSONDecodeError:
        data = json.dumps(failsafe_post)

    # Ditto for posts out of the range of the file, since they would otherwise return the most recent post added
    if post_id > json.loads(data)["id"]:
        data = json.dumps(failsafe_post)

    return data


def save(title, body, author):
    newData = {
        "id": None,
        "title": None,
        "body": None,
        "author": None,
        "date": None
    }
    f = open("post_data.txt", "r")

    # Roundabout way to read file line length
    i = 1
    for x in f:
        i += 1

    newData["id"] = i
    newData["title"] = title
    newData["body"] = body
    newData["author"] = author

    # Uses the current time for saving
    time = datetime.datetime.now(timezone.utc)
    newData["date"] = datetime.datetime.now(timezone.utc).timestamp()

    print(f"Saved entry '{title}' with ID {i} at {datetime.datetime.now()} UTC")
    f = open("post_data.txt", "a")
    f.write("\n" + json.dumps(newData))
    f.close()


# This loop is only used for local testing, and should be commented out in pushed builds
# If it isn't, tell Brabygg he's an idiot
#while True:
#    i = input("Save, load or exit? (s/l/e)")
#    if i == 'l':
#        i = input("ID to load: ")
#        print(load(int(i)))
#    elif i == 's':
#        t = input("Post title: ")
#        b = input("Post body: ")
#        a = input("Post author: ")
#        save(t, b, a)
#    elif i == 'e':
#        break
