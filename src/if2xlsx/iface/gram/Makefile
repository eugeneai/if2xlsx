.PHONY: gram tests

gram: Excel.g4
	antlr4 -Dlanguage=Python3 $<

tests: gram
	nosetests -s .
