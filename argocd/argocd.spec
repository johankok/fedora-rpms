Name:       	argocd
Version:    	2.10.10
Release:    	1%{?dist}
Summary:    	Declarative continuous deployment for Kubernetes

License:    	ASL 2.0
URL:        	https://github.com/argoproj/argo-cd/releases
Source0:    	https://github.com/argoproj/argo-cd/releases/download/v%{version}/argocd-linux-amd64
ExclusiveArch:	x86_64

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
* Wed May 22 2024 Johan Kok <johan@fedoraproject.org> - 2.10.10-1
- Bumped to 2.10.10

* Mon May 06 2024 Johan Kok <johan@fedoraproject.org> - 2.10.9-1
- Bumped to 2.10.9

* Fri Apr 12 2024 Johan Kok <johan@fedoraproject.org> - 2.10.6-1
- Bumped to 2.10.6

* Mon Mar 18 2024 Johan Kok <johan@fedoraproject.org> - 2.9.9-1
- Bumped to 2.9.9

* Sat Jan 20 2024 Johan Kok <johan@fedoraproject.org> - 2.8.9-1
- Bumped to 2.8.9

* Sat Dec 02 2023 Johan Kok <johan@fedoraproject.org> - 2.8.7-1
- Bumped to 2.8.7

* Fri Nov 17 2023 Johan Kok <johan@fedoraproject.org> - 2.8.6-1
- Bumped to 2.8.6

* Wed Oct 04 2023 Johan Kok <johan@fedoraproject.org> - 2.8.4-1
- Bumped to 2.8.4

* Fri Sep 15 2023 Johan Kok <johan@fedoraproject.org> - 2.7.14-1
- Bumped to 2.7.14

* Sat Aug 26 2023 Johan Kok <johan@fedoraproject.org> - 2.7.13-1
- Bumped to 2.7.13

* Tue Aug 08 2023 Johan Kok <johan@fedoraproject.org> - 2.7.11-1
- Bumped to 2.7.11

* Fri Jul 28 2023 Johan Kok <johan@fedoraproject.org> - 2.7.9-1
- Bumped to 2.7.9

* Wed Jul 19 2023 Johan Kok <johan@fedoraproject.org> - 2.7.8-1
- Bumped to 2.7.8

* Fri Jul 07 2023 Johan Kok <johan@fedoraproject.org> - 2.7.7-1
- Bumped to 2.7.7

* Thu Jun 22 2023 Johan Kok <johan@fedoraproject.org> - 2.7.6-1
- Bumped to 2.7.6

* Sat Jun 17 2023 Johan Kok <johan@fedoraproject.org> - 2.7.5-1
- Bumped to 2.7.5

* Wed May 24 2023 Johan Kok <johan@fedoraproject.org> - 2.7.3-1
- Bumped to 2.7.3

* Sun May 14 2023 Johan Kok <johan@fedoraproject.org> - 2.7.2-1
- Bumped to 2.7.2

* Sat May 06 2023 Johan Kok <johan@fedoraproject.org> - 2.7.1-1
- Bumped to 2.7.1

* Fri Mar 24 2023 Johan Kok <johan@fedoraproject.org> - 2.6.7-1
- Bumped to 2.6.7

* Mon Mar 20 2023 Johan Kok <johan@fedoraproject.org> - 2.6.6-1
- Bumped to 2.6.6

* Tue Feb 28 2023 Johan Kok <johan@fedoraproject.org> - 2.6.3-1
- Bumped to 2.6.3

* Fri Feb 17 2023 Johan Kok <johan@fedoraproject.org> - 2.6.2-1
- Bumped to 2.6.2

* Sat Feb 11 2023 Johan Kok <johan@fedoraproject.org> - 2.6.1-1
- Bumped to 2.6.1

* Fri Feb 03 2023 Johan Kok <johan@fedoraproject.org> - 2.5.10-1
- Bumped to 2.5.10

* Sat Jan 28 2023 Johan Kok <johan@fedoraproject.org> - 2.5.9-1
- Bumped to 2.5.9

* Wed Jan 25 2023 Johan Kok <johan@fedoraproject.org> - 2.5.8-1
- Bumped to 2.5.8

* Wed Jan 18 2023 Johan Kok <johan@fedoraproject.org> - 2.5.7-1
- Bumped to 2.5.7

* Thu Dec 08 2022 Johan Kok <johan@fedoraproject.org> - 2.5.4-1
- Bumped to 2.5.4

* Fri Nov 18 2022 Johan Kok <johan@fedoraproject.org> - 2.5.2-1
- Bumped to 2.5.2

* Wed Nov 02 2022 Johan Kok <johan@fedoraproject.org> - 2.4.16-1
- Bumped to 2.4.16

* Wed Nov 02 2022 Johan Kok <johan@fedoraproject.org> - 2.5.1-1
- Bumped to 2.5.1

* Mon Oct 24 2022 Johan Kok <johan@fedoraproject.org> - 2.4.15-1
- Bumped to 2.4.15

* Sat Oct 08 2022 Johan Kok <johan@fedoraproject.org> - 2.4.14-1
- Bumped to 2.4.14

* Sat Sep 17 2022 Johan Kok <johan@fedoraproject.org> - 2.4.12-1
- Bumped to 2.4.12

* Thu Aug 18 2022 Johan Kok <johan@fedoraproject.org> - 2.4.10-1
- Bumped to 2.4.10

* Fri Aug 12 2022 Johan Kok <johan@fedoraproject.org> - 2.4.9-1
- Bumped to 2.4.9

* Sat Jul 23 2022 Johan Kok <johan@fedoraproject.org> - 2.4.7-1
- Bumped to 2.4.7

* Wed Jul 13 2022 Johan Kok <johan@fedoraproject.org> - 2.4.6-1
- Bumped to 2.4.6

* Tue Jun 28 2022 Johan Kok <johan@fedoraproject.org> - 2.4.3-1
- Bumped to 2.4.3

* Fri Jun 24 2022 Johan Kok <johan@fedoraproject.org> - 2.4.2-1
- Bumped to 2.4.2

* Fri Jun 24 2022 Johan Kok <johan@fedoraproject.org> - 2.3.5-1
- Bumped to 2.3.5

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
