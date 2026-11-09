# Bachelor's Thesis: Organizational Implications of the NIS2 Directive

Francesco Maria Fuligni · University of Bologna · Bachelor's degree in Informatics for Management · Academic year 2024/2025

Supervisor: Edoardo Mollona

This thesis examines how organizations can implement the NIS2 Directive. It compares the support offered by ISO/IEC 27001 and the NIST Cybersecurity Framework 2.0 and discusses the CISO's role in translating regulatory requirements into organizational decisions. The thesis and presentation are in Italian.

- [Thesis PDF](fuligni_francesco_maria_tesi.pdf)
- [Presentation slides](francescomaria.fuligni.presentazione.tesi.pdf)
- [Sources and links](fonti/references.md)
- [LaTeX source](elaborato/main.tex)

## Build from source

Install a TeX Live distribution with pdfLaTeX, BibTeX and the packages used by the thesis. You also need Make. From the repository root, run:

```sh
make
```

The build writes the PDF to `elaborato/main.pdf` and keeps auxiliary files in `elaborato/.build/`. To update the copy distributed at the repository root, run:

```sh
cp elaborato/main.pdf fuligni_francesco_maria_tesi.pdf
```
