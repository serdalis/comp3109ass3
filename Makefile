#! usr/bin/make

GRAMMARFILE = VPL.g
BUILDDIR = build
TESTLAND = test.vpl

all: antlr

setup:
	  @mkdir -p build

%.vpl: antlr
	@echo "parsing $@ and generating assembly..."
	@python vpl2asm.py < $@ > target.s
	gcc -W -Wall -Pedantic -g target.s main.c -o run

antlr: setup
	@echo "Building ANTLR parser..."
	java -cp antlr-3.2.jar org.antlr.Tool -debug -o ${BUILDDIR} $(GRAMMARFILE)
	java -classpath .:$BUILD_DIR:antlr-3.2.jar Main $1 > "${1}.s"

clean:
	rm -f $(BUILDDIR)/*
	rm -f run

veryclean: clean
	rm -f *.s
	rm -f *.pyc
	rm -f antlr3/*.pyc
