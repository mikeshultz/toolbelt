#!/usr/bin/bash

Status() {
    CURRENT=$(status.py)
    echo -n "$CURRENT"
}

# Print the clock

while true; do
    echo "$(Status)"
    sleep 1
done
