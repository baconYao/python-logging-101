import logging

console = logging.StreamHandler()
file_handler = logging.FileHandler("file.log")
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)-8s - %(name)s - %(module)-10s: %(funcName)s "
    + "%(lineno)-4d - %(message)s",
    handlers=[console, file_handler],
)

logger = logging.getLogger("logging_101_ex1")


def test_func():
    logger.debug("Ex1 debug message")
    logger.info("Ex1 informational message")
    logger.warning("Ex1 warning message")
    logger.error("Ex1 error message")
    logger.critical("Ex1 critical message")


if __name__ == "__main__":
    test_func()
