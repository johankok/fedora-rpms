Name:       kubeseal
Version:    0.27.1
Release:    1%{?dist}
Summary:    CLI tool to encrypt secrets into a SealedSecret resource
License:    ASL 2.0

URL:        https://github.com/bitnami-labs/sealed-secrets/releases
Source0:    https://github.com/bitnami-labs/sealed-secrets/releases/download/v%{version}/%{name}-%{version}-linux-amd64.tar.gz
Source1:    https://github.com/bitnami-labs/sealed-secrets/releases/download/v%{version}/sealed-secrets_%{version}_checksums.txt
ExclusiveArch: x86_64

BuildRequires: coreutils

%description
Kubeseal is a CLI tool that generates a SealedSecret resource containing the
given secret.

%prep
pushd %{_sourcedir}
sha256sum --ignore-missing -c %{SOURCE1}
popd

%autosetup -c

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Sat Jul 20 2024 Johan Kok <johan@fedoraproject.org> - 0.27.1-1
- Bumped to 0.27.1

* Fri Apr 12 2024 Johan Kok <johan@fedoraproject.org> - 0.26.2-1
- Bumped to 0.26.2

* Sat Jan 20 2024 Johan Kok <johan@fedoraproject.org> - 0.25.0-1
- Bumped to 0.25.0

* Sat Dec 16 2023 Johan Kok <johan@fedoraproject.org> - 0.24.5-1
- Bumped to 0.24.5

* Fri Nov 17 2023 Johan Kok <johan@fedoraproject.org> - 0.24.4-1
- Bumped to 0.24.4

* Fri Nov 03 2023 Johan Kok <johan@fedoraproject.org> - 0.24.3-1
- Bumped to 0.24.3

* Mon Oct 16 2023 Johan Kok <johan@fedoraproject.org> - 0.24.2-1
- Bumped to 0.24.2

* Tue Oct 10 2023 Johan Kok <johan@fedoraproject.org> - 0.24.1-1
- Bumped to 0.24.1

* Wed Oct 04 2023 Johan Kok <johan@fedoraproject.org> - 0.24.0-1
- Bumped to 0.24.0

* Sat Aug 19 2023 Johan Kok <johan@fedoraproject.org> - 0.23.1-1
- Bumped to 0.23.1

* Wed Jul 19 2023 Johan Kok <johan@fedoraproject.org> - 0.23.0-1
- Bumped to 0.23.0

* Thu Jun 15 2023 Johan Kok <johan@fedoraproject.org> - 0.22.0-1
- Bumped to 0.22.0

* Mon May 15 2023 Johan Kok <johan@fedoraproject.org> - 0.21.0-1
- Bumped to 0.21.0

* Mon Mar 20 2023 Johan Kok <johan@fedoraproject.org> - 0.20.2-1
- Bumped to 0.20.2

* Mon Mar 20 2023 Johan Kok <johan@fedoraproject.org> - 0.20.1-1
- Bumped to 0.20.1

* Tue Feb 28 2023 Johan Kok <johan@fedoraproject.org> - 0.19.5
- Initial import
