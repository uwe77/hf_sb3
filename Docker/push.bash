#!/usr/bin/env bash

REPOSITORY="uwwee/ubuntu"
TAG="20.04"

IMG="${REPOSITORY}:${TAG}"

docker image push "${IMG}"
