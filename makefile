GRAMMARFILE = VPL.g
BUILDDIR = build
TESTLANG = test.vpl

all: antlr

setup:
	@mkdir -p build

%.vpl: antlr
	@echo "Parsing $@ and Generating Assembly..."
	@python vpl2asm.py < $@ > target.s
	gcc -w -Wall -pedantic -g target.s main.c -o run
	@echo "Ensure this is run on a 32-bit architecture, as x64 has a different instruction set"

antlr: setup
	@echo "Building ANTLR Parser..."
	@java -cp antlr-3.1.2.jar org.antlr.Tool -o $(BUILDDIR) $(GRAMMARFILE)
	@echo "Done."
clean:
	rm -f $(BUILDDIR)/*
	rm -f run
veryclean: clean
	rm -f *.s
	rm -f *.pyc
	rm -f antlr3/*.pyc
