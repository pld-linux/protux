Summary:	empty
Name:		protux
Version:	0.16.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://savannah.nongnu.org/download/protux/%{name}-%{version}.tar.gz
#Source0-md5:	00653c37500c8b74ac9dbcad963f49c3
Source1:	%{name}-acinclude.m4
URL:		http://www.nongnu.org/protux/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
empty


%prep
%setup -q

%build
cp -f %{SOURCE1} acinclude.m4
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT/*

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
