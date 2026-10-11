"""metablog publish"""


def register(sub):
    p = sub.add_parser("publish")
    p.set_defaults(func=run)


def run(args):
    raise NotImplementedError("metablog publish")
