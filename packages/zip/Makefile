SRC=resources
#NAME=zip-$$(cat Version.txt)-$$(git rev-parse --short HEAD).zip
NAME=zip-$$(cat Version.txt)-$$(git log -1 --pretty=format:%h .).zip

build:
	rm -f $(NAME)
	chmod -R u=rwX,g=rwX,o=rX $(SRC)
	# NOTE workaround, reset diff-index after permission change, need to run something like status once
	git status -s .
	find $(SRC) -exec sh -c 'touch -d "$$(git diff-index --quiet HEAD -- {} && git log -1 --pretty=format:%ai {})" {}' \;
	find $(SRC) -print0 | sort -z | TZ=UTC xargs -0 zip -X $(NAME)
	unzip -Z $(NAME)
	sha256sum $(NAME) | tee ../zip-hash.txt
	# Note same trick here
	git status -s ..
	git diff-index --quiet HEAD -- ../zip-hash.txt || (echo "WARN: hash differs from the saved one!" && false)

clean:
	rm -vf *.zip
