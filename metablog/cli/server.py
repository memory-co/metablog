"""metablog server"""


def register(sub):
    p = sub.add_parser("server")
    p.set_defaults(func=run)


def run(args):
    raise NotImplementedError("metablog server")
