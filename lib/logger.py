""" Logger Utilities

Basic logger setup utilities to create file rotation,
console handlers, etc.
"""
import os
import logging
from logging.handlers import RotatingFileHandler

LOG_LEVEL = logging.INFO
FILE_MODE='a'
FORMAT = "%(asctime)s - %(name)s - [%(levelname)s] - %(message)s"
CONSOLE_FORMAT = "%(asctime)s - [%(levelname)s] - %(message)s"
DEFAULT_LOGGER_NAME=''
MAX_BYTES=1000000
BACKUP_COUNT=10
DATE_FORMAT = '%Y-%m-%dT%H:%M:%S'
CONSOLE_DATE_FORMAT = '%m-%d-%y %H:%M:%S'

def init_basic_logger(filename, level=LOG_LEVEL, format=FORMAT, filemode=FILE_MODE, datefmt=DATE_FORMAT, **kw):
    """ Create basic Logger
    :param filename: log file name
    :param level: log level, default is LOG_LEVEL
    :param format: log formatter, default is FORMAT
    :param filemode: file mode, default is FILE_MODE
    :param datefmt: date time format, default is DATE_FORMAT
    :param **kw: all remaing args passed to basic_config
    """
    log_dir = os.path.dirname(filename)
    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)
    logging.basicConfig(
        filename=filename,
        filemode=filemode,
        level=level,
        format=format,
        datefmt=datefmt,

        **kw
    )

def add_console_handler(console_format=CONSOLE_FORMAT, datefmt=CONSOLE_DATE_FORMAT, logger_name=DEFAULT_LOGGER_NAME):
    """ Add Console Handler
    :param format: console format template, default is CONSOLE_FORMAT
    :param datefmt: console date time format, default is CONSOLE_DATE_FORMAT
    :param logger_name: logger name, the default is DEFAULT_LOGGER_NAME
    """
    console = logging.StreamHandler()
    formatter = logging.Formatter(console_format, datefmt)
    console.setFormatter(formatter)
    logging.getLogger(logger_name).addHandler(console)

def add_file_rotation(filename, max_bytes=MAX_BYTES, backup_count=BACKUP_COUNT, logger_name=DEFAULT_LOGGER_NAME):
    """ Add File Rotation Filter to Logger
    :param filename: log file name
    :param max_bytes: max bytes for rotater, default is MAX_BYTES
    :param backup_count: rotated log count, default is BACKUP_COUNT
    :param logger_name: logger name, the default is DEFAULT_LOGGER_NAME
    """
    rotator = RotatingFileHandler(

        filename=filename,
        maxBytes=max_bytes,
        backupCount=backup_count
    )
    logging.getLogger(logger_name).addFilter(rotator)

def basic_logger(
        filename,
        level=LOG_LEVEL,
        format=FORMAT,
        filemode=FILE_MODE,
        datefmt=DATE_FORMAT,
        console_format=CONSOLE_FORMAT,
        console_datefmt=CONSOLE_DATE_FORMAT,
        max_bytes=MAX_BYTES,
        backup_count=BACKUP_COUNT,
        logger_name=DEFAULT_LOGGER_NAME,
        **kw):
    """ Basic Logger Setup

    :param filename: log file name
    :param level: log level, default is LOG_LEVEL
    :param format: log formatter, default is FORMAT
    :param filemode: file mode, default is FILE_MODE
    :param datefmt: date time format, default is DATE_FORMAT
    :param console_format: console format template, default is CONSOLE_FORMAT
    :param console_datefmt: console date time format, default is CONSOLE_DATE_FORMAT
    :param max_bytes: max bytes for rotater, default is MAX_BYTES
    :param backup_count: rotated log count, default is BACKUP_COUNT
    :param logger_name: logger name, the default is DEFAULT_LOGGER_NAME
    :param **kw: all remaing args passed to basic_config
    """
    # setup basic logger
    init_basic_logger(filename, level, format, filemode, datefmt, **kw)

    # attach console
    add_console_handler(console_format, console_datefmt, logger_name)

    # add file rotation
    add_file_rotation(filename, max_bytes, backup_count, logger_name)
