Name:          minikube
Version:       1.33.1
Release:       1%{?dist}
Summary:       Minikube is a tool that makes it easy to run Kubernetes locally

Group:         Development Tools
URL:           https://github.com/kubernetes/minikube
License:       ASL 2.0
Source0:       https://github.com/kubernetes/minikube/releases/download/v%{version}/%{name}-linux-amd64
ExclusiveArch: x86_64
Requires:      docker-machine-driver-kvm2

%description
Minikube is a tool that makes it easy to run Kubernetes locally. Minikube
runs a single-node Kubernetes cluster inside a VM on your laptop for
users looking to try out Kubernetes or develop with it day-to-day.

%build

%prep
%setup -q -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Tue May 14 2024 Johan Kok <johan@fedoraproject.org> - 1.33.1-1
- Bumped to 1.33.1

* Sat Apr 20 2024 Johan Kok <johan@fedoraproject.org> - 1.33.0-1
- Bumped to 1.33.0

* Fri Nov 17 2023 Johan Kok <johan@fedoraproject.org> - 1.32.0-1
- Bumped to 1.32.0

* Sat Aug 19 2023 Johan Kok <johan@fedoraproject.org> - 1.31.2-1
- Bumped to 1.31.2

* Fri Jul 28 2023 Johan Kok <johan@fedoraproject.org> - 1.31.1-1
- Bumped to 1.31.1

* Wed Jul 19 2023 Johan Kok <johan@fedoraproject.org> - 1.31.0-1
- Bumped to 1.31.0

* Wed Apr 05 2023 Johan Kok <johan@fedoraproject.org> - 1.30.1-1
- Bumped to 1.30.1

* Tue Apr 04 2023 Johan Kok <johan@fedoraproject.org> - 1.30.0-1
- Bumped to 1.30.0

* Sat Jan 28 2023 Johan Kok <johan@fedoraproject.org> - 1.29.0-1
- Bumped to 1.29.0

* Fri Nov 04 2022 Johan Kok <johan@fedoraproject.org> - 1.28.0-1
- Bumped to 1.28.0

* Sat Oct 08 2022 Johan Kok <johan@fedoraproject.org> - 1.27.1-1
- Bumped to 1.27.1

* Sat Sep 17 2022 Johan Kok <johan@fedoraproject.org> - 1.27.0-1
- Bumped to 1.27.0

* Wed Aug 03 2022 Johan Kok <johan@fedoraproject.org> - 1.26.1-1
- Bumped to 1.26.1

* Sat Jul 23 2022 Johan Kok <johan@fedoraproject.org> - 1.26.0-1
- Bumped to 1.26.0

* Fri Feb 25 2022 Johan Kok <johan@fedoraproject.org> - 1.25.2-1
- Bumped to 1.25.2

* Sat Jan 22 2022 Johan Kok <johan@fedoraproject.org> - 1.25.1-1
- Bumped to 1.25.1

* Thu Jan 20 2022 Johan Kok <johan@fedoraproject.org> - 1.25.0-1
- Bumped to 1.25.0

* Fri Dec 10 2021 Johan Kok <johan@fedoraproject.org> - 1.24.0-1
- Bumped to 1.24.0

* Wed Sep 22 2021 Johan Kok <johan@fedoraproject.org> - 1.23.2-1
- Bumped to 1.23.2

* Fri Sep 17 2021 Johan Kok <johan@fedoraproject.org> - 1.23.1-1
- Bumped to 1.23.1

* Sat Sep 04 2021 Johan Kok <johan@fedoraproject.org> - 1.23.0-1
- Bumped to 1.23.0

* Thu Jul 08 2021 Johan Kok <johan@fedoraproject.org> - 1.22.0-1
- Bumped to 1.22.0

* Fri Jun 18 2021 Johan Kok <johan@fedoraproject.org> - 1.21.0-1
- Bumped to 1.21.0

* Fri May 07 2021 Johan Kok <johan@fedoraproject.org> - 1.20.0-1
- Bumped to 1.20.0

