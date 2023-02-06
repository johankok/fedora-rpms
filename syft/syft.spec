Name:       syft
Version:    0.70.0
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
* Mon Feb 06 2023 Johan Kok <johan@fedoraproject.org> - 0.70.0-1
- Initial import
