#!/bin/bash
line="--------------------------"
echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "JOBS"; jobs; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"
