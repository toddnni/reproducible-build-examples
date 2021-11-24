SRC=resources
NAME=zip-$$(cat Version.txt)-$$(git rev-parse --short HEAD).zip

build:
	chmod -R u=rwX,g=rwX,o=rX $(SRC)
	find $(SRC) -exec sh -c 'touch -d "$$(git log -1 --pretty=format:%ai {})" {}' \;
	find $(SRC) -print0 | sort -z | TZ=UTC xargs -0 zip -X $(NAME)
	unzip -Z $(NAME)
	sha256sum $(NAME) | tee hash.txt

clean:
	rm -vf *.zip
