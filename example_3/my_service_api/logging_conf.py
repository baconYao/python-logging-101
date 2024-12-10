from logging.config import dictConfig


def configure_logging() -> None:
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "console": {
                    "class": "logging.Formatter",
                    "datefmt": "%Y-%m-%dT%H:%M:%S",
                    "format": "%(levelname)-8s - %(name)s - %(module)-10s:"
                    + " %(funcName)s %(lineno)-4d - %(message)s",
                },
                "file": {
                    "class": "logging.Formatter",
                    "datefmt": "%Y-%m-%dT%H:%M:%S",
                    "format": "%(asctime)s.%(msecs)03dZ | %(levelname)-8s | %(name)s:%(lineno)d - %(message)s",  # noqa: E501,
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
                },
            },
            "loggers": {
                "my_service_api": {
                    "handlers": ["default", "rotating_file"],
                    "level": "INFO",
                    "propagate": False,
                },
            },
        }
    )
