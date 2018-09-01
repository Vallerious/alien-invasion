#!/usr/bin/env bash
for filename in tests/*.py
do
    python3 "$filename"
done