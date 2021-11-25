all:
	cd packages; make
	cd containers; make

clean:
	cd packages; make clean
	cd containers; make clean
