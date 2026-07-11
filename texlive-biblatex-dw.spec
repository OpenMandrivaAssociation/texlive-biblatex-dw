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
BuildSystem:	texlive
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

