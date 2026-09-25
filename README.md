# Command-line UNIX for Bioinformatics

Here you'll find the slides and videos for our CLUB club meetings.

* 2026-09-04: **Intro and setup** [Video](https://youtu.be/W7wlbDF9Ey0) ✽ [PDF](slides/20260904-intro-and-setup/20260904-intro-and-setup.pdf) ✽ [Markdown](slides/20260904-intro-and-setup/20260904-intro-and-setup.md)
* 2026-09-11: **Working with sequences** [Video](https://www.youtube.com/watch?v=ud3rFYOZ3CM) ✽ [PDF](slides/20260911-ngs-data/20260911-ngs-data.pdf) ✽ [Markdown](slides/20260911-ngs-data/20260911-ngs-data.md)
* 2026-09-18: **Mapping with bowtie2** [Video](https://www.youtube.com/watch?v=fUVUMLMscdk) ✽ [PDF](slides/20260918-nt-mapping/20260918-nt-mapping.pdf) ✽ [Markdown](slides/20260918-nt-mapping/20260918-nt-mapping.md)
* 2026-09-25: **Using Slurm** [Video](https://www.youtube.com/watch?v=xhfKUMNoMFQ) ✽ [PDF](slides/20260925-slurm/20260925-slurm.pdf) ✽ [Markdown](slides/20260925-slurm/20260925-slurm.md)

## Presenting

The slides are written in Markdown and are presented in the
terminal. If you want to do that, you'll need
[presenterm](https://github.com/mfontanini/presenterm) ([installation
instructions](https://mfontanini.github.io/presenterm/install.html)).

Use [kitty](https://sw.kovidgoyal.net/kitty/) if you want variable font sizes to work.

Run as follows:

```bash
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

## Verifying slides build

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
