# TIC-TAC-TOE WITH MINIMAX (HUMAN vs AI)


board = [' ' for _ in range(9)]

stats = {
    "Human Wins": 0,
    "AI Wins": 0,
    "Draws": 0
}


def show_positions():
    print("Board positions:")
    print("0 | 1 | 2")
    print("--+---+--")
    print("3 | 4 | 5")
    print("--+---+--")
    print("6 | 7 | 8\n")


def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
    print()


def check_winner(player):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def is_draw():
    return ' ' not in board


def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

def ai_move():
    best_score = -float('inf')
    move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i

    board[move] = 'O'


def play_game():
    print("\nTic-Tac-Toe | You = X | AI = O")
    show_positions()
    print_board()

    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move < 0 or move > 8 or board[move] != ' ':
                print("❌ Invalid move. Try again.")
                continue
        except ValueError:
            print("❌ Please enter a number between 0 and 8.")
            continue

        board[move] = 'X'
        print_board()

        if check_winner('X'):
            print("🎉 You Win!")
            stats["Human Wins"] += 1
            break

        if is_draw():
            print("😐 Draw!")
            stats["Draws"] += 1
            break

        ai_move()
        print("🤖 AI played:")
        print_board()

        if check_winner('O'):
            print("🤖 AI Wins!")
            stats["AI Wins"] += 1
            break

        if is_draw():
            print("😐 Draw!")
            stats["Draws"] += 1
            break

while True:
    board = [' ' for _ in range(9)]
    play_game()

    print("\n📊 Scoreboard")
    for k, v in stats.items():
        print(f"{k}: {v}")

    again = input("\nPlay again? (y/n): ")
    if again.lower() != 'y':
        print("Thanks for playing 👋")
        break
