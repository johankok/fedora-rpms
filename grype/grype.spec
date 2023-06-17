Name:       grype
Version:    0.62.3
Release:    1%{?dist}
Summary:    A vulnerability scanner for container images and filesystems

License:    ASL 2.0
URL:        https://github.com/anchore/grype/releases
Source0:    https://github.com/anchore/grype/releases/download/v%{version}/%{name}_%{version}_linux_amd64.tar.gz
Source1:    https://github.com/anchore/grype/releases/download/v%{version}/%{name}_%{version}_checksums.txt
ExclusiveArch: x86_64

BuildRequires: coreutils

%description
A vulnerability scanner for container images and filesystems. Easily install
the binary to try it out. Works with Syft, the powerful SBOM (software bill
of materials) tool for container images and filesystems.

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
* Sat Jun 17 2023 Johan Kok <johan@fedoraproject.org> - 0.62.3-1
- Bumped to 0.62.3

* Tue Feb 07 2023 Johan Kok <johan@fedoraproject.org> - 0.56.0-1
- Initial import
