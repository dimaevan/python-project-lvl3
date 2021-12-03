#!usr/bin/env python3
from page_loader.downloader import download
import argparse
import sys
import os


def main():
    first_path = os.getcwd()
    parser = argparse.ArgumentParser(usage='page-loader [option] <url>',
                                     description='Page-loader from url',
                                     add_help=False)
    parser.add_argument('-V', '--version', help="output the version number",
                        metavar='', default='0.2')
    parser.add_argument('-o', '--output', help="output dir (default: '/app')",
                        metavar='', dest='output', default=os.getcwd())
    parser.add_argument('-h', '--help', help="display help for command",
                        action='help')
    parser.add_argument('url', type=str, help=argparse.SUPPRESS)
    args = parser.parse_args()
    result = download(args.url, args.output)
    if not result:
        sys.exit(1)
    print(result)
    os.chdir(first_path)
    sys.exit(0)


if __name__ == "__main__":
    main()
