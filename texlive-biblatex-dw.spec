# revision 31752
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-dw
# catalog-date 2013-09-23 15:23:00 +0200
# catalog-license lppl
# catalog-version 1.6a
Name:		texlive-biblatex-dw
Version:	1.6a
Release:	3
Summary:	Humanities styles for biblatex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-dw
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-dw.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-dw.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A small collection of styles for the biblatex package. It was
designed for citations in the humanities and offers some
features that are not provided by the standard biblatex styles.
The styles are dependent on biblatex (at least version 0.9b)
and cannot be used without it. Eine kleine Sammlung von Stilen
fur das Paket biblatex. Es ist auf geisteswissenschaftliche
Zitierweise zugeschnitten und bietet einige Funktionen, die von
den Standard-Stilen von biblatex nicht direkt bereitgestellt
werden. Biblatex-dw baut vollstandig auf biblatex auf und kann
nicht ohne biblatex (mindestens in der Version 0.9b) verwendet
werden.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-dw/bbx/authortitle-dw.bbx
%{_texmfdistdir}/tex/latex/biblatex-dw/bbx/footnote-dw.bbx
%{_texmfdistdir}/tex/latex/biblatex-dw/bbx/standard-dw.bbx
%{_texmfdistdir}/tex/latex/biblatex-dw/cbx/authortitle-dw.cbx
%{_texmfdistdir}/tex/latex/biblatex-dw/cbx/footnote-dw.cbx
%{_texmfdistdir}/tex/latex/biblatex-dw/cbx/standard-dw.cbx
%{_texmfdistdir}/tex/latex/biblatex-dw/lbx/english-dw.lbx
%{_texmfdistdir}/tex/latex/biblatex-dw/lbx/german-dw.lbx
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/CHANGES
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/LIESMICH
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/README
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/biblatex-dw-preamble.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/biblatex-dw-print.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/biblatex-dw-screen.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/biblatex-dw.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/biblatex-dw.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/de-biblatex-dw.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/de-biblatex-dw.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/examples/de-authortitle-dw.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/examples/de-authortitle-dw.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/examples/de-examples-dw.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/examples/de-footnote-dw.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/examples/de-footnote-dw.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/examples/en-authortitle-dw.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/examples/en-authortitle-dw.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/examples/en-footnote-dw.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/examples/en-footnote-dw.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-dw/examples/examples-dw.bib

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
