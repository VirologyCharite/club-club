# MAFFT command-line options

All options taken by the `mafft` command. The list comes from the
option parser in the `mafft` script (`core/mafft.tmpl`) of **MAFFT
v7.471** (July 2020). The four options added later, up to v7.511, come
from the changelog. The current source (v7.526) wasn't available to
check; see the notes at the end.

The tag after each option shows where it is documented, using the keys
in the URL list at the bottom. **[src]** means the option appears only
in the source code. Its description is inferred from what the code
does, so treat it as approximate.

## Help and version

- `--auto`: choose L-INS-i, FFT-NS-i or FFT-NS-2 automatically from data size. [MAN, ADD, TREEIN]
- `--help`, `--info`: print a short usage summary. [src]
- `--version`: print the version and exit. [src]
- `--man`: show the manual page. [src]

## Pairwise / distance stage (strategy)

- `--6merpair`: distances from shared 6-mers; the default for FFT-NS methods. [MAN, ADD, VIRAL, REGION, SRV-FRAG]
- `--10merpair`: the same, using 10-mers. [src]
- `--6mermultipair`, `--10mermultipair`: k-mer distances, "multi" variant. [src]
- `--multipair`: accurate (costly) pairwise stage for `--addfragments`. [ADD, SRV-FRAG]
- `--globalpair`: all-to-all Needleman–Wunsch; with `--maxiterate 1000` this is G-INS-i. [MAN, ALG, TREEOUT, MT]
- `--localpair`: all-to-all Smith–Waterman; with `--maxiterate 1000` this is L-INS-i. [MAN, ALG, TREEOUT, DASH]
- `--genafpair`: local alignment with generalized affine gaps; with `--maxiterate 1000` this is E-INS-i. [MAN, ALG]
- `--localgenafpair`: alias for `--genafpair`. [src]
- `--oldgenafpair`: E-INS-i with the parameters used before v7.243. [ALG, MPI]
- `--globalgenafpair`: removed; exits with "no longer supported". [src]
- `--fastapair`: pairwise alignments by FASTA (FASTA must be installed). [MAN]
- `--fastswpair`: FASTA in Smith–Waterman mode. [MAN]
- `--blastpair`: pairwise alignments by BLAST. [MAN (named under `--weighti` only)]
- `--lastpair`, `--lastmultipair`: pairwise alignments by LAST. [src; see Katoh & Frith 2012]
- `--last_m n`, `--last_e n`: LAST tuning parameters passed to the pairwise step. [src]
- `--last_subopt`, `--last_once`: further LAST-mode switches. [src]
- `--hybridpair`: hybrid distance mode. [src]
- `--shortlongpair`, `--longshortpair`: local pairwise mode with zeroed offsets; a source comment says it is used with `--addfull`. [src]

## RNA structural alignment (Q-INS-i / X-INS-i)

- `--scarnapair`: MXSCARNA pairwise structural alignment (default for X-INS-i). [NCRNA]
- `--larapair`: LaRA pairwise structural alignment. [NCRNA]
- `--laraparams file`: LaRA parameter file. [NCRNA]
- `--slarapair`: SLARA pairwise structural alignment. [src]
- `--foldalignlocalpair`, `--foldalignglobalpair`: FOLDALIGN local / global pairwise alignment. [NCRNA]
- `--foldalignpair`: alias for `--foldalignlocalpair`. [src]
- `--dafspair`: DAFS pairwise structural alignment. [src]
- `--mccaskill`: base-pairing probabilities by the McCaskill algorithm. [NCRNA (as the default replaced by `--contrafold`)]
- `--contrafold`: base-pairing probabilities by CONTRAfold. [NCRNA]
- `--dafs`: base-pairing probabilities by DAFS. [src]
- `--rnaalifold`: RNAalifold-based structural term. [src]
- `--ribosum`: RIBOSUM scoring for RNA. [src]
- `--rop x`, `--rep x`: gap parameters for the RNA structural term. [src]
- `--weightr x`, `--weightm x`: weights for the RNA structural terms. [src]

## Progressive and iterative stages

