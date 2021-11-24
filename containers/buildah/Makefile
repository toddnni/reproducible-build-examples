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

oci:
	skopeo copy containers-storage:localhost/buildahtest oci:oci

run-in-docker:
	skopeo copy containers-storage:localhost/buildahtest docker-daemon:buildahtest:latest
	docker run --rm -it buildahtest

clean:
	buildah rmi buildahtest
	docker rmi buildahtest
	rm -rf oci
