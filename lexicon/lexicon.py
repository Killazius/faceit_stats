LEXICON: dict[str, str] = {
    '/help': '@killazius - пиши скорее, если <b>ты нашел баг/недочет в боте</b>, '
             'либо просто хочешь подкинуть мне идею',
    '/start': 'Привет! Тебя приветствует <i>FACEIT STATS BOT</i>\n'
              'Я бот, который поможет тебе отслеживать твою статистику.\n'
              '<b>Жду твоих команд!</b>',
    '/info': 'Этот бот создан для того, чтобы отслежить статистику пользователей на <b>FACEIT</b>\n'
             'В данный момент бот имеет лишь 1 функцию, чтобы ее посмотреть введите:\n'
             '<b>/stats nickname</b>\n'
             'Статистика береться лишь по игре CS2 на платформе FACEIT,если пользователь в нее не играл, '
             'то статистику бот не выведет\n',
    '/stats': 'Статистика <b>{nickname}</b> в игре Counter Strike 2\n'
              '🏆LEVEL - {level}\n'
              '🎯ELO - {elo}\n'
              '{next_level}\n'
              'Статистика за последние {matches} игр:\n'
              '📊Winrate - {winrate}% (🟩{win} - 🟥{lose})\n'
              'K/D Ratio - {kd}\n'
              'K/R Ratio - {kr}\n'
              '💀Headshots - {hs}%',
    'error': 'Произошла ошибка, вы что-то делаете не так.\n'
             'Посмотреть команды бота - /info, написать разработчику /help',

    'link_page': 'FACEIT',

    'link_steam': 'STEAM',

    'last_game': 'Последняя игра',

    'last_game_stats': '🌅MAP {map} |\t {result}\n'
                       'Score {score}\n\n'
                       '🧠<b>{nickname}</b> stats:\n'
                       '🏹K/D/A - {kda}\n'
                       '⭐️MVPs - {mvp}\n\n'
                       'KD - {kd}\n'
                       'KR - {kr}\n'
                       '💀Headshots - {hs}%'
}

LEXICON_COMMANDS: dict[str, str] = {
    '/help': 'Написать разработчику',
    '/stats': 'Посмотреть статистику игрока в игре CS2. Пример: /stats donk666',
    '/info': 'Информация о боте.'

}

LEXICON_MAPS_PHOTO: dict[str, str] = {
    'de_dust2': 'https://assets.faceit-cdn.net/third_party/games/ce652bd4-0abb-4c90-9936-1133965ca38b/assets/votables/7c17caa9-64a6-4496-8a0b-885e0f038d79_1695819126962.jpeg',
    'de_mirage': 'https://assets.faceit-cdn.net/third_party/games/ce652bd4-0abb-4c90-9936-1133965ca38b/assets/votables/7fb7d725-e44d-4e3c-b557-e1d19b260ab8_1695819144685.jpeg',
    'de_vertigo': 'https://assets.faceit-cdn.net/third_party/games/ce652bd4-0abb-4c90-9936-1133965ca38b/assets/votables/3bf25224-baee-44c2-bcd4-f1f72d0bbc76_1695819180008.jpeg',
    'de_nuke': 'https://assets.faceit-cdn.net/third_party/games/ce652bd4-0abb-4c90-9936-1133965ca38b/assets/votables/7197a969-81e4-4fef-8764-55f46c7cec6e_1695819158849.jpeg',
    'de_inferno': 'https://assets.faceit-cdn.net/third_party/games/ce652bd4-0abb-4c90-9936-1133965ca38b/assets/votables/993380de-bb5b-4aa1-ada9-a0c1741dc475_1695819220797.jpeg',
    'de_anubis': 'https://assets.faceit-cdn.net/third_party/games/ce652bd4-0abb-4c90-9936-1133965ca38b/assets/votables/31f01daf-e531-43cf-b949-c094ebc9b3ea_1695819235255.jpeg',
    'de_ancient': 'https://assets.faceit-cdn.net/third_party/games/ce652bd4-0abb-4c90-9936-1133965ca38b/assets/votables/5b844241-5b15-45bf-a304-ad6df63b5ce5_1695819190976.jpeg'


}
