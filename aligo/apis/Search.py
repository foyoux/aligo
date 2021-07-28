"""..."""
from typing import Iterator

from aligo.core import *
from aligo.request import *
from aligo.types import *


class Search(Core):
    """..."""

    def search_file(self, name: str = None, category: SearchCategory = None, drive_id: str = None,
                    body: SearchFileRequest = None, **kwargs) -> Iterator[BaseFile]:
        """..."""
        if body is None:
            query = f'name match "{name}"'
            if category is not None:
                query += f' and category = "{category}"'
            body = SearchFileRequest(query=query, **kwargs)
        result = super(Search, self).search_file(body)
        return [i for i in result]
