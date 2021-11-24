FROM debian:latest@sha256:e8c184b56a94db0947a9d51ec68f42ef5584442f20547fa3bd8cbd00203b2e7a

LABEL org.opencontainers.image.authors="toddnni"

#COPY --chown=1000:1000 file.txt .
COPY file.txt .
RUN chown 1000:1000 file.txt

RUN "/bin/bash"
