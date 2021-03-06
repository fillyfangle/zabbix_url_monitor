%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           url_monitor
Version:        2.0.0
Release:        1%{?dist}
Group:          Applications/Systems
Summary:        This is an external script for zabbix for monitoring restful endpoints for data.

License:        ASLv2
URL:            https://github.com/rackerlabs/zabbix_url_monitor
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  python-setuptools
Requires(pre):  shadow-utils
Requires:       python
Requires:       python-daemon
Requires:       python-setuptools
Requires:       python-requests
Requires:       python-requests-oauthlib
Requires:       python-argparse
Requires:       PyYAML

%define service_name %{name}d

%description
A zabbix plugin to perform URL endpoint monitoring for JSON and XML REST APIs, supporting multiple http auth mechinisms

%prep
%setup -q -n %{name}-%{version}

%build

%pre

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
%post

%preun

%postun

%files
%doc README.md
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/url_monitor.yaml
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}*.egg-info
%attr(0755,-,-) %{_bindir}/%{name}

%changelog
* Mon Jul 18 2016 Jonathan Kelley <jon.kelley@rackspace.com> - 1.0.0-1
- Spec now mock-build compatible by removing inline py code from spec.

* Fri Apr 29 2016 Jonathan Kelley <jon.kelley@rackspace.com> - 0.8.5-1
- First spec
