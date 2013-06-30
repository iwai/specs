Name:           php54-phalcon
Version:        1.1.0
Release:        1%{?dist}
Summary:        PhalconPHP is a web framework delivered as a C extension
License:        BSD
URL:            http://phalconphp.com

Source0:        https://github.com/phalcon/cphalcon/archive/v%{version}.zip

BuildRequires:  gcc php54-devel php-pear
Requires:       php-pear
Requires:       php(zend-abi) >= 20090626 
Requires:       php(api) >= 20090626 

%description
PhalconPHP is a web framework delivered as a C extension 

%prep
%setup -q -n cphalcon-%{version}
cat > phalcon.ini << 'EOF'
; Enable phalcon extension module
extension = phalcon.so 
EOF

%build
%ifarch x86_64
cd build/64bits
%else
cd build/32bits
%endif
phpize
%configure --enable-phalcon
make %{?_smp_mflags}


%install
rm -rf %{buildroot} 
%ifarch x86_64
pushd build/64bits
%else
pushd build/32bits
%endif
make install INSTALL_ROOT=%{buildroot}
popd
%{__install} -D -m 644 phalcon.ini %{buildroot}%{php_inidir}/phalcon.ini

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{php_extdir}/phalcon.so
%config(noreplace) %{php_inidir}/phalcon.ini


%changelog
* Fri Jun 14 2013 Yuji Iwai <iwai.ug@gmail.com> 1.1.0-1
- First build

