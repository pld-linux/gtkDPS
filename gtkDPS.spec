Summary:	gtkDPS - GTK+ front-end for DPS.
Summary(pl):	gtkDPS - GTK+ front-end dla DPS
Name:		gtkDPS
Version:	0.3.3
Release:	1
Copyright:	GPL
Group:		X11/Utils
Group(pl):	X11/narzêdzia
Source0:	ftp://ftp.gyve.org/pub/%name/%name-%version.tar.gz
BuildRequires:	XFree86-devel >= 3.3.5
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	dgs >= 0.5.9
Requires:	dgs-config
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
gtkDPS is the set of functions, objects, and widgets to use DPS
easily with GTK.

%description -l pl
gtkDPS jest zestawem funkji, obiektów i widgetów stworzonych do 
³atwiejszego manipulowania DPSem z poziomu GTK.

%package devel
Summary:	gtkDPS devel	
Summary(pl):	gtkDPS devel
Group:		X11/Development
Group(pl):	X11/Programowanie

%description devel
Static library and include needed for user program.

%description -l pl devel
Biblioteka linkowana statycznei, pliki nag³ówkowe niezbêdne do poprawej
kompilacji programów.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf README NEWS TODO ChangeLog ABOUT-NLS HACKING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,NEWS,TODO,ChangeLog,ABOUT-NLS,HACKING}.gz
%attr(755,root,root) %{_bindir}/gtkDPS-config
%attr(644,root,root) %{_libdir}/libgtkDPS.so*

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_includedir}/gtkDPS/*.h
%attr(644,root,root) %{_libdir}/libgtkDPS.a
%attr(644,root,root) %{_datadir}/aclocal/gtkDPS.m4
