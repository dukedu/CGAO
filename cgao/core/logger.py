"""
CGAO Logger
"""

from __future__ import annotations

import sys

from loguru import logger

from cgao.core.config import LOG_FILE, LOG_LEVEL


# ==========================================================
# Init
# ==========================================================

LOG_FILE.parent.mkdir(

    parents=True,

    exist_ok=True,

)

logger.remove()


# ==========================================================
# Console
# ==========================================================

logger.add(

    sys.stdout,

    level=LOG_LEVEL,

    colorize=True,

    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:"
        "<cyan>{function}</cyan>:"
        "<cyan>{line}</cyan> - "
        "<level>{message}</level>"
    ),

)


# ==========================================================
# File
# ==========================================================

logger.add(

    LOG_FILE,

    level=LOG_LEVEL,

    rotation="10 MB",

    retention="30 days",

    encoding="utf-8",

    enqueue=True,

    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level: <8} | "
        "{name}:{function}:{line} - "
        "{message}"
    ),

)


# ==========================================================
# Export
# ==========================================================

__all__ = [

    "logger",

]