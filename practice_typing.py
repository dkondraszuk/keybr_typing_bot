from typing_bot import TypingBot

if __name__ == '__main__':
    bot = TypingBot()
    bot.login()
    bot.go_to_practice()
    bot.change_settings()
    bot.practice_for_repetitions(practice_reps=15)
    bot.cleanup()
