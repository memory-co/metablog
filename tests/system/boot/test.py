"""system/boot：服务能起来，配置从环境变量来。见同目录 README.md。"""


def test_app_boots(client):
    assert client.get("/openapi.json").status_code == 200


def test_home_comes_from_env(client, home):
    config = client.app.state.config
    assert config.home == home
    assert config.metas_dir == home / "metas"
    assert config.layers_dir == home / "layers"
    assert config.site_dir == home / "site"
