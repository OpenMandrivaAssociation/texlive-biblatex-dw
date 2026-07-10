%global tl_name biblatex-dw
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7b
Release:	%{tl_revision}.1
Summary:	Humanities styles for BibLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-dw
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-dw.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-dw.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A small collection of styles for the BibLaTeX package. It was designed
for citations in the humanities and offers some features that are not
provided by the standard BibLaTeX styles. The styles are dependent on
BibLaTeX (at least version 0.9b) and cannot be used without it. Eine
kleine Sammlung von Stilen fur das Paket BibLaTeX. Es ist auf
geisteswissenschaftliche Zitierweise zugeschnitten und bietet einige
Funktionen, die von den Standard-Stilen von BibLaTeX nicht direkt
bereitgestellt werden. Das Paket baut vollstandig auf BibLaTeX auf und
kann nicht ohne BibLaTeX (mindestens in der Version 0.9b) verwendet
werden.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-dw
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-dw
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-dw/examples
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-dw/bbx
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-dw/cbx
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-dw/lbx
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/CHANGES
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/LIESMICH
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/biblatex-dw-preamble.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/biblatex-dw-print.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/biblatex-dw-screen.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/biblatex-dw.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/biblatex-dw.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/de-biblatex-dw.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/de-biblatex-dw.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/examples/de-authortitle-dw.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/examples/de-authortitle-dw.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/examples/de-examples-dw.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/examples/de-footnote-dw.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/examples/de-footnote-dw.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/examples/en-authortitle-dw.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/examples/en-authortitle-dw.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/examples/en-footnote-dw.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/examples/en-footnote-dw.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-dw/examples/examples-dw.bib
%{_datadir}/texmf-dist/tex/latex/biblatex-dw/bbx/authortitle-dw.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-dw/bbx/footnote-dw.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-dw/bbx/standard-dw.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-dw/cbx/authortitle-dw.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-dw/cbx/footnote-dw.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-dw/cbx/standard-dw.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-dw/lbx/english-dw.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-dw/lbx/german-dw.lbx
