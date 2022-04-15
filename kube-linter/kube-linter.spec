Name:       kube-linter
Version:    0.2.6
Release:    1%{?dist}
Summary:    Static analysis tool that checks Kubernetes YAML files and Helm charts

License:    ASL 2.0
URL:        https://github.com/stackrox/kube-linter
Source0:    https://github.com/stackrox/kube-linter/releases/download/%{version}/kube-linter-linux.tar.gz

%description
KubeLinter is a static analysis tool that checks Kubernetes YAML files and Helm charts to ensure the applications represented in them adhere to best practices. 

%install
mkdir -p %{buildroot}/%{_bindir}

tar xzf %{_sourcedir}/kube-linter-linux.tar.gz
install -p -m 755 kube-linter %{buildroot}/%{_bindir}

%files
%{_bindir}/kube-linter

%changelog
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
