Name:       helm
Version:    2.16.3
Release:    1%{?dist}
Summary:    The Kubernetes Package Manager

License:    ASL 2.0
URL:        https://github.com/helm/helm
Source0:    https://get.helm.sh/helm-v%{version}-linux-amd64.tar.gz

%description
The Kubernetes Package Manager

Requires: bash

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/licenses/%{name}
mkdir -p %{buildroot}/%{_docdir}/%{name}

tar xzf %{_sourcedir}/helm-v%{version}-linux-amd64.tar.gz
install -p -m 755 linux-amd64/helm %{buildroot}/%{_bindir}
install -p -m 755 linux-amd64/tiller %{buildroot}/%{_bindir}
install -p -m 644 linux-amd64/LICENSE %{buildroot}/%{_datadir}/licenses/%{name}/
install -p -m 644 linux-amd64/README.md %{buildroot}/%{_docdir}/%{name}/

%files
%license LICENSE
%doc README.md
%{_bindir}/helm
%{_bindir}/tiller

%changelog
* Tue Feb 18 2019 Nicolas Steinmetz <contact@cerenit.fr> - 2.16.3-1
- Upgrade to 2.16.3

* Thu Nov 14 2019 Nicolas Steinmetz <contact@cerenit.fr> - 2.16.1-1
- Upgrade to 2.16.1

* Sat Nov 2 2019 Nicolas Steinmetz <contact@cerenit.fr> - 2.15.2-1
- Upgrade to 2.15.2

* Thu Oct 24 2019 Nicolas Steinmetz <contact@cerenit.fr> - 2.15.0-1
- Upgrade to 2.15.0

* Wed Sep 04 2019 Nicolas Steinmetz <contact@cerenit.fr> - 2.14.3-1
- Upgrade to 2.14.3

* Thu Apr 04 2019 Nicolas Steinmetz <contact@cerenit.fr> - 2.13.1-1
- Initial package.
