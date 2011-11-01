Name:		texlive-biblatex-dw
Version:	1.3c
Release:	1
Summary:	Humanities styles for biblatex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-dw
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-dw.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-dw.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A small collection of styles for the biblatex package. It was
designed for citations in the humanities and offers some
features that are not provided by the standard biblatex styles.
Biblatex-dw is dependent on biblatex (at least version 0.9b)
and cannot be used without it. (Biblatex-dw will work with the
full release version 1.0 of biblatex.) Eine kleine Sammlung von
Stilen fur das Paket biblatex. Es ist auf
geisteswissenschaftliche Zitierweise zugeschnitten und bietet
einige Funktionen, die von den Standard-Stilen von biblatex
nicht direkt bereitgestellt werden. Biblatex-dw baut
vollstandig auf biblatex auf und kann nicht ohne biblatex
(mindestens in der Version 0.9b) verwendet werden.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
