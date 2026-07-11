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
BuildSystem:	texlive
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

