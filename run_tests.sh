#!/bin/bash

python -m unittest discover -s tests

echo $TEST_RESULT

TEST_RESULT=$?

exit $TEST_RESULT