def financial_chatbot(user_query):

    responses = {
        "what is the total revenue?":
            "The total revenue is $22 billion.",

        "what is the net income?":
            "The net income is $5 billion.",

        "how has net income changed over the last year?":
            "Net income increased by 10% compared to the previous year.",

        "what is the revenue growth?":
            "Revenue grew by 8% over the previous year.",

        "what are the total assets?":
            "The company's total assets are valued at $50 billion."
    }

    return responses.get(
        user_query.lower(),
        "Sorry, I can only answer predefined financial questions."
    )


print("=== Financial Analysis Chatbot ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = financial_chatbot(user_input)
    print("Chatbot:", response)