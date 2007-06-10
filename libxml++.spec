%define version 2.18.1
%define release %mkrel 1

%define major 	2
%define api_version 2.6
%define libname %mklibname xml++ %{api_version}

Name: 		libxml++
Summary: 	C++ interface for working with XML files
Version: 	%{version}
Release: 	%{release}
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://libxmlplusplus.sf.net/
License:	LGPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/libxmlpp-%{version}-buildroot
BuildRequires:	libxml2-devel >= 2.6.1 glibmm2.4-devel >= 2.4.0
BuildRequires:	doxygen

%description
libxml++ is a C++ interface for working with XML files, using libxml
(gnome-xml) to parse and write the actual XML files. It has a simple
but complete API.

%package	-n %{libname}_%{major}
Summary: 	C++ interface for working with XML files
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Provides:	%{libname} = %{version}-%{release}

%description	-n %{libname}_%{major}
libxml++ is a C++ interface for working with XML files, using libxml
(gnome-xml) to parse and write the actual XML files. It has a simple
but complete API.

%package	-n %{libname}_%{major}-devel
Summary:	Headers for developing programs that will use %name
Group:		Development/C++
Provides:	%{libname}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname}_%{major} = %{version}

%description	-n %{libname}_%{major}-devel
This package contains the headers that programmers will need to develop
applications which will use libraries from %name.

%prep
%setup -q
aclocal
autoconf
automake -a -c

%build
%configure2_5x
%make

### Build doc
pushd docs/reference
  perl -pi -e 's/^(HAVE_DOT.*=) YES/$1 NO/' Doxyfile
  make all
popd

%install
rm -rf $RPM_BUILD_ROOT installed-docs
%makeinstall_std
mv %buildroot%_datadir/doc/libxml++-2.6/docs installed-docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname}_%{major} -p /sbin/ldconfig
%postun -n %{libname}_%{major} -p /sbin/ldconfig

%files -n %{libname}_%{major}
%defattr(-,root,root)
%{_libdir}/libxml++-%{api_version}.so.%{major}*

%files -n %{libname}_%{major}-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README installed-docs/*
%{_includedir}/*
%dir %_libdir/libxml++-%{api_version}
%_libdir/libxml++-%{api_version}/include/libxml++config.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_libdir}/*.a
%attr(644,root,root) %{_libdir}/*.la


