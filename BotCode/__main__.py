from bot import RogueOneBot

bot_count = 0


def new_bot(bot_count):
    bot_count += 1
    print("Spawned new bot: #{}".format(bot_count))
    try:
        bot = RogueOneBot()
        bot.run()
    except Exception as e:
        print(e)
        new_bot(bot_count)


if __name__ == '__main__':
    new_bot(bot_count)
