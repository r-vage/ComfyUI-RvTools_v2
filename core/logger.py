# RvTools Logger - Centralized logging with log level filtering.
#
# Includes:
# - cstr class for colored terminal output
# - RvToolsLogger for filtered logging
#
# Usage:
#     from ..core.logger import log, cstr
#     
#     log.debug("MyModule", "Debug message")
#     log.info("MyModule", "Info message")  
#     log.warning("MyModule", "Warning message")
#     log.error("MyModule", "Error message")  # Always shown
#     log.msg("MyModule", "Regular message")  # Always shown
#
# Log levels (configured in rvtools_config.json):
#     error   - Only errors shown
#     warning - Errors + warnings
#     info    - Errors + warnings + info
#     debug   - Everything

import json
from pathlib import Path


# =============================================================================
# cstr - Colored String Class
# =============================================================================

class cstr(str):
    # String subclass with ANSI color support for terminal output.
    
    class color:
        END = '\33[0m'
        BOLD = '\33[1m'
        ITALIC = '\33[3m'
        UNDERLINE = '\33[4m'
        BLINK = '\33[5m'
        BLINK2 = '\33[6m'
        SELECTED = '\33[7m'

        BLACK = '\33[30m'
        RED = '\33[31m'
        GREEN = '\33[32m'
        YELLOW = '\33[33m'
        BLUE = '\33[34m'
        VIOLET = '\33[35m'
        BEIGE = '\33[36m'
        WHITE = '\33[37m'

        BLACKBG = '\33[40m'
        REDBG = '\33[41m'
        GREENBG = '\33[42m'
        YELLOWBG = '\33[43m'
        BLUEBG = '\33[44m'
        VIOLETBG = '\33[45m'
        BEIGEBG = '\33[46m'
        WHITEBG = '\33[47m'

        GREY = '\33[90m'
        LIGHTRED = '\33[91m'
        LIGHTGREEN = '\33[92m'
        LIGHTYELLOW = '\33[93m'
        LIGHTBLUE = '\33[94m'
        LIGHTVIOLET = '\33[95m'
        LIGHTBEIGE = '\33[96m'
        LIGHTWHITE = '\33[97m'

        GREYBG = '\33[100m'
        LIGHTREDBG = '\33[101m'
        LIGHTGREENBG = '\33[102m'
        LIGHTYELLOWBG = '\33[103m'
        LIGHTBLUEBG = '\33[104m'
        LIGHTVIOLETBG = '\33[105m'
        LIGHTBEIGEBG = '\33[106m'
        LIGHTWHITEBG = '\33[107m'

        @staticmethod
        def add_code(name, code):
            # Add a custom color code at runtime.
            if not hasattr(cstr.color, name.upper()):
                setattr(cstr.color, name.upper(), code)
            else:
                raise ValueError(f"'cstr' object already contains a code with the name '{name}'.")

    def __new__(cls, text):
        return super().__new__(cls, text)

    def __getattr__(self, attr):
        # Support attribute-based colorization.
        if attr.lower().startswith("_cstr"):
            code = getattr(self.color, attr.upper().lstrip("_cstr"))
            modified_text = self.replace(f"__{attr[1:]}__", f"{code}")
            return cstr(modified_text)
        elif attr.upper() in dir(self.color):
            code = getattr(self.color, attr.upper())
            modified_text = f"{code}{self}{self.color.END}"
            return cstr(modified_text)
        elif attr.lower() in dir(cstr):
            return getattr(cstr, attr.lower())
        else:
            raise AttributeError(f"'cstr' object has no attribute '{attr}'")

    def print(self, **kwargs):
        print(self, **kwargs)


# =============================================================================
# Log Level Configuration
# =============================================================================

# Path to RvTools node directory
NODE_DIR = Path(__file__).resolve().parent.parent

# Log level hierarchy: error < warning < info < debug
_LOG_LEVELS = {"error": 0, "warning": 1, "info": 2, "debug": 3}


def _get_config_value(key: str, default=None):
    # Get a value from rvtools_config.json.
    config_path = NODE_DIR / "rvtools_config.json"
    if not config_path.exists():
        return default
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            return config.get(key, default)
    except Exception:
        return default


def get_log_level() -> str:
    # Get current log level from config (error, warning, info, debug).
    return _get_config_value("log_level", "warning").lower()


def _get_log_level_value() -> int:
    # Get numeric log level value for comparison.
    return _LOG_LEVELS.get(get_log_level(), 1)


def is_error_enabled() -> bool:
    # Check if error logging is enabled (always True - errors are always shown).
    return True


def is_warning_enabled() -> bool:
    # Check if warning logging is enabled (warning, info, or debug level).
    return _get_log_level_value() >= _LOG_LEVELS["warning"]


def is_info_enabled() -> bool:
    # Check if info logging is enabled (info or debug level).
    return _get_log_level_value() >= _LOG_LEVELS["info"]


def is_debug_enabled() -> bool:
    # Check if debug logging is enabled via log_level config.
    return _get_log_level_value() >= _LOG_LEVELS["debug"]


class RvToolsLogger:
    # Centralized logger with log level filtering.
    
    def _reload_config(self):
        # Force reload of log level from config file (called when config changes).
        pass  # Log level is read dynamically via get_log_level()
    
    def debug(self, prefix: str, message: str):
        # Print debug message only when log_level is 'debug'.
        if is_debug_enabled():
            cstr(f"[DEBUG {prefix}] {message}").lightbeige.print()
    
    def info(self, prefix: str, message: str):
        # Print info message only when log_level is 'info' or higher.
        if is_info_enabled():
            cstr(f"[{prefix}] {message}").lightgreen.print()
    
    def warning(self, prefix: str, message: str):
        # Print warning message only when log_level is 'warning' or higher.
        if is_warning_enabled():
            cstr(f"[WARNING {prefix}] {message}").lightyellow.print()
    
    def error(self, prefix: str, message: str):
        # Print error message (always shown).
        cstr(f"[ERROR {prefix}] {message}").red.print()
    
    def msg(self, prefix: str, message: str):
        # Print regular message (always shown, not filtered by log level).
        cstr(f"[{prefix}] {message}").lightgreen.print()


# Singleton instance
log = RvToolsLogger()
