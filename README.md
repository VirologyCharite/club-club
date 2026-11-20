## Command-line UNIX for Bioinformatics (CLUB) club

Here you'll find the slides and videos for our CLUB club meetings.

1. **Intro and setup** 2026-09-04 [Video](https://youtu.be/W7wlbDF9Ey0), [PDF](slides/20260904-intro-and-setup/20260904-intro-and-setup.pdf), [Markdown](slides/20260904-intro-and-setup/20260904-intro-and-setup.md)
2. **Working with sequences** 2026-09-11 [Video](https://www.youtube.com/watch?v=ud3rFYOZ3CM), [PDF](slides/20260911-ngs-data/20260911-ngs-data.pdf), [Markdown](slides/20260911-ngs-data/20260911-ngs-data.md)
3. **Mapping with bowtie2** 2026-09-18 [Video](https://www.youtube.com/watch?v=fUVUMLMscdk), [PDF](slides/20260918-nt-mapping/20260918-nt-mapping.pdf), [Markdown](slides/20260918-nt-mapping/20260918-nt-mapping.md)
4. **Using SLURM** 2026-09-25 [Video](https://www.youtube.com/watch?v=xhfKUMNoMFQ), [PDF](slides/20260925-slurm/20260925-slurm.pdf), [Markdown](slides/20260925-slurm/20260925-slurm.md)
5. **Getting sequences** 2026-10-02 [Video](https://www.youtube.com/watch?v=3I-6uYH051Y), [PDF](slides/20261002-getting-sequences/20261002-getting-sequences.pdf), [Markdown](slides/20261002-getting-sequences/20261002-getting-sequences.md)
6. **Making consensuses** 2026-10-09 [Video](https://www.youtube.com/watch?v=64IFH_-Wmik), [PDF](slides/20261009-consensuses/20261002-consensuses.pdf), [Markdown](slides/20261009-consensuses/20261009-consensuses.md)
7. **Multiple sequence alignments** 2026-10-16 [Video](https://www.youtube.com/watch?v=hoEC7DzNtmo), [PDF](slides/20261016-multiple-sequence-alignment/20261002-consensuses.pdf), [Markdown](slides/20261016-multiple-sequence-alignment/20261016-multiple-sequence-alignment.md)
8. **Making trees** 2026-10-23 [Video](https://www.youtube.com/watch?v=cfQ5XW_Bcbg), [PDF](slides/20261023-trees/20261002-consensuses.pdf), [Markdown](slides/20261023-trees/20261023-trees.md)
9. **Dark-matter scripts** 2026-11-06 [Video](https://www.youtube.com/watch?v=uqzhRNgtcY8), [PDF](slides/20261106-dark-matter/20261106-dark-matter.pdf), [Markdown](slides/20261106-dark-matter/20261106-dark-matter.md)
10. **_De novo_ assembly** 2026-11-13 [Video](https://www.youtube.com/watch?v=bIQzwGpEUeI), [PDF](slides/20261113-de-novo-assembly/20261113-de-novo-assembly.pdf), [Markdown](slides/20261113-de-novo-assembly/20261113-de-novo-assembly.md)
11. **aa mapping** 2026-11-20 [Video](https://www.youtube.com/watch?v=zwfqQWN61HE), [PDF](slides/20261120-aa-mapping/20261120-aa-mapping.pdf), [Markdown](slides/20261120-aa-mapping/20261120-aa-mapping.md)

## Presenting the slides

The slides are written in Markdown and presented in the terminal.  If
you want to do that, you'll need
[presenterm](https://github.com/mfontanini/presenterm) ([installation
instructions](https://mfontanini.github.io/presenterm/install.html)).

Use [kitty](https://sw.kovidgoyal.net/kitty/) if you want variable font sizes to work.

Run as follows:

```bash
# Show the 2026-09-04 introduction slides.
$ presenterm slides/20260904-intro-and-setup/20260904-intro-and-setup.md
```

## Making slide PDFs

### Pre-requisites

On OS X:

```sh
$ brew install weasyprint gdk-pixbuf
```

### Making the PDFs

```sh
$ make pdf
```

## Tests

`make verify` checks that every slide deck under `slides/` can be exported
to PDF by presenterm without error (this needs [tmux](https://github.com/tmux/tmux)
installed, in addition to the pre-requisites above):

```sh
$ make verify
```

This same check runs automatically:

* In CI, via [.github/workflows/verify-slides.yml](.github/workflows/verify-slides.yml),
  on every push and pull request that touches `slides/`.
* Locally, as a pre-commit hook that checks any staged slide decks before
  each commit. Enable it once per clone with:

  ```sh
  $ git config core.hooksPath githooks
  ```
