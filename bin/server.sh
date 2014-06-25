#!/bin/bash

APP_DIR=..

function start() {
    cd $APP_DIR
    nohup python server/server.py > log/server.log 2>&1 &
}

function stop() {
    ps -ef | grep "server.py" | grep -v grep | awk '{print $2}'| xargs kill -9
}


case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    *)
        echo "Usage: $0 (start|stop)"
        ;;
esac
exit 0
