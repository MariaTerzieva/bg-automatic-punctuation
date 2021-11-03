#! /usr/bin/env bash

cd "$(dirname "$0")"
pip install -r ./resources/requirements.txt
python ./resources/download_external_library_models.py