- `--retree n`: number of guide-tree rebuilds (default 2); `--retree 0 --treeout` writes the tree without aligning. [MAN, ALG, TIPS, TREEOUT]
- `--maxiterate n`: maximum number of iterative refinement cycles (default 0). [MAN, ALG, TIPS, ADD, MERGE]
- `--weighti x`: weight of the consistency term (default 2.7). [MAN, SRV-FRAG]
- `--noscore`: skip the score check during iterative refinement. [MAN]
- `--oneiteration`: a single refinement pass. [src]
- `--skipiterate x`: refinement threshold (must be ≥ 0). [src]
- `--bestfirst`, `--adhoc0`, `--adhoc1`, `--adhoc2`: refinement / parallelization strategies; they also change the iteration cap (254 or 16). [src]
- `--simplehillclimbing`: alias for `--adhoc2`. [src]
- `--sp`: rigorous sum-of-pairs scoring; with refinement it works single-threaded only. [src]
- `--bunkatsunashi`: Japanese for "no division"; passes a no-split flag to the refinement program. [src]
- `--unweight`: turn off sequence weighting. [src]
- `--minimumweight x`: minimum sequence weight. [src]
- `--alga`: alternative group-to-group algorithm switch. [src]
- `--algq`: removed; exits with "no longer supported". [src]
- `--fft`, `--nofft`: turn the FFT approximation in group-to-group alignment on or off. [MAN, TIPS]
- `--memsave`, `--nomemsave`: force or prevent the Myers–Miller memory-saving DP. [MAN, TIPS]
- `--sparsepickup n`: align a subset only; unused sequences are written to `input.notused`. [src]
- `--lhlimit n`: limit the size of temporary pairwise data. [src; the MPI page documents this as `--limitlh`]
- `--focus`: focus flag passed to the pairwise stage. [src]

## Guide tree

- `--parttree`, `--dpparttree`, `--fastaparttree`: PartTree for very large inputs, using 6-mer, DP or FASTA distances. [MAN, TIPS, TREEOUT, EP]
- `--partsize n`: PartTree partition size (default 50). [MAN, TIPS]
- `--groupsize n`: maximum sequences per aligned group with PartTree; `--groupsize 1` sorts without aligning. [MAN, TIPS]
- `--treein file`: user-supplied guide tree in MAFFT format. [TREEIN, MERGE, REGION]
- `--treeout`: write the guide tree to `input.tree`. [MAN, TIPS, TREEOUT, REGION]
- `--nodeout`: tree output with node information (implies `--treeout`). [src]
- `--distout`: write the distance matrix to `input.hat2`. [src]
- `--averagelinkage`: UPGMA tree. [TREEOUT]
- `--minimumlinkage`: single-linkage tree. [TREEOUT]
- `--mixedlinkage x`: mixed linkage with weight x (mixed linkage is the default). [src]
- `--youngestlinkage`: youngest-linkage tree. [src]
- `--pileup`: align in input order. [TIPS]
- `--randomchain`: align in a random order. [TIPS]
- `--randomseed n`: random-number seed. [TIPS]
- `--memsavetree`: low-memory guide-tree construction. [TIPS]
- `--memsavetreex`: a variant of `--memsavetree`. [src]
- `--large`: keep G-/L-/E-INS-1 temporary data on disk instead of RAM; used with `--mpi`. [TIPS, MPI]
- `--stepadd`: step-by-step addition order. [src]
- `--topin file`: disabled; exits with a note about a bug in versions before 6.530. [src]

## Scoring: gaps

- `--op x`: gap-opening penalty for group-to-group alignment (default 1.53). [MAN, ALG]
- `--ep x`: offset, which acts like a gap-extension penalty (default 0.0 now; 0.123 in older versions). [MAN, ALG, EP, TIPS0]
- `--exp x`: gap-extension penalty for group-to-group alignment. [src]
- `--opdist x`: gap-opening penalty for the distance stage (defaults to `--op`). [src]
- `--lop x`, `--lep x`, `--lexp x`: gap parameters for local pairwise alignment. [MAN]
- `--LOP x`, `--LEXP x`: penalties for skipping a segment with `--genafpair`. [MAN]
- `--gop x`, `--gep x`, `--gexp x`: gap parameters for global pairwise alignment. [src]
- `--GOP x`, `--GEXP x`: further gap parameters for the generalized-affine pairwise stage. [src]
- `--termgappenalty`: penalize terminal gaps. [src]
- `--legacygappenalty`, `--leavegappyregion`: both set the same internal flag; the web server calls it "Leave gappy regions". [src]
- `--allowshift`: allow "shifted" (unaligned) regions; sets `--unalignlevel 0.8` and shift penalty 2.0 unless given; needs `--globalpair`. [CL (v7.486 entry); src]
- `--shiftpenalty x`: penalty for shifts with `--allowshift` (must be > 1). [src]
- `--unalignlevel x`: 0–1; leaves poorly matching regions unaligned; `--globalpair` only. [src; the web server describes "Unalignlevel"]
- `--similaritylevel x`: −1 to +1; shifts the gap offsets; cannot be combined with `--unalignlevel`. [src]

