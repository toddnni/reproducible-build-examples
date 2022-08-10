SRC=resources
NAME=tar-$$(cat Version.txt)-$$(git log -1 --pretty=format:%h .).tgz

build:
	rm -f $(NAME)
	chmod -R u=rwX,g=rwX,o=rX $(SRC)
	# NOTE workaround, reset diff-index after permission change, need to run something like status once
	git status -s .
	tar --sort=name --mtime="$$(git log -1 --pretty=format:%ai Version.txt)" \
	  --owner=0 --group=0 --numeric-owner \
	  --pax-option=exthdr.name=%d/PaxHeaders/%f,delete=atime,delete=ctime \
	  -czf $(NAME) $(SRC)
	tar -vtf $(NAME)
	sha256sum $(NAME) | tee ../tar-hash.txt
	# Note same trick here
	git status -s ..
	git diff-index --quiet HEAD -- ../tar-hash.txt || (echo "WARN: hash differs from the saved one!" && false)

clean:
	rm -vf *.tgz
