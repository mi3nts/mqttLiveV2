#!/bin/sh

kill $(pgrep -f 'python3 DCDataReader.py')
sleep 1
python3 DCDataReader.py &

kill $(pgrep -f 'python3 LNDataReader.py')
sleep 1
python3 LNDataReader.py &


