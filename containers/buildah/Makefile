build:
	# Double build
	buildah unshare ./build.sh
	skopeo inspect containers-storage:localhost/buildahtest -f '{{.Digest}}' | tee ../buildah-hash.txt
	buildah rmi buildahtest
	buildah unshare ./build.sh
	skopeo inspect containers-storage:localhost/buildahtest -f '{{.Digest}}'
	if ! [ "$$(cat ../buildah-hash.txt)" = "$$(skopeo inspect containers-storage:localhost/buildahtest -f '{{.Digest}}')" ]; then echo "HASH mismatch, not reproducible!!!" && false; fi
	# Note same trick here
	git status -s ..
	git diff-index --quiet HEAD -- ../buildah-hash.txt || (echo "WARN: hash differs from the saved one!" && false)

build-dockerfile:
	# Double build
	buildah bud --timestamp 0 -t buildahtest2 .
	skopeo inspect containers-storage:localhost/buildahtest2 -f '{{.Digest}}' | tee ../buildah-hash2.txt
	buildah rmi buildahtest2
	buildah bud --timestamp 0 -t buildahtest2 .
	skopeo inspect containers-storage:localhost/buildahtest2 -f '{{.Digest}}'
	if ! [ "$$(cat ../buildah-hash2.txt)" = "$$(skopeo inspect containers-storage:localhost/buildahtest2 -f '{{.Digest}}')" ]; then echo "HASH mismatch, not reproducible!!!" && false; fi
	# Note same trick here
	git status -s ..
	git diff-index --quiet HEAD -- ../buildah-hash2.txt || (echo "WARN: hash differs from the saved one!" && false)

oci:
	skopeo copy containers-storage:localhost/buildahtest oci:oci

run-in-docker:
	skopeo copy containers-storage:localhost/buildahtest docker-daemon:buildahtest:latest
	docker run --rm -it buildahtest

run-in-docker2:
	skopeo copy containers-storage:localhost/buildahtest2 docker-daemon:buildahtest2:latest
	docker run --rm -it buildahtest2

clean:
	buildah rmi buildahtest
	buildah rmi buildahtest2
	docker rmi buildahtest
	docker rmi buildahtest2
	rm -rf oci
