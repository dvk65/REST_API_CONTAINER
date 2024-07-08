#!/bin/bash

python -m unittest discover -s api

TEST_RESULT=$?

echo $TEST_RESULT

exit $TEST_RESULT