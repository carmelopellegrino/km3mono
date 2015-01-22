# $Id$
Name:           km3mono
Version:        3.2.8
Release:        1
Summary:        The Mono developing framework.

Group:          System Environment/Libraries
License:        Mixed (GNU GPL, GNU LGPL, MIT X11 and MPL)
URL:            http://www.mono-project.com/
Source0:        mono-3.2.8.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gcc-c++
Requires: bzip2
%description
Mono is a software platform designed to allow developers to easily create cross platform applications.

%prep
%setup -q -n mono-3.2.8

%build
./configure --prefix=$RPM_BUILD_ROOT/usr/local
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
make install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,-)
/usr/local/*

%changelog
