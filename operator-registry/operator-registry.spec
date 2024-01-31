Name:		operator-registry
Version:	1.36.0
Release:	1%{?dist}
Summary:	Operator Registry runs in a cluster to provide operator catalog data to OLM

License:	ASL 2.0
URL:		https://github.com/operator-framework/operator-registry/releases
Source0:	https://github.com/operator-framework/operator-registry/releases/download/v%{version}/linux-amd64-opm
Source1:	https://github.com/operator-framework/operator-registry/releases/download/v%{version}/checksums.txt
ExclusiveArch:	x86_64

BuildRequires: coreutils

%description
Operator Registry runs in a Kubernetes or OpenShift cluster to provide operator 
catalog data to Operator Lifecycle Manager.

%prep
pushd %{_sourcedir}
sha256sum --ignore-missing -c %{SOURCE1}
popd

%setup -q -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Wed Jan 31 2024 Johan Kok <johan@fedoraproject.org> - 1.36.0-1
- Initial import

