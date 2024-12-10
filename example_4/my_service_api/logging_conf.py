import logging
from logging.config import dictConfig


class HelloFilter(logging.Filter):
    def __init__(self, name: str = "") -> None:
        super().__init__(name)

    def filter(self, record: logging.LogRecord) -> bool:
        if "Hello" in record.__dict__["msg"]:
            record.__dict__["msg"] = record.__dict__["msg"].replace("Hello", "Hola")  # noqa: E501
        return True


def configure_logging() -> None:
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "filters": {
                "hello_filter": {
                    "()": HelloFilter,
                },
            },
            "formatters": {
                "console": {
                    "class": "logging.Formatter",
                    "format": "%(levelname)-8s - %(name)s - %(module)-10s:"
                    + " %(funcName)s %(lineno)-4d - %(message)s",
                },
                "file": {
                    "class": "logging.Formatter",
                    "datefmt": "%Y-%m-%dT%H:%M:%S",
                    "format": "%(asctime)s.%(msecs)03dZ | %(levelname)-8s | %(name)s:%(lineno)d - %(message)s",  # noqa: E501,
                },
                "json_file": {
                    "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
                    "datefmt": "%Y-%m-%dT%H:%M:%S",
                    "format": "%(asctime)s %(msecs)03d %(levelname)-8s %(name)s %(lineno)d %(message)s",  # noqa: E501
                },
            },
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "level": "DEBUG",
                    "formatter": "console",
                },
                "rotating_file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "level": "DEBUG",
                    "formatter": "file",
                    "filename": "my_service_api.log",
                    "maxBytes": 1024 * 1024,  # 1MB,
                    "backupCount": 5,
                    "encoding": "utf8",
                    "filters": ["hello_filter"],
                },
                "rotating_json_file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "level": "DEBUG",
                    "formatter": "json_file",
                    "filename": "my_service_api_json.log",
                    "maxBytes": 1024 * 1024,  # 1MB,
                    "backupCount": 5,
                    "encoding": "utf8",
                    "filters": ["hello_filter"],
                },
            },
            "loggers": {
                "my_service_api": {
                    "handlers": ["default", "rotating_file", "rotating_json_file"],  # noqa: E501
                    "level": "INFO",
                    "propagate": False,
                },
            },
        }
    )
