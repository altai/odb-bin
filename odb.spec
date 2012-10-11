Name:		odb
Version:	1.0
Release:	1%{?dist}
Summary:        Object Data Base for cloud

Group:          Development/Languages
License:        Apache 2.0
Vendor:         Grid Dynamics Consulting Services, Inc.
URL:		http://www.griddynamics.com/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
Object Data Base package used for storing assets data in a cloud


%prep
%setup -q


%build


%install
install -d -m 750 %{buildroot}%{_sharedstatedir}/%{name}
install -d -m 750 %{buildroot}%{_localstatedir}/log/%{name}
install -d -m 755 %{buildroot}%{_datarootdir}
cp -a odb %{buildroot}%{_datarootdir}/
install -p -D -m 644 etc/odb.conf %{buildroot}%{_sysconfdir}/odb.conf
install -p -D -m 755 etc/odb.init %{buildroot}%{_initrddir}/odb


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc COPYING
%defattr(-,root,root,-)
%{_datarootdir}/odb
%{_initrddir}/odb
%config(noreplace) %{_sysconfdir}/odb.conf
%attr(750,root,root) %{_sharedstatedir}/%{name}
%attr(750,root,root) %{_localstatedir}/log/%{name}


%changelog

