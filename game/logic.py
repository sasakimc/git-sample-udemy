import random

class NumberGuessGame:
    """
    数字当てゲームのコアロジックを管理するクラス。
    状態管理と判定のみを行い、UI（表示や入力）は分離する。
    """
    def __init__(self, min_val=1, max_val=100):
        """
        ゲームを初期化し、正解の数字を生成する。
        """
        self.min_val = min_val
        self.max_val = max_val
        self.correct_answer = random.randint(self.min_val, self.max_val)
        self.attempts = 0
        self.is_finished = False

    def guess(self, number):
        """
        ユーザーの予想を判定し、結果を返す。

        Args:
            number (int): ユーザーが予想した数字。

        Returns:
            str: 'high', 'low', 'correct' のいずれかの結果文字列。
        """
        if self.is_finished:
            return "finished"

        self.attempts += 1

        if number < self.correct_answer:
            return "low"
        elif number > self.correct_answer:
            return "high"
        else:
            self.is_finished = True
            return "correct"