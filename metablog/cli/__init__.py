"""metablog 命令行入口：每个子命令一个模块，各自提供 register(subparsers)。"""

import argparse

from metablog.cli import insight, meta, origin, post, publish, search, server

MODULES = [server, origin, post, insight, meta, search, publish]


def main(argv=None):
    parser = argparse.ArgumentParser(prog="metablog")
    sub = parser.add_subparsers(dest="command", required=True)
    for m in MODULES:
        m.register(sub)
    args = parser.parse_args(argv)
    return args.func(args)
