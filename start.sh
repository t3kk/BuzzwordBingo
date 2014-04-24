#!/bin/bash
echo "Starting BuzzwordBingo"
pyEnv/bin/gunicorn -w 4 -b localhost:8003 run:app & echo $! > server.pid &
