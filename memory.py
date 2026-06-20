import json

FILE_NAME = "memory.json"


def load_memory():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_memory(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def add_memory(user_message, assistant_reply):
    data = load_memory()

    memory = {
        "user_message": user_message,
        "assistant_reply": assistant_reply
    }

    data.append(memory)
    save_memory(data)
