Name:		texlive-bodeplot
Version:	69742
Release:	1
Summary:	Draw Bode, Nyquist and Nichols plots with gnuplot or pgfplots
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bodeplot
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bodeplot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bodeplot.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bodeplot.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX package to plot Bode, Nichols, and Nyquist
diagrams. It provides added functionality over the similar
bodegraph package: New \BodeZPK and \BodeTF commands to
generate Bode plots of any transfer function given either
poles, zeros, gain, and delay, or numerator and denominator
coefficients and delay Support for unstable poles and zeros.
Support for complex poles and zeros. Support for general stable
and unstable second order transfer functions. Support for both
Gnuplot (default) and pgfplots (package option pgf). Support
for linear and asymptotic approximation of magnitude and phase
plots of any transfer function given poles, zeros, and gain.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/bodeplot
%{_texmfdistdir}/tex/latex/bodeplot
%doc %{_texmfdistdir}/doc/latex/bodeplot

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
