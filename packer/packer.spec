%define debug_package %{nil}

Name:	    packer
Version:	0.4.0
Release:	1%{?dist}
Summary:	Packer is a tool for creating identical machine images for multiple platforms from a single source configuration.

Group:		Development/Libraries
License:	MPL2
URL:		http://www.packer.io
Source0:	https://dl.bintray.com/mitchellh/packer/%{version}_linux_amd64.zip
BuildArch:  x86_64
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description

Packer is an open source tool for creating identical machine images 
for multiple platforms from a single source configuration.
Packer is lightweight, runs on every major operating system, and is
highly performant, creating machine images for multiple platforms
in parallel. Packer does not replace configuration management like 
Chef or Puppet. In fact, when building images, Packer is able to 
use tools like Chef or Puppet to install software onto the image.

%prep
%setup -T -c %{name}-%{version}
%{__install} -m 644 %{SOURCE0} .
unzip -d bin `basename %{SOURCE0}`
rm `basename %{SOURCE0}`

%build
exit 0

%install
rm -rf %{buildroot}
install -m755 -d %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/bin
cp -r bin/* %{buildroot}/usr/bin

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/*


%changelog
* Thu Dec 5 2013 Yuji Iwai <iwai.ug@gmail.com> 0.4.0-1
- Initial packaged
