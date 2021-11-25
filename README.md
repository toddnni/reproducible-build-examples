Reproducible Build Examples
===========================

What
----

The same source will always produce the same output.

Term Hermetic builds is used in Google context (eg. SRE books and bazel).

Why
---

Motivation for reproducible builds

- security: reproducible builds can be used to verify builds, as the build result can be checked on another system
- quality: push for reproducible builds enforce one to design and change the build so that there are no undocumented inputs
- and it will grind out all undocumented build system dependencies and potential errors (like different permissions from different build systems)
- efficiency: deterministic builds leads to efficiency as single source revisions equals to single output and the output can efficiently cached

Resources
---------

- Collection of resources <https://reproducible-builds.org/>
- Good old tips for managing the timestamps <https://wiki.debian.org/ReproducibleBuilds/Howto>
- Reproducible buildah build examples <https://tensor5.dev/reproducible-container-images/>

Basic tricks
------------

Sources

- pinpoint the exact sources for the build and check checksums

Timestamps

- do the build in fixed (UTC) timezone
- ensure fixed timestamps of the contained resources (use the latest modification timestamp)

Version numbers

- version numbers need to be deterministic, so no incrementing counters or build numbers. Git checksums are good.

Resources

- ensure that the order of resources is deterministic
- fix resource permissions (mask, uid and gid)
- ensure uniform (unix) line endings

Compiling

- ensure that compiler does not inject build timestamp or it is controllable
- ensure that compiler output is reproducible
- build in a fixed path as path components are sometimes stored in the compilation
- check that locale language settings does not affect the output

Notes
-----

Build time does not have any meaning in reproducible builds. If there is a need to refer to a time, then you refer to the last modification time of the source.

If build time need to be stored, it can be stored as build output metadata.

Reproducibility need to be tested, because it is very easy to break it.

Examples
--------

Simple packaging examples [packages/](packages/)

Docker / Container examples [containers/](containers/)

- Potential next investigation is to make reproducible build that uses fixed operating system packages

No compiling examples yet.
