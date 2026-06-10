import time
from utils.logger import logger

def track_execution(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        logger.info(f"{func.__name__} Started")

        try:

            result = func(*args, **kwargs)

            duration = round(
                time.time() - start,
                2
            )

            logger.info(
                f"{func.__name__} Completed "
                f"in {duration}s"
            )

            return result

        except Exception as ex:

            logger.exception(
                f"{func.__name__} Failed"
            )

            raise

    return wrapper