#!/bin/bash

scripts/build.sh
docker tag siecle superbounou/siecle
docker push superbounou/siecle
