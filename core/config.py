import os
import logging

CONFIG = {
    "loglevel": int(os.environ.get("RVTOOLS_LOGLEVEL", logging.INFO)),
    "indent": int(os.environ.get("RVTOOLS_INDENT", 2))
}
