import logging


logger = logging.getLogger(__name__)


def hello_world():
    """
    Prints 'Hello World!'
    :return: str
    """
    output = "Hello World!"
    logger.info(output)
    return output
