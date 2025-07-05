import logging


file_handler = logging.FileHandler(f"{__name__}.log", mode='w')

def patch_logger(logger_: logging.Logger):
    logger_.handlers = []  # Clear any existing handlers
    logger_.addHandler(file_handler)
    # logger_.addHandler(console_handler)
    logger_.propagate = False
    logger_.setLevel(logging.INFO)
    return logger_