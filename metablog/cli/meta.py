"""metablog meta"""


def register(sub):
    p = sub.add_parser("meta")
    p.set_defaults(func=run)


def run(args):
    raise NotImplementedError("metablog meta")
