from config.config import AppConfig
from src.apis import app
from uvicorn import Server, Config
from src.services import create_tables


if __name__ == '__main__':
    config = AppConfig()
    server = Server(
        Config(app=app, host=config.APP_HOST, port=config.APP_PORT))
    server.run()