* Sat Apr 10 2021 Johan Kok <johan@fedoraproject.org> - 1.19.0-1
- Bumped to 1.19.0

* Sat Mar 06 2021 Johan Kok <johan@fedoraproject.org> - 1.18.1-1
- Bumped to 1.18.1

* Tue Mar  2 2021 Johan Kok <johan@fedoraproject.org> - 1.18.0-1
- Bumped to 1.18.0

* Thu Feb  4 2021 Johan Kok <johan@fedoraproject.org> - 1.17.1-1
- Bumped to 1.17.1

* Sat Dec 19 2020 Johan Kok <johan@fedoraproject.org> - 1.16.0-1
- Bumped to 1.16.0

* Sat Nov 14 2020 Johan Kok <johan@fedoraproject.org> - 1.15.0-1
- Bumped to 1.15.0

* Wed Oct 28 2020 Johan Kok <johan@fedoraproject.org> - 1.14.2-1
- Bumped to 1.14.2

* Mon Oct 26 2020 Johan Kok <johan@fedoraproject.org> - 1.14.1-1
- Bump to 1.14.1

* Sat Oct 17 2020 Johan Kok <johan@fedoraproject.org> - 1.14.0-1
- Bump to 1.14.0

* Fri Sep  4 2020 Johan Kok <johan@fedoraproject.org> - 1.13.0-1
- Bump to 1.13.0

* Thu Aug 13 2020 Johan Kok <johan@fedoraproject.org> - 1.12.3-1
- Bump to 1.12.3

* Wed Aug 05 2020 Johan Kok <johan@fedoraproject.org> - 1.12.2-1
- Bump to 1.12.2

* Sat Jul 18 2020 Johan Kok <johan@fedoraproject.org> - 1.12.1-1
- Bump to 1.12.1

* Sat Jul 11 2020 Johan Kok <johan@fedoraproject.org> - 1.12.0-1
- Bump to 1.12.0

* Sat May 30 2020 Johan Kok <johan@fedoraproject.org> - 1.11.0-1
- Bump to 1.11.0

* Sun May 17 2020 Johan Kok <johan@fedoraproject.org> - 1.10.1-1
- Bump to 1.10.1

* Thu Apr 30 2020 Johan Kok <johan@fedoraproject.org> - 1.9.2-1
- Bump to 1.9.2

* Thu Feb 20 2020 Johan Kok <johan@fedoraproject.org> - 1.7.3-1
- Bump to 1.7.3

* Mon Feb 17 2020 Sergi Jimenez <tripledes@fedoraproject.org> - 1.7.2-1
- Bump to 1.7.2

* Tue Jan 14 2020 Sergi Jimenez <tripledes@fedoraproject.org> - 1.6.2-1
- Bump to 1.6.2

* Fri Dec 13 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.6.1-1
- Bump to 1.6.1

* Wed Nov  6 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.5.2-1
- Bump to 1.5.2

* Tue Jul  2 2019 Edu Minguez <edu@linux.com> - 1.2.0-1
- Bump to 1.2.0

* Tue Jun 11 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.1.1-1
- Bump to 1.1.1

* Mon Jun  3 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.1.0-1
- Bump to 1.1.0

* Fri May  3 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.0.1-1
- Bump to 1.0.1

* Sun Mar 31 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 1.0.0-1
- Bump to 1.0.0

* Tue Mar 12 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.35.0-1
- Bump to 0.35.0

* Tue Mar  5 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.34.1-1
- Bump to 0.34.1

* Mon Jan 21 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.33.1-1
- Bump to 0.33.1

* Sun Jan 13 2019 Sergi Jimenez <tripledes@fedoraproject.org> - 0.32.0-1
- Bump to 0.32.0

* Wed Dec 12 2018 Sergi Jimenez <tripledes@fedoraproject.org> - 0.31.0-2
- Depend on docker-machine-driver-kvm2, as v1 is being deprecated.

* Wed Dec 12 2018 Sergi Jimenez <tripledes@fedoraproject.org> - 0.31.0-1
- Initial import
