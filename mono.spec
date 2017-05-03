# $Id$
%define debug_package %{nil}

Name:           km3mono
Version:        4.8.0.495
Release:        1
Summary:        The Mono developing framework.

Group:          System Environment/Libraries
License:        Mixed (GNU GPL, GNU LGPL, MIT X11 and MPL)
URL:            http://www.mono-project.com/
Source0:        mono-4.8.0.495.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gcc-c++ autoconf libtool automake gettext
Requires: bzip2
%description
Mono is a software platform designed to allow developers to easily create cross platform applications.

%prep
%setup -q -n mono-4.8.0

%build
./configure --prefix=/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/local/etc/mono
/usr/local/bin/
/usr/local/lib/
/usr/local/include/mono-2.0
/usr/local/share/man/
/usr/local/share/man/
/usr/local/share/
%changelog
