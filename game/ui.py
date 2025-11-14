from .logic import NumberGuessGame

def start_console_game():
    """
    コンソールで数字当てゲームを実行する。
    """
    game = NumberGuessGame(1, 100)

    print("=== 数字当てゲーム ===")
    print(f"{game.min_val}から{game.max_val}までの数字を当ててください。")
    print("ゲームを終了したい場合は 'q' を入力してください。")
    print("======================")

    while not game.is_finished:
        user_input = input("あなたの予想を入力してください: ")

        if user_input.lower() == 'q':
            print(f"ゲームを終了します。正解は {game.correct_answer} でした。")
            break

        try:
            guess_num = int(user_input)
        except ValueError:
            print(f"無効な入力です。{game.min_val}から{game.max_val}までの整数か、'q'を入力してください。")
            continue

        result = game.guess(guess_num)

        if result == "low":
            print("ヒント: もっと大きいです。")
        elif result == "high":
            print("ヒント: もっと小さいです。")
        elif result == "correct":
            print(f"おめでとうございます！正解です！")
            print(f"正解するまでにかかった回数: {game.attempts}回")

    print("ゲームをプレイしていただき、ありがとうございました。")