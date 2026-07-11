%global tl_name lastpackage
%global tl_revision 34481

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Indicates the last loaded package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lastpackage
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lastpackage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lastpackage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lastpackage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package may be used to define the last point where some code shall
be executed. Its provides a package name for use in package-placing
commands from the author's templatetools. Usage examples are provided in
the documentation.

