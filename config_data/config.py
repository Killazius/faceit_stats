from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_id: str

@dataclass
class Faceit:
    api_key: str

@dataclass
class Config:
    tg_bot: TgBot
    faceit: Faceit


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_id=env('ADMIN_ID'),
        ),
        faceit = Faceit(
            api_key=env('API_KEY')
        )
    )