## Scoring: substitution matrices

- `--bl n`: BLOSUM 30/45/62/80 (default 62). [MAN]
- `--jtt n`: JTT PAM n. [MAN]
- `--tm n`: transmembrane PAM n. [MAN, REGION]
- `--aamatrix file`: user amino-acid matrix in BLAST format. [MAN]
- `--kimura n`: nucleotide PAM-n matrix (the web server offers 1, 20, 200 PAM with κ = 2). [src]
- `--kappa x`: transition/transversion ratio for nucleotide matrices. [src]
- `--fmodel`: incorporate composition into the matrix. [MAN]
- `--nwildcard`: treat N as a wildcard. [src; web-server label]
- `--nzero`: N contributes nothing to the score. [src; web-server label]
- `--text`: align non-biological text (any printable characters). [ANYSYM, TEXT]
- `--textmatrix file`: user scoring matrix for `--text` mode (v7.371+). [TEXT, CL]

## Adding, merging and seeds

- `--add file`: add full-length unaligned sequences to an existing alignment. [ADD, TIPS4, VIRAL]
- `--addfragments file`: add fragmentary sequences. [ADD, TIPS4, VIRAL, SRV-ADD]
- `--addprofile file`: add an aligned profile. [ADD, TIPS4]
- `--addfull file`: full-length addition mode (named, not explained). [ADD]
- `--addlong file`: experimental: add long sequences to a short MSA. [SRV-ADD]
- `--keeplength`: keep the alignment length; delete insertions in the added sequences. [ADD, VIRAL]
- `--mapout`: write a position correspondence table (`.map`); implies `--keeplength`. [ADD]
- `--mapoutfile file`: `--mapout` to a named file. [src]
- `--compactmapout`: compact `.map` of insertion positions (v7.496+). [ADD, CL, SRV-FRAG]
- `--smoothing`: smoothing option for the addition step. [src]
- `--maxambiguous x`: drop sequences whose fraction of ambiguous characters exceeds x (v7.473+); later also collapses runs of n/X (v7.505). [CL, VIRAL]
- `--seed file`: seed alignment(s) whose aligned letters are preserved; repeatable. [MAN, TIPS4, MERGE]
- `--seedtable file`: table describing the seeds. [src]
- `--merge table`: merge sub-MSAs, keeping each one intact. [MERGE]
- `--anchors file`: user-supplied anchor points. [src]
- `--skipanchorsremoterthan n`: maximum gap between anchors. [src]
- `--core`, `--coreext`, `--corethr x`, `--corewin n`: extract or mark the conserved "core" columns (post-processing). [src]

## Input and output

