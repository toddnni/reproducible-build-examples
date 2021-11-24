#!/bin/sh
set -e
set -u

ctr=$(buildah from debian@sha256:e8c184b56a94db0947a9d51ec68f42ef5584442f20547fa3bd8cbd00203b2e7a ) #FROM debian:latest

#LABEL org.opencontainers.image.authors="toddnni"
buildah config --label org.opencontainers.image.authors="toddnni" "$ctr"
buildah commit --omit-timestamp "$ctr"

#COPY --chown=1000:1000 file.txt .
mnt=$(buildah mount "$ctr")

cp file.txt "$mnt"
chmod 0644 "$mnt/file.txt"
# TODO does not seem to be necessary?
touch --date="$(git log -1 --pretty=format:%ai file.txt)" "$mnt/file.txt"
# NOTE chown is not must, defaults to root
chown 1000:1000 "$mnt/file.txt"

buildah umount "$ctr"
buildah commit --omit-timestamp "$ctr"

#RUN "/bin/sh"
buildah config --cmd '/bin/bash' "$ctr"
buildah commit --omit-timestamp "$ctr" "buildahtest"

buildah rm "$ctr"
