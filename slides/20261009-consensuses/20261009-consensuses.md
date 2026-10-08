---
title: "CLUB club"
# sub_title: Command-line UNIX for Bioinformatics
sub_title: 2026-10-09
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

2026-10-09 class
===

Today we'll cover how to "call" a consensuses from a SAM/BAM file of
aligned reads.

Some basic initial comments
===

Your sequencing reads (or other sequences, e.g., contigs from _de
novo_ assembly) have been aligned to a reference sequence by a tool
like bowtie2. The result is in a SAM/BAM file.  Now you want to put
together a summary "consensus" sequence that represents what's in your
data _vis a vis_ the reference sequence.

The consensus sequence is a statistical summary
===

Especially with viral data, the idea that the genomes present in a
sample all carry a "consensus" genome sequence is extremely
simplistic.

Or even that any of them do.

This is pretty obvious, but is almost never mentioned, so it feels
like a widespread misconception, even though the idea of viral
quasispecies is well established.

# A consensus sequence is like a mean

There may be no virus particle containing the consensus sequence. Just
as with a set of numbers, the mean is not necessarily in the set.
E.g. `3, 4, 7, 10` have a mean of `6`. A consensus sequence is also a
form of summary statistic.

This makes for a nice puzzle, BTW. As the size of a set of numbers
increases, what happens to the probability that their mean is a member
of the set?  (Given some assumptions / model.)

# You have to deal with variation in any case

Even outside the viral world, there will still frequently be variation
in your sequence data. This can arise from misincorporation errors
during PCR, mis-reading of optical data while sequencing,
contamination, etc.

Reference bias
===

The choice of reference sequence to align to can have a major impact
on your eventual consensus. It's important to remember that the
reference may _not_ be particularly close to what's in your data. If
the genomes in your sample differ sufficiently from the reference in a
region, no reads will map to that part of the reference. If you then
call a consensus from the resulting SAM file, you will necessarily end
up with a sub-optimal result.

Something to be aware of: It is possible with some consensus callers
to tell it to use the reference if no reads map to a region. In
general this is probably a bad idea.

If you have good coverage, there's no real reason to give the
reference sequence to a consensus caller. A legitimate use of the
reference can be to adjudicate between reads with low coverage and
similar quality - you may want to call in favour of the reference
base.

Note that Geneious puts a `?` into consensus sequences for regions of
the reference with no matching reads. It is not clear whether your
organism does not have that region at all or whether you were unlucky
and molecules with sequences that do match the missing region were
simply not sequenced.

So how do you call a consensus?
===

The simplest thing to do is to proceed "site" by site (i.e., column by
column) through the reference genome positions. For each site you look
at the nucleotide calls (the bases _and_ their qualities) and "call" a
decision. The sequence of calls gives you a consensus sequence.

# Obvious considerations

* How many reads will you require at minimum to make a call at a site?
* What homogeneity threshold(s) will you use?

# Ambiguous nucleotide codes

```
    M: AC
    R: AG
    W: AT
    S: GC
    K: GT
    Y: CT
    V: ACG
    H: ACT
    D: AGT
    B: CGT
    N: ACGT
```

An example
===

![](../images/20261009-consensus-calling.png)

Using samtools mpileup | ivar
===

Here's the general pattern:

```sh
samtools mpileup -d 0 -aa -A -B -Q 0 --fasta-ref reference.fasta matches.bam
    | ivar consensus -p consensus-prefix -q 20 -t 0.6 -m 5
```

And you can try this on the Charite cluster:

```sh
$ samtools mpileup -d 0 -aa -A -B -Q 0 \
    --fasta-ref ~/data/references/NC_055231.1.fasta \
    ~/data/bam/mapped-to-NC_055231.1.bam \
    | ivar consensus -p consensus-prefix -q 20 -t 0.6 -m 5
```


Upcoming classes
===

* The dark-matter tools.
* _de novo_ assembly.
* Protein-level matching.
* Making multiple-sequence alignments.
* Tree making.

<!--
Local Variables:
indent-tabs-mode: nil
End:
-->
