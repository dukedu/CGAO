from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class BaseCollector(ABC):

    def __init__(self, page):

        self.page = page

    @abstractmethod
    def collect(self, *args, **kwargs):
        ...