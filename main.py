import random
from art import logo
from art import vs
from game_data import data


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]

    description = account["description"]

    country = account["country"]

    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


def check_answer(answer, data_a, data_b):
    data_a_followers = data_a["follower_count"]

    data_b_followers = data_b["follower_count"]

    if data_a_followers > data_b_followers:
        return answer == "a"
    else:
        return answer == "b"


def play_game():
    print(logo)

    score = 0
    should_contuniue = True

    data_a = random.choice(data)
    print(data_a)
    while should_contuniue:
        data_b = random.choice(data)
        print(data_b)

        print(format_data(data_a))
        print(vs)
        print(format_data(data_b))

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        check_answers = check_answer(answer, data_a, data_b)
        if check_answers:
            score += 1
            data_a = data_b
            print(f"you are right. Your current score is {score}")
        else:
            should_contuniue = False
            print(f"that's wrong. Your final score is {score}")


play_game()
