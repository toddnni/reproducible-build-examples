build:
	# File fixes, maybe not needed in kaniko
	#touch -d "$$(git log -1 --pretty=format:%ai file.txt)" file.txt
	#chmod 0644 file.txt
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
	skopeo copy oci:oci docker-daemon:kanikotest:latest
	docker run --rm -it kanikotest

clean:
	rm -rf digest oci
	docker rmi kanikotest