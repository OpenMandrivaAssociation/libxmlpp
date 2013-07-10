%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	2.6
%define major 	2
%define libname %mklibname xml++ %{api} %{major}
%define devname %mklibname -d xml++ %{api}

Summary: 	C++ interface for working with XML files
Name: 		libxml++
Version: 	2.36.0
Release: 	2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://libxmlplusplus.sf.net/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libxml++/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	doxygen
BuildRequires:	pkgconfig(libxml-2.0) >= 2.6.1 
BuildRequires:	pkgconfig(glibmm-2.4)

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

%package	-n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description	-n %{devname}
This package contains the headers that programmers will need to develop
applications which will use libraries from %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libxml++-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS README
%doc %{_datadir}/doc/%{name}-%{api}/reference
%{_datadir}/devhelp/books/%{name}-%{api}/%{name}-%{api}.devhelp2
%{_includedir}/*
%dir %{_libdir}/libxml++-%{api}/include
%{_libdir}/libxml++-%{api}/include/libxml++config.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

