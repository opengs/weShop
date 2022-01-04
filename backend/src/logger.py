from logging import getLogger, Logger, StreamHandler, Formatter, FileHandler

from .config import DEFAULT_LOG_LEVEL, LOG_FILE_PATH

#_formatter = Formatter("%(levelname)s:%(asctime)s:%(name)s:%(message)s")
_formatter = Formatter("%(levelname)s:%(process)d:%(name)s:%(message)s")

_stream_handler = StreamHandler()
_stream_handler.setLevel(DEFAULT_LOG_LEVEL)
_stream_handler.setFormatter(_formatter)

_file_hadler = None
if LOG_FILE_PATH != None:
    _file_hadler = FileHandler(LOG_FILE_PATH)
    _file_hadler.setLevel(DEFAULT_LOG_LEVEL)
    _file_hadler.setFormatter(_formatter)


def create_logger(name: str) -> Logger:
    logger = getLogger(name)

    logger.addHandler(_stream_handler)
    if _file_hadler != None:
        logger.addHandler(_file_hadler)

    logger.setLevel(DEFAULT_LOG_LEVEL)

    return logger