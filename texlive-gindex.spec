Name:		texlive-gindex
Version:	52311
Release:	1
Summary:	Formatting indexes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gindex
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gindex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gindex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a way to generate the format of index
entries from within LaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/gindex
%{_texmfdistdir}/makeindex/gindex
%doc %{_texmfdistdir}/doc/latex/gindex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
