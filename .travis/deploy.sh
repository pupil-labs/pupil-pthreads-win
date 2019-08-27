#!/bin/bash

pip3 install twine
twine upload \
    --username "__token__" \
    --password "$PYPI_APITOKEN" \
    ./dist/*