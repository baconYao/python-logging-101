import logging

logger = logging.getLogger(__name__)


def greet():
    logger.debug("Hi auth (Debug)")
    logger.info("Hi auth")
