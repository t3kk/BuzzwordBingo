#!/bin/bash
kill $(cat server.pid)
git pull
./deploy.sh
./start.sh
