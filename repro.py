import logging
import pika
import time

LOG_FORMAT = "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) -35s %(lineno) -5d: %(message)s"
LOGGER = logging.getLogger(__name__)

logging.basicConfig(level=logging.ERROR, format=LOG_FORMAT)

while True:
    try:
        c = pika.BlockingConnection()
        ch = c.channel()

        # Note: exclusive=False results in unbounded queue count
        # and eventual memory alarm
        q = ch.queue_declare("", exclusive=True)
        print("q: {}".format(q), flush=True)

        ch.queue_bind(queue="", exchange="amq.direct", routing_key="foobar")
        ch.close()
        c.close()
    except pika.exceptions.ChannelClosedByBroker:
        print("BOOM")
        c.close()

    time.sleep(2)
