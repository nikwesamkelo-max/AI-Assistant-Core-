from memory import load_memory


def search_memories(query):
    memories = load_memory()
    results = []

    for memory in memories:
        if query.lower() in memory["user_message"].lower():
            results.append(memory)

    return results
