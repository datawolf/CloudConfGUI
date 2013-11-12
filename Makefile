# Makefile for run CloudConf
#
#
.PHONY: run motif clean

run:
	./cloudconf.py  -style cleanlooks
	
motif:
	./cloudconf.py  -style motif

clean:
	$(RM)	*.ini
