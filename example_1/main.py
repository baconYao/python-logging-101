import logging

console = logging.StreamHandler()
file_handler = logging.FileHandler("file.log")
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name) s:%(lineno)d %(message) s",
    handlers=[console, file_handler],
)

logger = logging.getLogger("logging_101_ex1")

logger.debug("Ex1 debug message")
logger.info("Ex1 informational message")
logger.warning("Ex1 warning message")
logger.error("Ex1 error message")
logger.critical("Ex1 critical message")
