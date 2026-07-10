%global tl_name bodeplot
%global tl_revision 79073

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1
Release:	%{tl_revision}.1
Summary:	Draw Bode, Nyquist and Nichols plots with gnuplot or pgfplots
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/bodeplot
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bodeplot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bodeplot.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bodeplot.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX package to plot Bode, Nichols, and Nyquist diagrams. It
provides added functionality over the similar bodegraph package: New
\BodeZPK and \BodeTF commands to generate Bode plots of any transfer
function given either poles, zeros, gain, and delay, or numerator and
denominator coefficients and delay Support for unstable poles and zeros.
Support for complex poles and zeros. Support for general stable and
unstable second order transfer functions. Support for both Gnuplot
(default) and pgfplots (package option pgf). Support for linear and
asymptotic approximation of magnitude and phase plots of any transfer
function given poles, zeros, and gain.

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bodeplot
%dir %{_datadir}/texmf-dist/source/latex/bodeplot
%dir %{_datadir}/texmf-dist/tex/latex/bodeplot
%doc %{_datadir}/texmf-dist/doc/latex/bodeplot/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bodeplot/bodeplot-doc.pdf
%doc %{_datadir}/texmf-dist/source/latex/bodeplot/bodeplot.dtx
%doc %{_datadir}/texmf-dist/source/latex/bodeplot/bodeplot.ins
%{_datadir}/texmf-dist/tex/latex/bodeplot/bodeplot-2024-02-06.sty
%{_datadir}/texmf-dist/tex/latex/bodeplot/bodeplot.sty
