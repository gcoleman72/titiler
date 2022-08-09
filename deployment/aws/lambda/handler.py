"""AWS Lambda handler."""

import logging

from mangum import Mangum

from titiler.application.main import dir
pp

logging.getLogger("mangum.lifespan").setLevel(logging.ERROR)
logging.getLogger("mangum.http").setLevel(logging.ERROR)

handler = Mangum(app, lifespan="auto")
