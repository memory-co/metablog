"""metablog insight"""


def register(sub):
    p = sub.add_parser("insight")
    p.set_defaults(func=run)


def run(args):
    raise NotImplementedError("metablog insight")
