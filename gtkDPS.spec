Summary:	gtkDPS - GTK+ front-end for DPS
Summary(pl):	gtkDPS - front-end GTK+ dla DPS
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtkDPS is a set of functions, objects, and widgets to use DPS easily
with GTK.

%description -l pl
gtkDPS jest zestawem funkji, obiektów i widgetów stworzonych do
³atwiejszego u¿ywania DPS-a z poziomu GTK.

%package devel
Summary:	gtkDPS development files
Summary(pl):	Pliki gtkDPS dla programistów
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Headed and other files needed for building programs that use gtkDPS.

%description devel -l pl
Pliki nag³ówkowe i inne niezbêdne przy kompilowaniu programów
u¿ywajacych gtkDPS.

%package static
Summary:	gtkDPS static libraries
Summary(pl):	Biblioteki statyczne gtkDPS
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
gtkDPS static libraries.

%description static -l pl
Biblioteki statyczne gtkDPS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal}
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
%attr(755,root,root) %{_libdir}/lib*.so*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtkDPS-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/gtkDPS
%{_aclocaldir}/gtkDPS.m4

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.a
