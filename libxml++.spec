%define version 2.34.2
%define release %mkrel 1

%define major 	2
%define api_version 2.6
%define libname %mklibname xml++ %{api_version} %major
%define libnamedev %mklibname -d xml++ %{api_version}

Name: 		libxml++
Summary: 	C++ interface for working with XML files
Version: 	%{version}
Release: 	%{release}
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
URL:		http://libxmlplusplus.sf.net/
License:	LGPLv2+
Group:		System/Libraries
BuildRoot:	%{_tmppath}/libxmlpp-%{version}-buildroot
BuildRequires:	libxml2-devel >= 2.6.1 glibmm2.4-devel >= 2.4.0
BuildRequires:	doxygen

%description
libxml++ is a C++ interface for working with XML files, using libxml
(gnome-xml) to parse and write the actual XML files. It has a simple
but complete API.

%package	-n %{libname}
Summary: 	C++ interface for working with XML files
Group:		System/Libraries

%description	-n %{libname}
libxml++ is a C++ interface for working with XML files, using libxml
(gnome-xml) to parse and write the actual XML files. It has a simple
but complete API.

%package	-n %{libnamedev}
Summary:	Headers for developing programs that will use %name
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}%{api_version}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes: %mklibname -d xml++ 2.6 2

%description	-n %{libnamedev}
This package contains the headers that programmers will need to develop
applications which will use libraries from %name.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libxml++-%{api_version}.so.%{major}*

%files -n %{libnamedev}
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%doc %_datadir/doc/%name-%{api_version}/reference
%_datadir/devhelp/books/%name-%{api_version}/%name-%{api_version}.devhelp2
%{_includedir}/*
%dir %_libdir/libxml++-%{api_version}
%_libdir/libxml++-%{api_version}/include/libxml++config.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la


