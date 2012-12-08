%define major 	2
%define api	2.6
%define libname %mklibname xml++ %{api} %{major}
%define devname %mklibname -d xml++ %{api}

Name: 		libxml++
Summary: 	C++ interface for working with XML files
Version: 	2.36.0
Release: 	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://libxmlplusplus.sf.net/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

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
Provides:	%{name}%{api}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%mklibname -d xml++ 2.6 2

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
rm -f %{buildroot}%{_libdir}/*.la

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

