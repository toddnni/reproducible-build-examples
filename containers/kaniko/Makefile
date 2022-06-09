build:
	# File fixes, timestamp not needed with kaniko
	#touch -d "$$(git log -1 --pretty=format:%ai file.txt)" file.txt
	chmod 0644 file.txt
	# Double build
	docker run --rm -v $$PWD:/workspace \
	gcr.io/kaniko-project/executor:latest \
	--context /workspace \
	--dockerfile Dockerfile \
	--no-push \
	--reproducible \
	--digest-file /workspace/digest \
	--oci-layout-path /workspace/oci
	cat digest | tee ../kaniko-hash.txt
	docker run --rm -v $$PWD:/workspace \
	gcr.io/kaniko-project/executor:latest \
	--context /workspace \
	--dockerfile Dockerfile \
	--no-push \
	--reproducible \
	--digest-file /workspace/digest \
	--oci-layout-path /workspace/oci
	cat digest
	if ! [ "$$(cat ../kaniko-hash.txt)" = "$$(cat digest)" ]; then echo "HASH mismatch, not reproducible!!!" && false; fi
	# Note same trick here
	git status -s ..
	git diff-index --quiet HEAD -- ../zip-hash.txt || (echo "WARN: hash differs from the saved one!" && false)

run-in-docker:
	docker run --rm -it -v "$$PWD"/oci:/oci debian:latest /bin/sh -c "chmod -R g+rX,o+rX /oci/"
	skopeo copy oci:oci docker-daemon:kanikotest:latest
	docker run --rm -it kanikotest

clean:
	rm -f digest
	docker run --rm -it -v "$$PWD"/oci:/oci debian:latest /bin/sh -c "rm -rf /oci/*"
	rmdir oci
	docker rmi kanikotest
