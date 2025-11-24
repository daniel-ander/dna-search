# Debugging utilities for the application

def log_debug_info(message: str) -> None:
    """
    Logs debug information if DEBUG_MODE is enabled.

    :param message: The debug message to log
    """
    from utils.global_variables import DEBUG_MODE
    if DEBUG_MODE:
        print(f"[DEBUG]: {message}")

def log_verbose_info(message: str) -> None:
    """
    Logs verbose information if VERBOSE_LOGGING is enabled.

    :param message: The verbose message to log
    """
    from utils.global_variables import VERBOSE_LOGGING
    if VERBOSE_LOGGING:
        print(f"[VERBOSE]: {message}")


