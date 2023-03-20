Name:       syft
Version:    0.75.0
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
