Summary:	gtkDPS
Summary(pl):	gtkDPS
Name:		gtkDPS
Version:	0.3.3
Release:	1
Copyright:	GPL
Group:		X11/Utils
Group(pl):	X11/narzêdzia
Source0:	ftp://ftp.gyve.org/pub/%name/%name-%version.tar.gz
#Patch0:		
BuildRequires:	gtk-devel >= 1.2.6
BuildRequires:	dgs >= 0.5.9
Requires:	dgs-config
Buildroot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description


%description -l pl
 # optional package =====================

%package devel
Summary:	gtkDPS devel	
Summary(pl):	gtkDPS devel
Group:		X11/Development
Group(pl):	X11/Programowanie

%description devel

%description -l pl devel
 # end of optional package ==============

%prep
%setup -q

#%patch

%build
./configure --prefix=%{_prefix}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)

# optional package

%files devel
%defattr(644,root,root,755)
%doc
#%attr(,,)
#end of optional package

* %{date} PLD Team <pld-list@pld.org.pl>
All below listed persons can be reached on <cvs_login>@pld.org.pl

$Log: gtkDPS.spec,v $
Revision 1.1  2000-03-17 10:37:03  cieciwa
- first version of rpm,
- build rpm.
