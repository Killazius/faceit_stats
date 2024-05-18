def next_level(level: int, elo: int) -> str:

    elo_thresholds = [500, 750, 900, 1050, 1200, 1350, 1530, 1750, 2000]

    next_threshold = next((threshold for threshold in elo_thresholds if elo <= threshold), None)

    if next_threshold is not None:
        need_elo = next_threshold + 1 - elo
        return f'До следующего уровня <b>({level+1})</b> осталось <b>{need_elo}</b> elo'
    else:
        return 'Игрок достиг максимального level на FACEIT'



