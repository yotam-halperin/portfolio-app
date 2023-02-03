#!/bin/bash

sleep 10

curl -X GET 'http://18.135.117.62/health' || exit 1