GRAMMARFILE = VPL.g
BUILDDIR = build
TESTLANG = test.vpl

all: antlr

setup:
	@mkdir -p build

%.vpl: antlr
	@echo "parsing input file $@"
	@echo "generating assembly"
	@python vpl2asm.py < $@ > target.s
	@echo "compiling"
	gcc -w -Wall -pedantic -g target.s main.c -o run
	@echo "type ./run to execute program"

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
