%global package_speccommit 4f7e6d5948466ec591325900df5c2e2d6877d8a8
%global usver 2.5.0
%global xsver 3
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global unversion 2_5_0

Summary: An XML parser library
Name: expat
Version: %(echo %{unversion} | sed 's/_/./g')
Release: %{?xsrel}%{?dist}
Source0: expat-2.5.0.tar.gz
URL: https://libexpat.github.io/
License: MIT
BuildRequires: autoconf, libtool, gcc-c++
BuildRequires: make

%description
This is expat, the C library for parsing XML, written by James Clark. Expat
is a stream oriented XML parser. This means that you register handlers with
the parser prior to starting the parse. These handlers are called when the
parser discovers the associated structures in the document being parsed. A
start tag is an example of the kind of structures for which you may
register handlers.

%package devel
Summary: Libraries and header files to develop applications using expat
Requires: expat%{?_isa} = %{version}-%{release}

%description devel
The expat-devel package contains the libraries, include files and documentation
to develop XML applications with expat.

%package static
Summary: expat XML parser static library
Requires: expat-devel%{?_isa} = %{version}-%{release}

%description static
The expat-static package contains the static version of the expat library.
Install it if you need to link statically with expat.

%prep
%autosetup -p1 -n libexpat-R_%{unversion}/expat
sed -i 's/install-data-hook/do-nothing-please/' lib/Makefile.am
./buildconf.sh

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure
%make_build

%install
%make_install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%check
make check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc AUTHORS Changes
%license COPYING
%{_bindir}/*
%{_libdir}/libexpat.so.1
%{_libdir}/libexpat.so.1.*
%if 0%{?xenserver} < 9
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/Changes
%endif

%files devel
%doc doc/reference.html doc/*.css examples/*.c
%{_libdir}/libexpat.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*.h
%{_libdir}/cmake/expat-%{version}

%files static
%{_libdir}/libexpat.a

%changelog
* Thu Feb 06 2025 Gerald Elder-Vass <gerald.elder-vass@cloud.com> - 2.5.0-3
- CA-405691: Enable expat build for XenServer 8 & 9

* Thu Jan 16 2025 XenServer Rebuild <rebuild@xenserver.com> - 2.5.0-2
- CP-53241: XenServer 9 rebuild

* Thu Dec 21 2023 Lin Liu <lin.liu@citrix.com> - 2.5.0-1
- First imported release

