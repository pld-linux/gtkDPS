Summary:	gtkDPS - GTK+ front-end for DPS
Summary(pl):	gtkDPS - GTK+ front-end dla DPS
Name:		gtkDPS
Version:	0.3.4
Release:	2
License:	GPL
Group:		X11/Libraries
Source0:	ftp://ftp.gyve.org/pub/gtkDPS/%{name}-%{version}.tar.gz
Patch0:		%{name}-lib%{name}_la_LDFLAGS.patch
Patch1:		%{name}-am_fix.patch
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	dgs-devel >= 0.5.9
BuildRequires:	gettext-devel
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_aclocaldir	%(aclocal --print-ac-dir)

%description
gtkDPS is the set of functions, objects, and widgets to use DPS easily
with GTK.

%description -l pl
gtkDPS jest zestawem funkji, obiektów i widgetów stworzonych do
³atwiejszego manipulowania DPSem z poziomu GTK.

%package devel
Summary:	gtkDPS devel
Summary(pl):	gtkDPS dla programistów
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Headed files and documentation needed for compile programOB.

%description devel -l pl
Pliki nag³ówkowe i inne narzedzia niezbêdne przy kompilowaniu
programów u¿ywajacych gtkDPS.

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
%{__gettextize}
aclocal
%{__automake}
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf README NEWS TODO ChangeLog HACKING

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gtkDPS-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/gtkDPS
%{_aclocaldir}/gtkDPS.m4

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/lib*.a
