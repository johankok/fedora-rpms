Name:       argocd
Version:    2.1.3
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
* Fri Oct 01 2021 Johan Kok <johan@fedoraproject.org> - 2.1.3-1
- Bumped to 2.1.3

* Sat Sep 04 2021 Johan Kok <johan@fedoraproject.org> - 2.1.2-1
- Bumped to 2.1.2

* Thu Aug 26 2021 Johan Kok <johan@fedoraproject.org - 2.1.1-1
- Bumped to 2.1.1

* Sat Jul 24 2021 Johan Kok <johan@fedoraproject.org> - 2.0.5-1
- Bumped to 2.0.5

* Wed Jun 23 2021 Johan Kok <johan@fedoraproject.org> - 2.0.4-1
- Bumped to 2.0.4

* Fri Jun 18 2021 Johan Kok <johan@fedoraproject.org> - 2.0.3-1
- Initial import
