Name:       kube-linter
Version:    0.1.6
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
* Sun Apr 11 2021 Johan Kok <johan@fedoraproject.org> - 0.1.6-1
- Initial spec file
