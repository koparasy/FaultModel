TOPTARGETS := all clean

SUBDIRS := $(wildcard */.)

path=$(shell pwd)
cmd="CFLAGS=-DFI=1 -I/${path}/../include -L/${path}/../lib/"
lflags="LFLAGS=-lm5"
$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@ $(cmd) $(lflags) $(MAKECMDGOALS) 


.PHONY: $(TOPTARGETS) $(SUBDIRS)
