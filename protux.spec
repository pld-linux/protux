Summary:	Professional Audio Tools
Summary(pl.UTF-8):	Profesjonalne Narzędzia Audio
Name:		protux
Version:	0.20.1
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://savannah.nongnu.org/download/protux/%{name}-%{version}.tar.gz
# Source0-md5:	9fe44d4df01309a52570c60c58a5a231
URL:		http://www.nongnu.org/protux/
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libmustux-devel >= 0.20.1
# checked for but not used
#BuildRequires:	libogg-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Protux aims to be the most practical and one of the most powerful
audio tools for Linux. Protux will allow you to use the power of
keyboard+mouse combination (with no clicks) to vastly speed up the
process of audio production. The authors call this concept
"Jog-Mouse-Board" or JMB, for short.

%description -l pl.UTF-8
Protux ma być najbardziej praktycznym i jednym z najpotężniejszych
narzędzi dźwiękowych dla Linuksa. Protux pozwoli na użycie potęgi
połączenia klawiatura+mysz (bez klikania), aby wybitnie przyspieszyć
proces produkcji dźwięku. Autorzy nazywają ten pomysł
"Jog-Mouse-Board", w skrócie JMB.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-mustux-lib-dir=%{_libdir} \
	--with-qt-lib-dir=%{_libdir}
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
