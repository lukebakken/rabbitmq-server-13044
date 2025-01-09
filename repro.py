import logging
import pika

LOG_FORMAT = "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) -35s %(lineno) -5d: %(message)s"
LOGGER = logging.getLogger(__name__)

logging.basicConfig(level=logging.ERROR, format=LOG_FORMAT)

c = pika.BlockingConnection()
ch = c.channel()

LOGGER.info("declaring exclusive queue")

# Note: exclusive=False results in unbounded queue count
# and eventual memory alarm
q = ch.queue_declare("", exclusive=True)
print("q: {}".format(q), flush=True)

LOGGER.info("declared exclusive queue, sleeping 30 seconds")
c.process_data_events(time_limit=30)
