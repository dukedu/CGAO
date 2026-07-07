"""
Global configuration for CGAO.
"""

from pathlib import Path

# -------------------------------------------------------------------
# Project Path
# -------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

LOG_DIR = PROJECT_ROOT / "logs"

OUTPUT_DIR = PROJECT_ROOT / "outputs"

# -------------------------------------------------------------------
# Browser
# -------------------------------------------------------------------

HEADLESS = False

TIMEOUT = 30000

VIEWPORT = {
    "width": 1440,
    "height": 900,
}