build:
	# File fixes for Docker
	touch -d "$$(git log -1 --pretty=format:%ai file.txt)" file.txt
	chmod 0644 file.txt
	# Double build
	docker build -t dockertest .
	docker inspect dockertest -f '{{.Id}}' | tee ../docker-hash.txt
	docker rmi dockertest
	docker build -t dockertest .
	docker inspect dockertest -f '{{.Id}}'
	if ! [ "$$(cat ../docker-hash.txt)" = "$$(docker inspect dockertest -f '{{.Id}}')" ]; then echo "HASH mismatch, not reproducible!!!" && false; fi
	# TODO this is broken as Created timestamp always changes
	# See this issue and it references https://github.com/moby/moby/issues/40754

run-in-docker:
	docker run --rm -it dockertest

clean:
	docker rmi dockertest

