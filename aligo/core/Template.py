"""..."""
from aligo.core.Config import V2_TEMPLATE_TEST
from aligo.request import TemplateRequest
from aligo.response import TemplateResponse
from .BaseAligo import BaseAligo


class Template(BaseAligo):
    """..."""

    def _core_template(self, body: TemplateRequest) -> TemplateResponse:
        """模板"""
        response = self._post(V2_TEMPLATE_TEST, body=body)
        return self._result(response, TemplateResponse, status_code=202)
