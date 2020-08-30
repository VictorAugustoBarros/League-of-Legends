from __future__ import annotations

import datetime
import logging
import os
import sys


class Logger:

    __monostate = None

    def __init__(self, name="callback", log_level="INFO"):
        """
        :param name:
        :param log_level:
        """
        if not Logger.__monostate:
            Logger.__monostate = self.__dict__

            self.logger = logging.getLogger(name)
            hdlr = logging.StreamHandler(sys.stdout)
            log_format = "%(asctime)-15s [Callback] %(levelno)s: %(levelname)s - %(message)s"
            formatter = logging.Formatter(log_format)
            hdlr.setFormatter(formatter)
            self.logger.addHandler(hdlr)

            debug = os.environ.get("LOG_LEVEL", log_level)
            if debug == "INFO":
                debug = logging.INFO
            elif debug == "DEBUG":
                debug = logging.DEBUG
            elif debug == "ERROR":
                debug = logging.ERROR
            elif debug == "CRITICAL":
                debug = logging.CRITICAL

            self.logger.setLevel(debug)
        else:
            self.__dict__ = Logger.__monostate

    def __default(self, o):
        if type(o) is datetime.date or type(o) is datetime.datetime:
            return o.isoformat()

    def info(self, message, **kwargs):
        self.logger.info(message, **kwargs)

    def warning(self, message, **kwargs):
        self.logger.warning(message, **kwargs)

    def success(self, message, **kwargs):
        self.logger.info(message, **kwargs)

    def error(self, message, **kwargs):
        self.logger.error(message, **kwargs)

    def critical(self, message, **kwargs):
        self.logger.critical(message, **kwargs)

    def debug(self, message, **kwargs):
        self.logger.debug(message, **kwargs)
