Name:       kind
Version:    0.23.0
Release:    1%{?dist}
Summary:    Kubernetes IN Docker - local clusters for testing Kubernetes

License:    ASL 2.0
URL:        https://github.com/kubernetes-sigs/kind/releases
Source0:    https://github.com/kubernetes-sigs/kind/releases/download/v%{version}/%{name}-linux-amd64
Source1:    https://github.com/kubernetes-sigs/kind/releases/download/v%{version}/%{name}-linux-amd64.sha256sum
ExclusiveArch: x86_64

BuildRequires: coreutils

%description
kind is a tool for running local Kubernetes clusters using Docker container
"nodes". kind was primarily designed for testing Kubernetes itself, but may
be used for local development or CI.

%prep
pushd %{_sourcedir}
sha256sum --ignore-missing -c %{SOURCE1}
popd

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Sat Jul 20 2024 Johan Kok <johan@fedoraproject.org> - 0.23.0-1
- Bumped to 0.23.0

* Fri Apr 12 2024 Johan Kok <johan@fedoraproject.org> - 0.22.0-1
- Bumped to 0.22.0

* Sat Dec 23 2023 Johan Kok <johan@fedoraproject.org> - 0.20.0-1
- Initial import
