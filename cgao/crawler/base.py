"""
Abstract base crawler.
"""

from abc import ABC
from abc import abstractmethod


class BaseCrawler(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def search(self, keyword: str):
        pass

    @abstractmethod
    def collect(self):
        pass

    @abstractmethod
    def export(self, path: str):
        pass