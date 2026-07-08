"""
CGAO Core
"""

from .browser import Browser
from .config import (
    CONFIG,
    ROOT,
    DATA_DIR,
    DATABASE_DIR,
    RAW_DIR,
    PROCESSED_DIR,
    LOG_DIR,
    OUTPUT_DIR,
    STATE_DIR,
    HEADLESS,
    TIMEOUT,
    VIEWPORT,
    STATE_FILE,
    DATABASE_PATH,
    CSV_DIR,
    JSON_DIR,
    LOG_LEVEL,
    LOG_FILE,
)
from .logger import logger

__all__ = [

    # browser
    "Browser",

    # logger
    "logger",

    # config
    "CONFIG",
    "ROOT",
    "DATA_DIR",
    "DATABASE_DIR",
    "RAW_DIR",
    "PROCESSED_DIR",
    "LOG_DIR",
    "OUTPUT_DIR",
    "STATE_DIR",

    "HEADLESS",
    "TIMEOUT",
    "VIEWPORT",
    "STATE_FILE",

    "DATABASE_PATH",

    "CSV_DIR",
    "JSON_DIR",

    "LOG_LEVEL",
    "LOG_FILE",
]