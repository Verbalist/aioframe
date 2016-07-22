#!/usr/bin/env bash
IMAGE_NAME="base"

sudo docker build -no-cache -t "${IMAGE_NAME}" .
