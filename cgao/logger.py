"""
Centralized logger.
"""

from pathlib import Path

from loguru import logger

from cgao.config import LOG_DIR

LOG_DIR.mkdir(exist_ok=True)

logger.remove()

logger.add(
    LOG_DIR / "cgao.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
)

logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
)

__all__ = ["logger"]