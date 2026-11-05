---
title: "CLUB club"
# sub_title: Command-line UNIX for Bioinformatics
sub_title: 2026-11-05
options:
  implicit_slide_ends: true
theme:
  name: tokyonight-moon
  override:
    slide_title:
      bold: true
    intro_slide:
      author:
        positioning: below_title
      title:
        alignment: center
        font_size: 5
      subtitle:
        alignment: center
        font_size: 5
    code:
      padding:
        horizontal: 2
        vertical: 1
      # Whether the theme's background color should be used around the code block.
      background: false
      line_numbers: false
---

2026-11-05 class
===

Today I'll give an introduction to the `dark-matter` scripts

# WTF is dark-matter?

A suite of Python scripts (and library functions) for bioinformatics
work.

You don't need to be a Python programmer to use the scripts. But you
need Python installed.

# Stats

`dark-matter` was written over the last 13 years (first commit 27.06.2013).

It provides 108 scripts, and has 87,267 lines of code and 2,627 tests.

![](../images/dark-matter-commits.png)


Installing dark-matter
===

```sh
$ pixi add dark-matter
# Or 'pixi upgrade dark-matter' if you already have it installed.

$ pixi shell

$ dark-matter-version.py
7.5.8
```

You can find the Python source on GitHub at
https://github.com/acorg/dark-matter


dark-matter is famously undocumented!
===

Or it was until now.

I got Claude to help with a basic categorization and description of all
the scripts.  So there is now a fairly minimal (but at least accurate)
main README at https://acorg.github.io/dark-matter/

Click on the `Scripts` link on the left to see a listing of the
available scripts. Each script (that supports `--help`) can be clicked
on to see its `--help` output.

Or go to https://github.com/acorg/dark-matter/ and in the `doc` directory
you'll see a link to `scripts.md`.

Today we'll look briefly at 15 scripts
===

# Simple utilities

* aa-compare.py
* aa-info.py
* fasta-count-chars.py
* fasta-count.py
* fasta-ids.py
* fasta-lengths.py

# More FASTA tools

* compare-sequences.py
* fasta-identity-table.py
* filter-fasta.py

# Command runners

* make-consensus.py
* run-bowtie2.py

# Tree tools

* curate-tree-ete.py
* tree-info.py

# SAM/BAM files

* sam-coverage-depth.py
* sam-reference-read-counts.py


aa-compare.py
===

aa-info.py
===

Print information about amino acids, based on names or codons.

fasta-count-chars.py
===

Print a summary of the characters in the sequences in FASTA input.

fasta-count.py
===

Count the number of sequences in FASTA input.

fasta-ids.py
===

Print the sequence IDs from FASTA input.

fasta-lengths.py
===

Print the sequence IDs and lengths from FASTA input.

compare-sequences.py
===

fasta-identity-table.py
===

Make an HTML table showing the identity between sequences in FASTA
input.

filter-fasta.py
===

Provides many ways to filter FASTA.

make-consensus.py
===

run-bowtie2.py
===

curate-tree-ete.py
===

tree-info.py
===

sam-coverage-depth.py
===

sam-reference-read-counts.py
===

Upcoming classes
===

* _de novo_ assembly.
* Protein-level matching.

<!--
Local Variables:
indent-tabs-mode: nil
End:
-->
