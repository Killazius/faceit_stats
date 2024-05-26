LEXICON: dict[str, str] = {
    '/help': '@killazius - пиши скорее, если <b>ты нашел баг/недочет в боте</b>, '
             'либо просто хочешь подкинуть мне идею',
    '/start': 'Привет! Тебя приветствует <i>FACEIT STATS BOT</i>\n'
              'Я бот, который поможет тебе отслеживать твою статистику.\n'
              '<b>/stats &lt;nickname&gt;</b>\n',
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

    '/top': 'Хотите узнать, кто входит в топ-10 лучших игроков?\n'
            'Просто выберите свой любимый регион и окунитесь в мир соревнований!\n'
            'Нажмите на кнопку с регионом, который вас интересует, чтобы увидеть лучших из лучших!',
    'error': 'Произошла ошибка, вы что-то делаете не так.\n'
             'Посмотреть команды бота - /info, написать разработчику /help',

    'error_no_matches': 'Извини, но я не могу собрать статистику, ведь ты не сыграл ни одной игры на FACEIT',

    'no_user': 'Такого игрока не существует',

    'win': '🟩WIN',
    'lose': '🟥LOSE',

    'link_page': 'FACEIT',

    'link_steam': 'STEAM',

    'link_lobby': 'LOBBY',

    'avatar_faceit': 'https://corporate.faceit.com/wp-content/uploads/logo-full-preview-2.png',

    'last_game': 'Последняя игра',

    'last_game_stats': '🌅MAP {Map} |\t {Result}\n'
                       'Score {Score}\n\n'
                       '🧠<b>{Nickname}</b> stats:\n'
                       '🏹K/D/A - {kda}\n'
                       '⭐️MVPs - {MVPs}\n\n'
                       'KD - {K/D Ratio}\n'
                       'KR - {K/R Ratio}\n'
                       '💀Headshots - {Headshots %}%\n'
}

LEXICON_COMMANDS: dict[str, str] = {
    '/stats': 'Посмотреть статистику игрока в игре CS2. Пример: /stats donk666',
    '/top': 'Посмотреть топ 10 игроков разных регионов',
    '/info': 'Информация о боте.',
    '/help': 'Написать разработчику'

}

link_begin = 'https://assets.faceit-cdn.net/third_party/games/ce652bd4-0abb-4c90-9936-1133965ca38b/assets/votables/'
LEXICON_MAPS_PHOTO: dict[str, str] = {
    'de_dust2': link_begin + '7c17caa9-64a6-4496-8a0b-885e0f038d79_1695819126962.jpeg',
    'de_mirage': link_begin + '7fb7d725-e44d-4e3c-b557-e1d19b260ab8_1695819144685.jpeg',
    'de_vertigo': link_begin + '3bf25224-baee-44c2-bcd4-f1f72d0bbc76_1695819180008.jpeg',
    'de_nuke': link_begin + '7197a969-81e4-4fef-8764-55f46c7cec6e_1695819158849.jpeg',
    'de_inferno': link_begin + '993380de-bb5b-4aa1-ada9-a0c1741dc475_1695819220797.jpeg',
    'de_anubis': link_begin + '31f01daf-e531-43cf-b949-c094ebc9b3ea_1695819235255.jpeg',
    'de_ancient': link_begin + '5b844241-5b15-45bf-a304-ad6df63b5ce5_1695819190976.jpeg'


}

LEXICON_REGIONS: dict[str:str] = {
    'EU': '🇪🇺 EU',
    'NA': '🇺🇸 NA',
    'SA': '🇧🇷 SA',
    'SEA': '🌍 SEA',
    'OCE': '🌐 OCE',
}
