"""..."""
from typing import Iterator

from aligo.core import *
from aligo.core.Config import *
from aligo.request import *
from aligo.response import *
from aligo.types import *


class Search(BaseAligo):
    """..."""

    def _core_search_files(self, body: SearchFileRequest) -> Iterator[BaseFile]:
        """
        关于 query 的语法, 参考下段代码
        {
            key: "getPDSSearchQuery", value: function () {
                var n = ['name match "'.concat(this.queryToSearch, '"')];
                return this.filter && ("folder" === this.filter ? n.push('type = "'.concat(this.filter, '"')) : n.push('category = "'.concat(this.filter, '"'))), n.join(" and ")
            }
        }
        eg: 'name match "epub"'
        eg: 'name match "epub" and category = "image"'
        category : BaseFileCategory
        """
        yield from self._list_file(V2_FILE_SEARCH, body, SearchFileResponse)

    def _core_search_aims(self, body: AimSearchRequest) -> Iterator[BaseFile]:
        """
        {
          "drive_id": "1067819",
          "limit": 20,
          "marker": "",
          "order_by": "image_time DESC,last_access_at DESC,updated_at DESC",
          "query": "keywords ='画画' and type = 'file' and category = 'image' and status = 'available' and hidden = false and status = 'available' and hidden = false",
          "return_total_count": true
        }
        """
        yield from self._list_file(V2_AIMS_SEARCH, body, AimSearchResponse)
