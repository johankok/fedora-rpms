Name:       helm
Version:    3.16.1
Release:    1%{?dist}
Summary:    The Kubernetes Package Manager

License:    ASL 2.0
URL:        https://github.com/helm/helm
Source0:    https://get.helm.sh/helm-v%{version}-linux-amd64.tar.gz
Source1:    https://github.com/helm/helm/releases/download/v%{version}/helm-v%{version}-linux-amd64.tar.gz.asc
Source2:    helm.gpg
ExclusiveArch: x86_64

BuildRequires: gnupg

%description
The Kubernetes Package Manager

Requires: bash

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -c -T
tar --strip-components=1 -zxf %{SOURCE0}


%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 helm %{buildroot}/%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/helm

%changelog
* Sat Sep 13 2024 Johan Kok <johan@fedoraproject.org> - 3.16.1-1
- Bumped to 3.16.1

* Sat Jul 20 2024 Johan Kok <johan@fedoraproject.org> - 3.15.3-1
- Bumped to 3.15.3

* Fri Apr 12 2024 Johan Kok <johan@fedoraproject.org> - 3.14.4-1
- Bumped to 3.14.4

* Mon Mar 18 2024 Johan Kok <johan@fedoraproject.org> - 3.14.3-1
- Bumped to 3.14.3

* Sat Jan 20 2024 Johan Kok <johan@fedoraproject.org> - 3.14.0-1
- Bumped to 3.14.0

* Sat Dec 23 2023 Johan Kok <johan@fedoraproject.org> - 3.13.3-1
- Bumped to 3.13.3

* Fri Nov 03 2023 Johan Kok <johan@fedoraproject.org> - 3.13.2-1
- Bumped to 3.13.2

* Sat Oct 14 2023 Johan Kok <johan@fedoraproject.org> - 3.13.1-1
- Bumped to 3.13.1

* Thu Sep 28 2023 Johan Kok <johan@fedoraproject.org> - 3.13.0-1
- Bumped to 3.13.0

* Fri Aug 11 2023 Johan Kok <johan@fedoraproject.org> - 3.12.3-1
- Bumped to 3.12.3

* Fri Jul 14 2023 Johan Kok <johan@fedoraproject.org> - 3.12.2-1
- Bumped to 3.12.2

* Thu Jun 15 2023 Johan Kok <johan@fedoraproject.org> - 3.12.1-1
- Bumped to 3.12.1

* Sun May 14 2023 Johan Kok <johan@fedoraproject.org> - 3.12.0-1
- Bumped to 3.12.0

* Wed Apr 12 2023 Johan Kok <johan@fedoraproject.org> - 3.11.3-1
- Bumped to 3.11.3

* Fri Mar 10 2023 Johan Kok <johan@fedoraproject.org> - 3.11.2-1
- Bumped to 3.11.2

* Sat Feb 11 2023 Johan Kok <johan@fedoraproject.org> - 3.11.1-1
- Bumped to 3.11.1

* Fri Jan 20 2023 Johan Kok <johan@fedoraproject.org> - 3.11.0-1
- Bumped to 3.11.0

* Fri Nov 18 2022 Johan Kok <johan@fedoraproject.org> - 3.10.2-1
- Bumped to 3.10.2

* Mon Oct 24 2022 Johan Kok <johan@fedoraproject.org> - 3.10.1-1
- Bumped to 3.10.1

* Sat Oct 08 2022 Johan Kok <johan@fedoraproject.org> - 3.10.0-1
- Bumped to 3.10.0

* Fri Aug 26 2022 Johan Kok <johan@fedoraproject.org> - 3.9.4-2
- Update packaging for README.md and LICENSE

* Fri Aug 26 2022 Johan Kok <johan@fedoraproject.org> - 3.9.4-1
- Bumped to 3.9.4

* Wed Aug 10 2022 Johan Kok <johan@fedoraproject.org> - 3.9.3-1
- Bumped to 3.9.3

* Sat Jul 23 2022 Johan Kok <johan@fedoraproject.org> - 3.9.2-1
- Bumped to 3.9.2

* Fri May 20 2022 Johan Kok <johan@fedoraproject.org> - 3.9.0-1
- Bumped to 3.9.0

* Fri Apr 15 2022 Johan Kok <johan@fedoraproject.org> - 3.8.2-1
- Bumped to 3.8.2

* Thu Mar 10 2022 Johan Kok <johan@fedoraproject.org> - 3.8.1-1
- Bumped to 3.8.1

* Fri Feb 18 2022 Johan Kok <johan@fedoraproject.org> - 3.8.0-1
- Bumped to 3.8.0

* Fri Dec 10 2021 Johan Kok <johan@fedoraproject.org> - 3.7.2-1
- Bumped to 3.7.2

* Fri Oct 15 2021 Johan Kok <johan@fedoraproject.org> - 3.7.1-1
- Bumped to 3.7.1

* Fri Sep 17 2021 Johan Kok <johan@fedoraproject.org> - 3.7.0-1
- Bumped to 3.7.0

* Fri Jul 16 2021 Johan Kok <johan@fedoraproject.org> - 3.6.3-1
- Bumped to 3.6.3

* Wed Jun 30 2021 Johan Kok <johan@fedoraproject.org> - 3.6.2-1
- Bumped to 3.6.2

* Thu Jun 17 2021 Johan Kok <johan@fedoraproject.org> - 3.6.1-1
- Upgrade to 3.6.1

* Sat May 29 2021 Johan Kok <johan@fedoraproject.org> - 3.6.0-1
- Upgrade to 3.6.0

* Thu Apr 15 2021 Johan Kok <johan@fedoraproject.org> - 3.5.4-1
- Upgrade to 3.5.4

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
