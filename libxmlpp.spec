%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api 5.0
%define major 1
%define libname %mklibname xml++
%define devname %mklibname -d xml++
%define oldlibname %mklibname xml++ 5.0
%define olderlibname %mklibname xml++ 2.6 2
%define olddevname %mklibname -d xml++ %{api}

Summary:	C++ interface for working with XML files
Name:		libxml++
Version:	5.4.0
Release:	3
License:	LGPLv2+
Group:		System/Libraries
Url:		https://libxmlplusplus.sf.net/
Source0:	https://download.gnome.org/sources/libxml++/%(echo %{version} |cut -d. -f1-2)/libxml++-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:	doxygen
BuildRequires:	pkgconfig(mm-common-libstdc++) >= 0.9.10
BuildRequires:	pkgconfig(libxml-2.0) >= 2.6.1 
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	docbook5-style-xsl
#BuildRequires:	docbook5-schemas
BuildRequires:	xsltproc
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	meson
BuildSystem:	meson

%description
libxml++ is a C++ interface for working with XML files, using libxml
to parse and write the actual XML files. It has a simple but complete API.

%package -n %{libname}
Summary:	C++ interface for working with XML files
Group:		System/Libraries
%rename %{oldlibname}
%rename %{olderlibname}

%description -n %{libname}
libxml++ is a C++ interface for working with XML files, using libxml
to parse and write the actual XML files. It has a simple but complete API.

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
%rename %{mklibname -d xml++ 2.6}
%rename %{olddevname}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use libraries from %{name}.

%files -n %{libname}
%{_libdir}/libxml++-%{api}.so.%{major}*

%files -n %{devname}
%doc ChangeLog NEWS README*
%{_includedir}/*
%dir %{_libdir}/libxml++-%{api}/include
%{_libdir}/libxml++-%{api}/include/libxml++config.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
