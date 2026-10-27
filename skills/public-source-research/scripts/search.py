"""Infimeta public-source search client (Python 3, no dependencies).

Queries and optional purpose are retained privately for research for 90 days
(backups up to 7 extra days). Never send secrets or full conversations.
Use --test for demonstrations and integration checks, not organic demand.
"""
import argparse
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', help='A public-information search question')
    parser.add_argument('--sources', nargs='+', default=['crossref'],
                        choices=['crossref', 'hackernews', 'stackexchange',
                                 'wikipedia_en', 'wikipedia_zh'])
    parser.add_argument('--purpose', default='', help='Optional short task purpose')
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()
    payload = {'q': args.query, 'sources': args.sources, 'purpose': args.purpose}
    headers = {'Content-Type': 'application/json', 'User-Agent': 'InfimetaExample/1.0'}
    if args.test:
        headers['X-Research-Traffic'] = 'test'
    req = Request('https://infimeta.cn/api/search',
                  data=json.dumps(payload).encode('utf-8'), headers=headers)
    try:
        with urlopen(req, timeout=35) as response:
            result = json.load(response)
    except (HTTPError, URLError, TimeoutError) as error:
        print('Search failed: ' + str(error), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result.get('status') == 'unavailable' else 0


if __name__ == '__main__':
    sys.exit(main())
