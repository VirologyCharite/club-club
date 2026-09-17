XARGS := xargs $(shell test $$(uname) = Linux && echo -r)

MARKDOWN = $(wildcard slides/*/*.md)
PDF = $(subst .md,.pdf,$(MARKDOWN))


%.pdf: %.md
	presenterm --export-pdf $<

.PHONY: pdf verify clean clobber

pdf: $(PDF)

verify:
	scripts/verify-slides.sh $(MARKDOWN)

clean:
	find . \( -name '*.pyc' -o -name '*~' \) -print0 | $(XARGS) -0 rm
	find . -name '__pycache__' -type d -print0 | $(XARGS) -0 rm -r
	find . -name '.pytest_cache' -type d -print0 | $(XARGS) -0 rm -r
	find . -name '.ruff_cache' -type d -print0 | $(XARGS) -0 rm -r

clobber:
	rm -f $(PDF)
