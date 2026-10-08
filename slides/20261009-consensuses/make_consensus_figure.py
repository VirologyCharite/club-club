"""Schematic of consensus calling from aligned reads (slide figure)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

matplotlib.rcParams["svg.fonttype"] = "none"
matplotlib.rcParams["font.family"] = "DejaVu Sans"

# ---------------------------------------------------------------- data
REF = "ACTGAGTCTAAGCGTACTGA"          # 20 sites; sites 9-12 deleted in sample
NO_COV = "N"                           # symbol used where there is no coverage

# Each row is a list of reads: (first column, clipped-left, aligned, clipped-right)
# "first column" is the 1-based column of the first *drawn* base (clips included).
ROWS = [
    [(1, "", "ATTGAGT", ""),      (14, "", "GAACTG", "")],
    [(1, "", "ATTAAGTC", "CGT"),  (14, "", "GTATT", "CT")],
    [(1, "", "ATTAA", ""),        (10, "GTC", "CGTACTG", "")],
    [(1, "TG", "TGAGTC", ""),     (11, "TC", "CGTATTG", "")],
    [(1, "", "ATTGAGTC", "CG"),   (15, "", "TACTG", "")],
]

IUPAC = {frozenset("AG"): "R", frozenset("CT"): "Y", frozenset("CG"): "S",
         frozenset("AT"): "W", frozenset("GT"): "K", frozenset("AC"): "M"}
THRESHOLD = 0.25                       # minor base must reach this to be reported


def call_consensus():
    counts = [dict() for _ in REF]
    for row in ROWS:
        for start, cl, al, cr in row:
            for k, b in enumerate(al):
                col = start + len(cl) + k          # 1-based
                counts[col - 1][b] = counts[col - 1].get(b, 0) + 1
    cons = []
    for c in counts:
        depth = sum(c.values())
        if depth == 0:
            cons.append(NO_COV)
            continue
        kept = frozenset(b for b, n in c.items() if n / depth >= THRESHOLD)
        cons.append(next(iter(kept)) if len(kept) == 1 else IUPAC[kept])
    return "".join(cons), counts


CONS, COUNTS = call_consensus()

# ---------------------------------------------------------------- style
COL = {"A": "#009E73", "C": "#0072B2", "G": "#E69F00", "T": "#C8102E"}
PALE = {"A": "#D5F0E8", "C": "#D3E6F3", "G": "#FBEBC8", "T": "#F7D6DB"}
AMBIG = "#6A3D9A"
GREY = "#B8B8B8"
INK = "#222222"
CELL = 0.90
FS = 27                                # base letter size (pt)


def cell(ax, col, y, base, kind="aligned"):
    x = col - 1 + (1 - CELL) / 2
    y0 = y - CELL / 2
    if kind == "clip":
        ax.add_patch(Rectangle((x, y0), CELL, CELL, facecolor=PALE[base],
                               edgecolor=COL[base], lw=1.8, ls=(0, (2.2, 1.6))))
        tc = COL[base]
    else:
        if base in COL:
            fc = COL[base]
        elif base == NO_COV:
            fc = GREY
        else:
            fc = AMBIG
        ax.add_patch(Rectangle((x, y0), CELL, CELL, facecolor=fc, edgecolor="none"))
        tc = "white"
    ax.text(col - 0.5, y - 0.02, base, ha="center", va="center", color=tc,
            fontsize=FS, fontweight="bold", family="DejaVu Sans Mono")


def outline(ax, c0, c1, y, color):
    pad = 0.03
    x = c0 - 1 + (1 - CELL) / 2 - pad
    w = (c1 - c0) + CELL + 2 * pad
    ax.add_patch(FancyBboxPatch((x, y - CELL / 2 - pad), w, CELL + 2 * pad,
                                boxstyle="round,pad=0,rounding_size=0.10",
                                facecolor="none", edgecolor=color, lw=4.0, zorder=5))


# ---------------------------------------------------------------- layout
Y_POS, Y_REF = 13.25, 12.25
Y_READ0, DY = 10.55, 1.08
Y_CONS = 4.75
XMIN, XMAX, YMIN, YMAX = -4.3, 21.6, 0.35, 13.85
SCALE = 16 / (XMAX - XMIN)
fig = plt.figure(figsize=(16, (YMAX - YMIN) * SCALE))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(XMIN, XMAX)
ax.set_ylim(YMIN, YMAX)
ax.axis("off")

# position numbers and reference
for i, b in enumerate(REF, start=1):
    ax.text(i - 0.5, Y_POS, str(i), ha="center", va="center", fontsize=17, color="#555555")
    cell(ax, i, Y_REF, b)
ax.text(-0.45, Y_REF, "Reference", ha="right", va="center", fontsize=25,
        fontweight="bold", color=INK)

# reads
row_y = [Y_READ0 - k * DY for k in range(len(ROWS))]
for y, row in zip(row_y, ROWS):
    for start, cl, al, cr in row:
        col = start
        for b in cl:
            cell(ax, col, y, b, "clip"); col += 1
        for b in al:
            cell(ax, col, y, b); col += 1
        for b in cr:
            cell(ax, col, y, b, "clip"); col += 1
ax.text(-0.45, (row_y[0] + row_y[-1]) / 2, "Aligned\nreads", ha="right", va="center",
        fontsize=25, fontweight="bold", color=INK, linespacing=1.15)

# matching soft-clip / flank pairs (rows 2 and 3)
y2, y3 = row_y[1], row_y[2]
outline(ax, 6, 8, y2, INK);    outline(ax, 10, 12, y3, INK)
outline(ax, 9, 11, y2, AMBIG); outline(ax, 13, 15, y3, AMBIG)
ax.plot([6.5, 6.5, 9.0], [y2 - CELL / 2 - 0.03, y3, y3], color=INK, lw=3,
        solid_capstyle="round", solid_joinstyle="round", zorder=4)
ax.plot([11.0, 12.5, 12.5], [y2, y2, y3 + CELL / 2 + 0.03], color=AMBIG, lw=3,
        solid_capstyle="round", solid_joinstyle="round", zorder=4)

# consensus
ax.plot([0, 20], [Y_CONS + 0.85, Y_CONS + 0.85], color="#999999", lw=1.5)
for i, b in enumerate(CONS, start=1):
    cell(ax, i, Y_CONS, b)
ax.text(-0.45, Y_CONS, "Consensus", ha="right", va="center", fontsize=25,
        fontweight="bold", color=INK)


def note(xc, text, level=0, x0=None, x1=None, color=INK):
    """Annotation under the consensus row; bracket if x0/x1 given, else a tick."""
    top = Y_CONS - CELL / 2 - 0.12
    ytxt = Y_CONS - 1.25 - 0.85 * level
    if x0 is not None:
        ax.plot([x0, x0, x1, x1], [top, top - 0.22, top - 0.22, top], color=color, lw=2.2)
        ax.plot([xc, xc], [top - 0.22, ytxt + 0.33], color=color, lw=2.2)
    else:
        ax.plot([xc, xc], [top, ytxt + 0.33], color=color, lw=2.2)
    ax.text(xc, ytxt, text, ha="center", va="center", fontsize=19, color=color)


note(1.5, "variant (C→T)", level=1)
note(3.5, "R = A or G", level=0, color=AMBIG)
note(10.0, "no coverage: deleted in sample", level=0, x0=8.1, x1=11.9, color="#666666")
note(16.5, "Y = C or T", level=0, color=AMBIG)
note(19.5, "no coverage", level=1, color="#666666")

# legend
yl = 1.05
cell(ax, 1, yl, "A")
ax.text(1.25, yl, "aligned base", ha="left", va="center", fontsize=19, color=INK)
cell(ax, 6, yl, "A", "clip")
ax.text(6.25, yl, "soft-clipped base (not used for consensus)", ha="left", va="center",
        fontsize=19, color=INK)

if __name__ == "__main__":
    print("REF ", REF)
    print("CONS", CONS)
    for i, c in enumerate(COUNTS, start=1):
        print(i, REF[i - 1], c)
    fig.savefig("consensus_calling.png", dpi=200, facecolor="white")
    fig.savefig("consensus_calling.svg", facecolor="white")
