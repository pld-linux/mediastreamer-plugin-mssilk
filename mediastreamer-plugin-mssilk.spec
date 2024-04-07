Summary:	SILK audio codec for mediastreamer
Summary(pl.UTF-8):	Kodek dźwięku SILK dla mediastreamera
Name:		mediastreamer-plugin-mssilk
Version:	1.2.0
Release:	2
License:	GPL v2+
Group:		Libraries
#Source0Download: https://gitlab.linphone.org/BC/public/mssilk/-/tags
Source0:	https://gitlab.linphone.org/BC/public/mssilk/-/archive/%{version}/mssilk-%{version}.tar.bz2
# Source0-md5:	ae2b44566c7f66c32c8c0d698736afe1
Patch0:		%{name}-system-silk.patch
URL:		https://gitlab.linphone.org/BC/public/mssilk
BuildRequires:	SILK_SDK-devel >= 1.0.9
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	mediastreamer-devel >= 2.0.0
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
Requires:	SILK_SDK >= 1.0.9
Requires:	mediastreamer >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package supplies the mediastreamer plugin for the SILK audio
codec.

%description -l pl.UTF-8
Ten pakiet udostępnia wtyczkę mediastreamera do kodeka dźwięku SILK.

%prep
%setup -q -n mssilk-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/mediastreamer/plugins/libmssilk.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/mediastreamer/plugins/libmssilk.so*
