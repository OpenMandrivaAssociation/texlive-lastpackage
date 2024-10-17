Name:		texlive-lastpackage
Version:	34481
Release:	2
Summary:	Indicates the last loaded package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lastpackage
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lastpackage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lastpackage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lastpackage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package may be used to define the last point where some
code shall be executed. Its provides a package name for use in
package-placing commands from the author's templatetools. Usage
examples are provided in the documentation.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/lastpackage
%{_texmfdistdir}/tex/latex/lastpackage
%doc %{_texmfdistdir}/doc/latex/lastpackage

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