- `--nuc`, `--amino`: force the sequence type (default: auto-detect). [MAN, ANYSYM]
- `--anysymbol`: accept unusual printable symbols (U, O, # …). [ANYSYM, TEXT]
- `--preservecase`: keep input upper/lower case; internally equivalent to `--anysymbol`. [PRESCASE, ANYSYM]
- `--adjustdirection`: reverse-complement sequences as needed, by 6-mer counting. [ADJDIR, CL]
- `--adjustdirectionaccurately`: the same, by DP (slower). [ADJDIR]
- `--clustalout`: Clustal-format output. [MAN, TEXT]
- `--phylipout`: PHYLIP-format output. [src]
- `--namelength n`: name length in Clustal output. [src]
- `--linelength n`: FASTA line length (default 60; −1 = one line per sequence; v7.510+). [CL]
- `--inputorder`: output in input order (default). [MAN]
- `--reorder`: output in aligned order. [MAN, TREEOUT]
- `--out file`: write output to a file. [src]
- `--quiet`: suppress progress messages. [MAN, STDERR]
- `--progress file`: write progress to a file (absolute path). [STDERR, CL]
- `--scoreout`: report the alignment score. [src]
- `--outnum`: number the output names. [src]
- `--debug`: keep debugging output. [src]

## Parallel execution

- `--thread n`: threads (`-1` = auto). [MT, MPI, TIPS]
- `--threadtb n`: threads for the progressive step. [MT, MPIHYB]
- `--threadit n`: threads for iterative refinement (`0` gives reproducible results). [MT, MPI]
- `--mpi`: MPI version of G-/L-/E-INS-1 (with `--large`). [MPI, MPIHYB]

## DASH and structure

- `--dash`: add structural homologs from the DASH server and align with them. [DASH]
- `--originalseqonly`: with `--dash`, output only the input sequences. [DASH]
- `--excludehomologs`: filter added homologs out of the DASH set. [src]
- `--strdir dir`: structure directory (parsed but not used in v7.471). [src]
- `--pdbidlist file`, `--pdbfilelist file`: disabled since Dec 2018; exit with "temporarily unavailable". [src]

## Notes

- **Version coverage.** The parsed options come from v7.471. `--maxambiguous`, `--compactmapout` and `--linelength` were added later and are taken from the changelog. The changelog says changes from v7.520 on are recorded only in the GitLab repository, which I couldn't reach, so options added in 7.520–7.526 may be missing.
- **Commented-out options** (`--enrich`, `--enrichseq`, `--enrichstr`) exist in the source but do nothing, so they are left out.
- **Inconsistencies in the docs.** The MPI page documents `--limitlh`, but the v7.471 parser only knows `--lhlimit`. The MPI pages also disagree with the multithreading page about what `--threadtb` and `--threadit` control.
- **Wrapper commands** (`linsi`, `ginsi`, `einsi`, `fftns`, `fftnsi`, `nwns`, `nwnsi`, `mafft-qinsi`, `mafft-xinsi`, `mafft-profile`) are presets for the options above [ALG]. `mafft-homologs.rb` and `mafft-sparsecore.rb` have their own separate options.

## Where the options are documented

- **MAN**: Manual (written for v6.2xx): https://mafft.cbrc.jp/alignment/software/manual/manual.html
- **ALG**: Algorithms: https://mafft.cbrc.jp/alignment/software/algorithms/algorithms.html
- **TIPS**: Tips for large data: https://mafft.cbrc.jp/alignment/software/tips.html
- **TIPS0**: Tips index: https://mafft.cbrc.jp/alignment/software/tips0.html
- **TIPS4**: Seed / add / addprofile: https://mafft.cbrc.jp/alignment/software/tips4.html
- **ADD**: Adding sequences: https://mafft.cbrc.jp/alignment/software/addsequences.html
- **MERGE**: Merge: https://mafft.cbrc.jp/alignment/software/merge.html
- **REGION**: Regional realignment: https://mafft.cbrc.jp/alignment/software/regionalrealignment.html
- **VIRAL**: Closely related viral genomes: https://mafft.cbrc.jp/alignment/software/closelyrelatedviralgenomes.html
- **TREEOUT**: Guide-tree output: https://mafft.cbrc.jp/alignment/software/treeout.html
- **TREEIN**: Guide-tree input: https://mafft.cbrc.jp/alignment/software/treein.html
- **ANYSYM**: Unusual symbols: https://mafft.cbrc.jp/alignment/software/anysymbol.html
- **PRESCASE**: Preserve case: https://mafft.cbrc.jp/alignment/software/preservecase.html
- **TEXT**: Text comparison: https://mafft.cbrc.jp/alignment/software/textcomparison.html
- **ADJDIR**: Adjust direction: https://mafft.cbrc.jp/alignment/software/adjustdirection.html
- **EP**: The `--ep` value: https://mafft.cbrc.jp/alignment/software/epvalue.html
- **NCRNA**: ncRNA (Q-INS-i / X-INS-i): https://mafft.cbrc.jp/alignment/software/source66.html
- **MT**: Multithreading: https://mafft.cbrc.jp/alignment/software/multithreading.html
- **MPI**: MPI version: https://mafft.cbrc.jp/alignment/software/mpi.html
- **MPIHYB**: MPI hybrid: https://mafft.cbrc.jp/alignment/software/mpihybrid.html
- **DASH**: DASH: https://mafft.cbrc.jp/alignment/software/dash.html
- **STDERR**: stderr workaround: https://mafft.cbrc.jp/alignment/software/stderr.html
- **CL**: Changelog: https://mafft.cbrc.jp/alignment/software/changelog.html
- **SRV-ADD**: Online `--add` / `--addlong`: https://mafft.cbrc.jp/alignment/server/add.html
- **SRV-FRAG**: Online `--addfragments`: https://mafft.cbrc.jp/alignment/server/add_fragments.html
- Web-server settings page (labels for unalignlevel, gappy regions, nwildcard/nzero, matrices): https://mafft.cbrc.jp/alignment/server/index.html
- **src**: Source (`core/mafft.tmpl`). Current: https://gitlab.com/sysimm/mafft. v7.471 mirror used here: https://github.com/GSLBiotech/mafft
- Katoh & Frith (2012), *Adding unaligned sequences into an existing alignment using MAFFT and LAST* (LAST-based options): https://pmc.ncbi.nlm.nih.gov/articles/PMC3516148/

The same pages are also served from the mirror `https://imm.ifrec.osaka-u.ac.jp/alignment/…`.
