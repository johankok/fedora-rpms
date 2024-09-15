Name:       syft
Version:    1.12.2
Release:    1%{?dist}
Summary:    CLI tool and library for generating a Software Bill of Materials

License:    ASL 2.0
URL:        https://github.com/anchore/syft/releases
Source0:    https://github.com/anchore/syft/releases/download/v%{version}/%{name}_%{version}_linux_amd64.tar.gz
Source1:    https://github.com/anchore/syft/releases/download/v%{version}/%{name}_%{version}_checksums.txt
ExclusiveArch: x86_64

BuildRequires: coreutils

%description
Syft is a CLI tool and Go library for generating a Software Bill of Materials
(SBOM) from container images and filesystems.

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
* Sat Jul 20 2024 Johan Kok <johan@fedoraproject.org> - 1.12.2-1
- Bumped to 1.12.2

* Sat Jul 20 2024 Johan Kok <johan@fedoraproject.org> - 1.9.0-1
- Bumped to 1.9.0

* Mon May 06 2024 Johan Kok <johan@fedoraproject.org> - 1.3.0-1
- Bumped to 1.3.0

* Fri Apr 12 2024 Johan Kok <johan@fedoraproject.org> - 1.1.1-1
- Bumped to 1.1.1

* Sat Jan 20 2024 Johan Kok <johan@fedoraproject.org> - 0.101.1-1
- Bumped to 0.101.1

* Mon Oct 23 2023 Johan Kok <johan@fedoraproject.org> - 0.94.0-1
- Bumped to 0.94.0

* Sat Oct 14 2023 Johan Kok <johan@fedoraproject.org> - 0.93.0-1
- Bumped to 0.93.0

* Wed Oct 04 2023 Johan Kok <johan@fedoraproject.org> - 0.92.0-1
- Bumped to 0.92.0

* Sat Sep 02 2023 Johan Kok <johan@fedoraproject.org> - 0.89.0-1
- Bumped to 0.89.0

* Sat Aug 26 2023 Johan Kok <johan@fedoraproject.org> - 0.88.0-1
- Bumped to 0.88.0

* Fri Aug 18 2023 Johan Kok <johan@fedoraproject.org> - 0.87.1-1
- Bumped to 0.87.1

* Wed Aug 09 2023 Johan Kok <johan@fedoraproject.org> - 0.86.1-1
- Bumped to 0.86.1

* Fri Jul 14 2023 Johan Kok <johan@fedoraproject.org> - 0.85.0-1
- Bumped to 0.85.0

* Fri Jun 30 2023 Johan Kok <johan@fedoraproject.org> - 0.84.1-1
- Bumped to 0.84.1

* Thu Jun 22 2023 Johan Kok <johan@fedoraproject.org> - 0.84.0-1
- Bumped to 0.84.0

* Wed Jun 14 2023 Johan Kok <johan@fedoraproject.org> - 0.83.1-1
- Bumped to 0.83.1

* Wed May 24 2023 Johan Kok <johan@fedoraproject.org> - 0.82.0-1
- Bumped to 0.82.0

* Sat May 06 2023 Johan Kok <johan@fedoraproject.org> - 0.80.0-1
- Bumped to 0.80.0

* Sat Apr 22 2023 Johan Kok <johan@fedoraproject.org> - 0.79.0-1
- Bumped to 0.79.0

* Wed Apr 12 2023 Johan Kok <johan@fedoraproject.org> - 0.77.0-1
- Bumped to 0.77.0

* Fri Apr 07 2023 Johan Kok <johan@fedoraproject.org> - 0.76.1-1
- Bumped to 0.76.1

* Fri Mar 31 2023 Johan Kok <johan@fedoraproject.org> - 0.76.0-1
- Bumped to 0.76.0

* Mon Mar 20 2023 Johan Kok <johan@fedoraproject.org> - 0.75.0-1
- Bumped to 0.75.0

* Fri Mar 10 2023 Johan Kok <johan@fedoraproject.org> - 0.74.1-1
- Bumped to 0.74.1

* Sun Mar 05 2023 Johan Kok <johan@fedoraproject.org> - 0.74.0-1
- Bumped to 0.74.0

* Tue Feb 28 2023 Johan Kok <johan@fedoraproject.org> - 0.73.0-1
- Bumped to 0.73.0

* Tue Feb 28 2023 Johan Kok <johan@fedoraproject.org> - 0.72.1-1
- Bumped to 0.72.1

* Fri Feb 17 2023 Johan Kok <johan@fedoraproject.org> - 0.72.0-1
- Bumped to 0.72.0

* Fri Feb 10 2023 Johan Kok <johan@fedoraproject.org> - 0.71.0-1
- Bumped to 0.71.0

* Mon Feb 06 2023 Johan Kok <johan@fedoraproject.org> - 0.70.0-1
- Initial import
