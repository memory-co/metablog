"""metablog post"""


def register(sub):
    p = sub.add_parser("post")
    p.set_defaults(func=run)


def run(args):
    raise NotImplementedError("metablog post")
