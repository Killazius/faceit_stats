from lexicon.lexicon import LEXICON

def next_level(level: int, elo: int) -> str:

    elo_thresholds = [500, 750, 900, 1050, 1200, 1350, 1530, 1750, 2000]

    next_threshold = next((threshold for threshold in elo_thresholds if elo <= threshold), None)

    if next_threshold is not None:
        need_elo = next_threshold + 1 - elo
        return f'До следующего уровня <b>({level+1})</b> осталось <b>{need_elo}</b> elo'
    else:
        return 'Игрок достиг максимального level на FACEIT'


def get_player_stats(response_stats) -> dict[str:str]:
    stats = {
        'kr': 0,
        'kd': 0,
        'hs': 0,
        'win': 0,
        'matches': 0,
        'lose': 0
    }
    for match_info in response_stats['items']:
        match = match_info['stats']
        if match['Game Mode'] == '5v5':
            if match['Result'] == '1':
                stats['win'] += 1
            stats['matches'] += 1
            stats['kr'] += float(match['K/R Ratio'])
            stats['kd'] += float(match['K/D Ratio'])
            stats['hs'] += int(match['Headshots %'])
    if stats['matches'] != 0:
        stats['winrate'] = int(stats['win'] / stats['matches'] * 100)
        stats['kr'] = round(stats['kr'] / stats['matches'], 2)
        stats['kd'] = round(stats['kd'] / stats['matches'], 2)
        stats['hs'] = int(stats['hs'] / stats['matches'])
        stats['lose'] = stats['matches'] - stats['win']
    return stats

def get_lastgame_stats(last_game) -> dict[str:str]:
    specifications = ['Map', 'Result', 'Score', 'Nickname', 'Kills', 'Deaths', 'Assists', 'MVPs', 'K/D Ratio', 'K/R Ratio',
         'Headshots %']
    stats = {
        "kda": last_game['Kills'] + '/' + last_game['Deaths'] + '/' + last_game['Assists'],
    }

    for spec in specifications:
        if spec not in ['Kills','Deaths','Assists']:
            stats[spec] = last_game[spec]

    stats["Result"] = LEXICON['win'] if stats["Result"] == '1' else LEXICON['lose']
    return stats






