"""create_app(config)：装配 services，挂 controllers。"""

from fastapi import FastAPI

from metablog.backend.config import Config


def create_app(config: Config | None = None) -> FastAPI:
    config = config or Config.from_env()
    app = FastAPI(title="metablog")
    app.state.config = config
    # TODO: 装配 MetasService / PostService / InsightService / SearchService / PublishService，挂 controllers
    return app
