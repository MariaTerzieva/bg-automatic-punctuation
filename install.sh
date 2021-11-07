#! /usr/bin/env bash

cd "$(dirname "$0")"
pip install -r ./solution/resources/requirements.txt
python ./solution/resources/download_external_library_models.py