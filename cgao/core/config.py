"""
CGAO Core Configuration
"""

from __future__ import annotations

from pathlib import Path

import yaml

# ==========================================================
# Project Paths
# ==========================================================

ROOT = Path(__file__).resolve().parents[2]

CONFIG_DIR = ROOT / "config"

DATA_DIR = ROOT / "data"

DATABASE_DIR = DATA_DIR / "database"

RAW_DIR = DATA_DIR / "raw"

PROCESSED_DIR = DATA_DIR / "processed"

LOG_DIR = ROOT / "logs"

OUTPUT_DIR = ROOT / "outputs"

STATE_DIR = ROOT / "storage" / "state"

# ==========================================================
# Create Directories
# ==========================================================

for path in (

    DATA_DIR,

    DATABASE_DIR,

    RAW_DIR,

    PROCESSED_DIR,

    LOG_DIR,

    OUTPUT_DIR,

    STATE_DIR,

):

    path.mkdir(

        parents=True,

        exist_ok=True,

    )

# ==========================================================
# Load YAML
# ==========================================================

CONFIG_FILE = CONFIG_DIR / "config.yaml"

if CONFIG_FILE.exists():

    with open(

        CONFIG_FILE,

        "r",

        encoding="utf-8",

    ) as f:

        CONFIG = yaml.safe_load(f)

else:

    CONFIG = {}

# ==========================================================
# Browser
# ==========================================================

_browser = CONFIG.get(

    "browser",

    {},

)

HEADLESS = _browser.get(

    "headless",

    False,

)

TIMEOUT = _browser.get(

    "timeout",

    30000,

)

VIEWPORT = _browser.get(

    "viewport",

    {

        "width": 1440,

        "height": 900,

    },

)

STATE_FILE = ROOT / _browser.get(

    "state_file",

    "storage/state/state.json",

)

# ==========================================================
# Database
# ==========================================================

_database = CONFIG.get(

    "database",

    {},

)

DATABASE_PATH = ROOT / _database.get(

    "path",

    "data/database/cgao.db",

)

# ==========================================================
# Export
# ==========================================================

_export = CONFIG.get(

    "export",

    {},

)

CSV_DIR = ROOT / _export.get(

    "csv",

    "data/raw",

)

JSON_DIR = ROOT / _export.get(

    "json",

    "data/raw",

)

# ==========================================================
# Logger
# ==========================================================

_log = CONFIG.get(

    "log",

    {},

)

LOG_LEVEL = _log.get(

    "level",

    "INFO",

)

LOG_FILE = ROOT / _log.get(

    "path",

    "logs/cgao.log",

)