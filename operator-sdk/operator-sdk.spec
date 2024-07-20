Name:       operator-sdk
Version:    1.35.0
Release:    1%{?dist}
Summary:    SDK for building Kubernetes applications

License:    ASL 2.0
URL:        https://github.com/operator-framework/operator-sdk
Source0:    https://github.com/operator-framework/operator-sdk/releases/download/v%{version}/operator-sdk_linux_amd64
Source1:    https://github.com/operator-framework/operator-sdk/releases/download/v%{version}/checksums.txt
Source2:    https://github.com/operator-framework/operator-sdk/releases/download/v%{version}/checksums.txt.asc
Source3:    operator-sdk.gpg
ExclusiveArch: x86_64

BuildRequires: coreutils gnupg

%description
SDK for building Kubernetes applications. Provides high level APIs, useful 
abstractions, and project scaffolding.

%prep
%{gpgverify} --keyring='%{SOURCE3}' --signature='%{SOURCE2}' --data='%{SOURCE1}'
pushd %{_sourcedir}
sha256sum --ignore-missing -c %{SOURCE1}
popd

%setup -q -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/operator-sdk

%files
%{_bindir}/operator-sdk

%changelog
* Sat Jul 20 2024 Johan Kok <johan@fedoraproject.org> - 1.35.0-1
- Bumped to 1.35.0

* Fri Apr 12 2024 Johan Kok <johan@fedoraproject.org> - 1.34.1-1
- Bumped to 1.34.1

* Wed Jan 31 2024 Johan Kok <johan@fedoraproject.org> - 1.33.0-1
- Initial package.
