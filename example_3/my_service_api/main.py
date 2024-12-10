import logging

from my_service_api.handlers.users import greet as user_great
from my_service_api.logging_conf import configure_logging
from my_service_api.security.auth import greet as auth_great

logger = logging.getLogger("my_service_api.main")


def main():
    configure_logging()  # Example: setup logging for the service
    logger.info("Hi Main")
    user_great()
    auth_great()


if __name__ == "__main__":
    main()
