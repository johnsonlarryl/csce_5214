#!/bin/bash

# Comment out the following line for trouble-shooting locally
poetry run python -m uvicorn main:app --reload --port=$WEB_SERVICE_PORT --host=0.0.0.0

# Uncomment the following lines for trouble-shooting locally
# touch /tmp/text_classification.log
# tail -f /tmp/text_classification.log