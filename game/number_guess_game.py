import random

def guess_the_number_game():
    """
    数字当てゲームを実行する関数です。
    """
    # 1. コンピューターが1から100までのランダムな整数を生成します。
    correct_answer = random.randint(1, 100)
    attempts = 0

    print("=== 数字当てゲーム ===")
    print("1から100までの数字を当ててください。")
    print("ゲームを終了したい場合は 'q' を入力してください。")
    print("======================")

    while True:
        # 2. ユーザーは数字を入力して予想します。
        user_input = input("あなたの予想を入力してください: ")

        # 5. ユーザーがゲームを終了したい場合は'q'を入力できるようにしてください。
        if user_input.lower() == 'q':
            print(f"ゲームを終了します。正解は {correct_answer} でした。")
            break

        try:
            guess = int(user_input)
            attempts += 1
        except ValueError:
            print("無効な入力です。1から100までの整数か、'q'を入力してください。")
            continue

        # 3. ユーザーの予想が正解するまで、コンピューターは「大きい」または「小さい」というヒントを提供します。
        if guess < correct_answer:
            print("ヒント: もっと大きいです。")
        elif guess > correct_answer:
            print("ヒント: もっと小さいです。")
        else:
            # 4. 正解したら、何回で当てたかを表示します。
            print(f"おめでとうございます！正解です！")
            print(f"正解するまでにかかった回数: {attempts}回")
            break

if __name__ == "__main__":
    guess_the_number_game()
