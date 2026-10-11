"""Config：全部来自环境变量。"""

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:
    home: Path
    author: str
    email: str

    @classmethod
    def from_env(cls) -> "Config":
        return cls(
            home=Path(os.environ.get("METABLOG_HOME", Path.home() / ".metablog")),
            author=os.environ.get("METABLOG_AUTHOR", "metablog"),
            email=os.environ.get("METABLOG_EMAIL", "metablog@localhost"),
        )

    @property
    def metas_dir(self) -> Path:
        return self.home / "metas"

    @property
    def layers_dir(self) -> Path:
        return self.home / "layers"

    @property
    def site_dir(self) -> Path:
        return self.home / "site"
