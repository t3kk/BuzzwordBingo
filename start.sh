#!/bin/bash
echo "Starting BuzzwordBingo"
pyEnv/bin/gunicorn -w 4 -b 0.0.0.0:8003 run:app & echo $! > server.pid &
