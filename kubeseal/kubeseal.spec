Name:       kubeseal
Version:    0.20.2
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
* Mon Mar 20 2023 Johan Kok <johan@fedoraproject.org> - 0.20.2-1
- Bumped to 0.20.2

* Mon Mar 20 2023 Johan Kok <johan@fedoraproject.org> - 0.20.1-1
- Bumped to 0.20.1

* Tue Feb 28 2023 Johan Kok <johan@fedoraproject.org> - 0.19.5
- Initial import