from typing_bot import TypingBot
import argparse


parser = argparse.ArgumentParser(description='Script that runs typing bot')
parser.add_argument('-r', '--repeat', help='specify how many times bot should repeat typing practice', type=int)
args = parser.parse_args()

if __name__ == '__main__':
    bot = TypingBot()
    bot.login()
    bot.go_to_practice()
    bot.change_settings()
    repeat = args.repeat if args.repeat else 10
    bot.practice_for_repetitions(practice_reps=repeat)
    bot.cleanup()
