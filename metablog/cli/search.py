"""metablog search"""


def register(sub):
    p = sub.add_parser("search")
    p.set_defaults(func=run)


def run(args):
    raise NotImplementedError("metablog search")
