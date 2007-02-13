Summary:	gtkDPS - GTK+ frontend for DPS
Summary(pl.UTF-8):	gtkDPS - frontend GTK+ dla DPS
Name:		gtkDPS
Version:	0.3.4
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.gyve.org/pub/gtkDPS/%{name}-%{version}.tar.gz
# Source0-md5:	59fdb6b71bf75e61a0a3477583e9ab98
Patch0:		%{name}-libgtkDPS_la_LDFLAGS.patch
Patch1:		%{name}-am_fix.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dgs-devel >= 0.5.9
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtkDPS is a set of functions, objects, and widgets to use DPS easily
with GTK.

%description -l pl.UTF-8
gtkDPS jest zestawem funkcji, obiektów i widgetów stworzonych do
łatwiejszego używania DPS-a z poziomu GTK.

%package devel
Summary:	gtkDPS development files
Summary(pl.UTF-8):	Pliki gtkDPS dla programistów
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header and other files needed for building programs that use gtkDPS.

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne niezbędne przy kompilowaniu programów
używających gtkDPS.

%package static
Summary:	gtkDPS static libraries
Summary(pl.UTF-8):	Biblioteki statyczne gtkDPS
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
gtkDPS static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne gtkDPS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

sed -e 's/AM_GTK_GNU_GETTEXT/AM_GNU_GETTEXT/' configure.in > configure.in.tmp
mv -v configure.in.tmp configure.in
rm -f acinclude.m4

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtkDPS-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gtkDPS
%{_aclocaldir}/gtkDPS.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
