Summary:	Professional Audio Tools
Summary(pl):	Profesjonalne Narzêdzia Audio
Name:		protux
Version:	0.20.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Sound
#Source0:	http://savannah.nongnu.org/download/protux/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.gnu.org/savannah/files/protux/%{name}-%{version}.tar.gz
# Source0-md5:	dacb13bf1ef9b7a6cbed707a2af75eea
URL:		http://www.nongnu.org/protux/
Patch0:		%{name}-long.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libmustux-devel
BuildRequires:	libtool
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Protux aims to be the most practical and one of the most powerful
audio tools for Linux. Protux will allow you to use the power of
keyboard+mouse combination (with no clicks) to vastly speed up the
process of audio production. The authors call this concept
"Jog-Mouse-Board" or JMB, for short.

%description -l pl
Protux ma byæ najbardziej praktycznym i jednym z najpotê¿niejszych
narzêdzi d¼wiêkowych dla Linuksa. Protux pozwoli na u¿ycie potêgi
po³±czenia klawiatura+mysz (bez klikania), aby wybitnie przyspieszyæ
proces produkcji d¼wiêku. Autorzy nazywaj± ten pomys³
"Jog-Mouse-Board", w skrócie JMB.

%prep
%setup -q
#%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/protux
