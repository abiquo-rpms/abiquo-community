%define abiquo_basedir /opt/abiquo

Name:     abiquo-community
Version:  1.7
Release:  4%{?dist}
Summary:  Abiquo Community Setup Metapackage
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source0:  README 
Source1:  exports
Source2:  smb.conf
Source3:  dhcpd.conf
Source4:  abiquo-community-install
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: dhcp nfs-utils samba abiquo-server-community abiquo-remote-services-community  abiquo-api-community
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package installs Abiquo Community Platform.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}/examples/
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
cp %{SOURCE0} $RPM_BUILD_ROOT/%{_docdir}/%{name}/
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_docdir}/%{name}/examples/
cp %{SOURCE2} $RPM_BUILD_ROOT/%{_docdir}/%{name}/examples/
cp %{SOURCE3} $RPM_BUILD_ROOT/%{_docdir}/%{name}/examples/
cp %{SOURCE4} $RPM_BUILD_ROOT/%{_sbindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/
%{_sbindir}/abiquo-community-install

%changelog
* Tue Feb 22 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-4
- updated abiquo-community-install script

* Tue Feb 22 2011 Sergio Rubio <rubiojr@frameos.org> - 1.7-3
- added abiquo-community-install script 

* Mon Feb 07 2011 Sergio Rubio <rubiojr@frameos.org> - 1.7-2
- remove post scripts, add sample files instead 

* Wed Feb 02 2011 Sergio Rubio <srubio@abiquo.com> - 1.7-1
- Initial release
