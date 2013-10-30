%define _name redis
%define _unpackaged_files_terminate_build 0

Name:             %{_name}-cli
Version:          2.6.14
Release:          1%{?dist}
Summary:          Redis command line tool

Group:            Development/Tools
License:          BSD
URL:              http://redis.io
Source0:          http://redis.googlecode.com/files/%{_name}-%{version}.tar.gz
# Update configuration
BuildRoot:        %{_tmppath}/%{_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:    tcl >= 8.5

%description
Redis is an advanced key-value store. It is similar to memcached but the data
set is not volatile, and values can be strings, exactly like in memcached, but
also lists, sets, and ordered sets. All this data types can be manipulated with
atomic operations to push/pop elements, add/remove elements, perform server side
union, intersection, difference between sets, and so forth. Redis supports
different kind of sorting abilities.

%prep
%setup -q -n %{_name}-%{version}

%build
make %{?_smp_mflags} \
  DEBUG='' \
  CFLAGS='%{optflags}' \
  V=1 \
  all

%check
make test

%install
rm -fr %{buildroot}
make install PREFIX=%{buildroot}%{_prefix}

# Fix non-standard-executable-perm error
chmod 755 %{buildroot}%{_bindir}/%{_name}-*

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root,-)
%doc 00-RELEASENOTES BUGS CONTRIBUTING COPYING README MANIFESTO
%{_bindir}/redis-benchmark
%{_bindir}/redis-check-aof
%{_bindir}/redis-check-dump
%{_bindir}/redis-cli

%changelog
* Wed Oct 30 2013 Yuji Iwai <iwai@sonicmoov.com> - 2.6.13-1
- Initial

