Name:       helm
Version:    3.5.3
Release:    2%{?dist}
Summary:    The Kubernetes Package Manager

License:    ASL 2.0
URL:        https://github.com/helm/helm
Source0:    https://get.helm.sh/helm-v%{version}-linux-amd64.tar.gz
Source1:    https://github.com/helm/helm/releases/download/v%{version}/helm-v%{version}-linux-amd64.tar.gz.asc
Source2:    helm.gpg

BuildRequires: gnupg

%description
The Kubernetes Package Manager

Requires: bash

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/licenses/%{name}
mkdir -p %{buildroot}/%{_docdir}/%{name}

tar xzf %{_sourcedir}/helm-v%{version}-linux-amd64.tar.gz
install -p -m 755 linux-amd64/helm %{buildroot}/%{_bindir}
install -p -m 644 linux-amd64/LICENSE %{buildroot}/%{_datadir}/licenses/%{name}/
install -p -m 644 linux-amd64/README.md %{buildroot}/%{_docdir}/%{name}/

%files
%license LICENSE
%doc README.md
%{_bindir}/helm

%changelog
* Sun Apr 11 2021 Johan Kok <johan@fedoraproject.org> - 3.5.3-2
- Added gpgverify

* Sun Apr 11 2021 Johan Kok <johan@fedoraproject.org> - 3.5.3-1
- Upgrade to 3.5.3

* Tue Feb 18 2020 Nicolas Steinmetz <contact@cerenit.fr> - 2.16.3-1
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
