from bot import DeveloperNotDevloper
import time

bot_count = 0
wait_time = 30
maximum_tries = 100


def new_bot(bot_count):
    bot_count += 1
    print("Spawned new bot: #{}".format(bot_count))
    
    # Pokemon Exception Handling - Gotta catch 'em all!
    try:
        bot = DeveloperNotDevloper()
        bot.run()
    except Exception as e:
        print(e)
        time.sleep(wait_time)
        if bot_count < maximum_tries:
            new_bot(bot_count)


if __name__ == '__main__':
    new_bot(bot_count)

