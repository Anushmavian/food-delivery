#!/bin/bash

python src/consumer.py &
flask run --host=0.0.0.0
