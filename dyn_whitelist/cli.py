import argparse
import sys
from pathlib import Path

from . import __version__
from .check import check_rules

# import click
# @click.command()
# @click.option("--as-cowboy", "-c", is_flag=True, help="Greet as a cowboy.")
# @click.argument("name", default="world", required=False)


def main():
    """Manage firewall rules for a set of ip addresses and/or hostnames."""
    parser = argparse.ArgumentParser(
        # prog = 'letitdefault to basename "$0"',
        # formatter_class=argparse.RawDescriptionHelpFormatter,
        # epilog=textwrap.dedent('''\
        #   aditional information:
        #     Add any additional help text you like.
        #   ''')
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="count",
        dest="debug",
        default=0,
        help="increment debug level",
    )
    parser.add_argument(
        "-t",
        "--test",
        action="store_true",
        dest="test",
        default=False,
        help="sets test flag",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        dest="verbose",
        default=0,
        help="increment verbosity level",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="store_true",
        dest="version",
        default=False,
        help="show version and exit",
    )

    args = parser.parse_args()

    options = vars(args)
    if options["debug"] > 1:
        print(options)
        print(args)

    exit_code = 0
    if options["version"]:
        print(f"{Path(sys.argv[0]).name} Version: {__version__}")
        sys.exit(exit_code)

    exit_code = check_rules(options)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
