N = int(input())

def check_game():
    history = {}
    player = 1
    previous_word = input()
    history[previous_word] = True

    for _ in range(N-1):
        word = input()
        if history.get(word) is not None:
            return f"Player {player + 1} lost"
        if word[0] != previous_word[-1]:
            return f"Player {player + 1} lost"
        previous_word = word
        history[word] = True
        player = (player + 1) % 2
    return "Fair game"

print(check_game())
