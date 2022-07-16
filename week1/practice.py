
def locate_card(cards, query):
    indices = []
    for idx, card in enumerate(cards):
        if card == query:
            indices.append(idx)

    if bool(indices):
        return indices
    return "The query was not found in the deck."



if __name__ == "__main__":
    cards = [13, 11, 7, 7, 4, 3, 1, 0]
    query = 7
    idx = locate_card(cards, query)
    print(f"The index is: {idx}")

    # representing test cases as a dictionary

    test = {
        "input" : {
            "cards" : [55, 43, 22, 19, 14, 3, 1, 0],
            "query": 14
        },
        "output": 4
    }

    test_result = locate_card(**test["input"]) # kwargs
    for result in test_result:
        print(result == test["output"])

