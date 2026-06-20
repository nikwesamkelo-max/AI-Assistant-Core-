from memory import add_memory
from search import search_memories


def generate_response(user_input, memories):
    # Simple logic (we upgrade this later)
    
    if "hello" in user_input.lower():
        return "Hey! How can I help you today?"

    if "what do i like" in user_input.lower():
        if memories:
            return f"You previously said: {memories[0]['user_message']}"
        else:
            return "I don't know yet. Tell me something about yourself!"

    return "I hear you. Tell me more."


# ---------------- MAIN LOOP ----------------

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    # 1. SEARCH MEMORY FIRST
    memories = search_memories(user_input)

    # 2. GENERATE RESPONSE
    response = generate_response(user_input, memories)

    # 3. REPLY
    print("Assistant:", response)

    # 4. SAVE MEMORY
    add_memory(user_input, response)
