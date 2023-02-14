#!/bin/bash

OLD=$1

END=$(echo $OLD | tr '.' '\n' | tail -1)

START=$(echo $OLD | tr '.' '\n' | head -2 | tr '\n' '.')

NEW=$[$END+1]

FINAL="$START$NEW"

echo "$FINAL"