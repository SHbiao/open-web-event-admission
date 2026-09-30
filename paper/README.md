# INS LaTeX draft

This directory is the first concise full-length manuscript draft for *Information Sciences*.

## Files

- `main.tex`: Elsevier `elsarticle` 5p two-column manuscript. The abstract is intentionally left as a TODO.
- `figures/pipeline.tex`: task and measurement-chain diagram.
- `figures/coverage.tex`: D2 score-coverage bar chart.
- `figures/retention_far.tex`: D2 Retention--FAR operating-point plot.
- `references.bib`: initial verified event-linking references; the related-work matrix still needs expansion.

## Compile

From this directory with TeX Live:

```text
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

The Windows TeX Live binary detected in this environment is `F:\\texlive\\2026\\bin\\windows\\pdflatex.exe`.

## Writing contract

The draft is intentionally argument-led rather than chronological. It starts with the observed admission gap, defines the units and policy, explains why the evidence is layered, then presents the frozen D2 result and its negative method comparison. No new experiment is introduced.

Before submission, complete only these writing tasks:

1. write the abstract after the body is stable;
2. expand and verify the related-work citations;
3. replace anonymous author metadata and add the repository URL after the anonymous release plan is fixed;
4. move long audit/hash material to an appendix or release package while retaining core denominators and failure rules in the paper;
5. run the current INS Guide for Authors and anonymous-submission checks.

The numbers in the manuscript are copied from the frozen F2/F3 records. In particular, Primary's 79/102 coverage means its full-set AUC/AUPRC are reported as NA, not replaced with conditional AUC.
