all:
	cd buildah; make
	cd kaniko; make

update-images:
	sh update-tags.sh

clean:
	cd buildah; make clean
	cd kaniko; make clean
