Name:       argocd
Version:    2.0.5
Release:    1%{?dist}
Summary:    Declarative continuous deployment for Kubernetes

License:    ASL 2.0
URL:        https://github.com/argoproj/argo-cd/releases
Source0:    https://github.com/argoproj/argo-cd/releases/download/v%{version}/argocd-linux-amd64

%description
Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes.

%prep
%setup -q -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Sat Jul 24 2021 Johan Kok <johan@fedoraproject.org> - 2.0.5-1
- Bumped to 2.0.5

* Wed Jun 23 2021 Johan Kok <johan@fedoraproject.org> - 2.0.4-1
- Bumped to 2.0.4

* Fri Jun 18 2021 Johan Kok <johan@fedoraproject.org> - 2.0.3-1
- Initial import
