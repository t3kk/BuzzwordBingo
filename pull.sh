#!/bin/bash
./stop.sh
git pull
./deploy.sh
./start.sh
