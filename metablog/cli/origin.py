"""metablog origin"""


def register(sub):
    p = sub.add_parser("origin")
    p.set_defaults(func=run)


def run(args):
    raise NotImplementedError("metablog origin")
