Name:       kube-linter
Version:    0.6.8
Release:    1%{?dist}
Summary:    Static analysis tool that checks Kubernetes YAML files and Helm charts

License:    ASL 2.0
URL:        https://github.com/stackrox/kube-linter
Source0:    https://github.com/stackrox/kube-linter/releases/download/v%{version}/kube-linter-linux.tar.gz

%description
KubeLinter is a static analysis tool that checks Kubernetes YAML files and Helm charts to ensure the applications represented in them adhere to best practices.

%prep
%setup -q -c -T
tar xzf %{SOURCE0}

%install
mkdir -p %{buildroot}/%{_bindir}

install -p -m 755 kube-linter %{buildroot}/%{_bindir}

%files
%{_bindir}/kube-linter

%changelog
* Mon Mar 18 2024 Johan Kok <johan@fedoraproject.org> - 0.6.8-1
- Bumped to 0.6.8

* Fri Jan 26 2024 Johan Kok <johan@fedoraproject.org> - 0.6.6-1
- Bumped to 0.6.6

* Fri Nov 03 2023 Johan Kok <johan@fedoraproject.org> - 0.6.5-1
- Bumped to 0.6.5

* Wed May 24 2023 Johan Kok <johan@fedoraproject.org> - 0.6.4-1
- Bumped to 0.6.4

* Wed Apr 12 2023 Johan Kok <johan@fedoraproject.org> - 0.6.3-1
- Bumped to 0.6.3

* Thu Mar 16 2023 Johan Kok <johan@fedoraproject.org> - 0.6.1-1
- Bumped to 0.6.1

* Thu Jan 19 2023 Johan Kok <johan@fedoraproject.org> - 0.6.0-1
- Bumped to 0.6.0

* Thu Dec 08 2022 Johan Kok <johan@fedoraproject.org> - 0.5.1-1
- Bumped to 0.5.1

* Sat Sep 17 2022 Johan Kok <johan@fedoraproject.org> - 0.5.0-1
- Bumped to 0.5.0

* Sat Jul 23 2022 Johan Kok <johan@fedoraproject.org> - 0.4.0-1
- Bumped to 0.4.0

* Fri May 20 2022 Johan Kok <johan@fedoraproject.org> - 0.3.0-1
- Bumped to 0.3.0

* Fri Apr 15 2022 Johan Kok <johan@fedoraproject.org> - 0.2.6-1
- Bumped to 0.2.6

* Thu Oct 14 2021 Johan Kok <johan@fedoraproject.org> - 0.2.5-1
- Bumped to 0.2.5

* Thu Sep 23 2021 Johan Kok <johan@fedoraproject.org> - 0.2.4-1
- Bumped to 0.2.4

* Thu Aug 26 2021 Johan Kok <johan@fedoraproject.org> - 0.2.3-1
- Bumped to 0.2.3

* Wed May 19 2021 Johan Kok <johan@fedoraproject.org> - 0.2.2-1
- Bumped to version 0.2.2

* Wed May 05 2021 Johan Kok <johan@fedoraproject.org> - 0.2.1-1
- Bumped to version 0.2.1

* Sun Apr 11 2021 Johan Kok <johan@fedoraproject.org> - 0.1.6-1
- Initial spec file
