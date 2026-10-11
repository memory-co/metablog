"""CLI 公共件：服务地址、HTTP 客户端、输出。"""

import os

DEFAULT_URL = "http://127.0.0.1:8100"


def base_url() -> str:
    return os.environ.get("METABLOG_URL", DEFAULT_URL)
