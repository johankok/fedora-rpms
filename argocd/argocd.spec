Name:       argocd
Version:    2.3.4
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
* Sat May 21 2022 Johan Kok <johan@fedoraproject.org> - 2.3.4-1
- Bumped to 2.3.4

* Fri May 20 2022 Johan Kok <johan@fedoraproject.org> - 2.2.9-1
- Bumped to 2.2.9

* Wed Mar 23 2022 Johan Kok <johan@fedoraproject.org> - 2.2.8-1
- Bumped to 2.2.8

* Thu Mar 10 2022 Johan Kok <johan@fedoraproject.org> - 2.2.7-1
- Bumped to 2.2.7

* Fri Feb 18 2022 Johan Kok <johan@fedoraproject.org> - 2.2.5-1
- Bumped to 2.2.5

* Thu Jan 20 2022 Johan Kok <johan@fedoraproject.org> - 2.2.3-1
- Bumped to 2.2.3

* Sat Jan 01 2022 Johan Kok <johan@fedoraproject.org> - 2.2.2-1
- Bumped to 2.2.2

* Fri Dec 17 2021 Johan Kok <johan@fedoraproject.org> - 2.2.1-1
- Bumped to 2.2.1

* Thu Dec 16 2021 Johan Kok <johan@fedoraproject.org> - 2.2.0-1
- Bumped to 2.2.0

* Tue Dec 14 2021 Johan Kok <johan@fedoraproject.org> - 2.1.8-1
- Bumped to 2.1.8

* Fri Dec 10 2021 Johan Kok <johan@fedoraproject.org> - 2.1.7-1
- Bumped to 2.1.7

* Thu Oct 28 2021 Johan Kok <johan@fedoraproject.org> - 2.1.6-1
- Bumped to 2.1.6

* Wed Oct 20 2021 Johan Kok <johan@fedoraproject.org> - 2.1.5-1
- Bumped to 2.1.5

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
