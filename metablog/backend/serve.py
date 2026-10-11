"""uvicorn 入口：metablog server start 调它。"""

import uvicorn

from metablog.backend.main import create_app


def run(host: str = "127.0.0.1", port: int = 8100):
    uvicorn.run(create_app(), host=host, port=port)
