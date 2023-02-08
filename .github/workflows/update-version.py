import os
import re
from pathlib import Path


def main():
    tag = os.getenv('GITHUB_REF_NAME')
    if not tag:
        raise RuntimeError('tag not exists')
    if not tag.startswith('v'):
        raise ValueError(f'tag({tag}) not starts with "v"')
    print(f'tag: {tag}')
    init = Path('src/aligo/__init__.py')
    init.write_text(re.sub(
        r'^__version__ = [\'"]\d+\.\d+\.\d+[\'"]$',
        f"__version__ = '{tag[1:]}'",
        init.read_text(), flags=re.M
    ))


if __name__ == '__main__':
    main()
