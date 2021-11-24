#!/bin/sh
set -e
set -u
cd $(dirname $0)
for f in */Dockerfile */build.sh
do
	python3 update-from.py "$f"
	# NOTE
	# This would give the same, but is extra dependency and needs complicated shell coding
	#skopeo inspect --format '{{.Digest}}'  docker://debian:latest
done
