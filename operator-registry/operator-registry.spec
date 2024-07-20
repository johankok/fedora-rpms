Name:		operator-registry
Version:	1.45.0
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
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/opm

%files
%{_bindir}/opm

%changelog
* Sat Jul 20 2024 Johan Kok <johan@fedoraproject.org> - 1.45.0-1
- Bumped to 1.45.0

* Mon May 06 2024 Johan Kok <johan@fedoraproject.org> - 1.40.0-1
- Bumped to 1.40.0

* Fri Apr 12 2024 Johan Kok <johan@fedoraproject.org> - 1.39.0-1
- Bumped to 1.39.0

* Mon Mar 18 2024 Johan Kok <johan@fedoraproject.org> - 1.37.0-1
- Bumped to 1.37.0

* Wed Jan 31 2024 Johan Kok <johan@fedoraproject.org> - 1.36.0-2
- Rename the CLI to opm

* Wed Jan 31 2024 Johan Kok <johan@fedoraproject.org> - 1.36.0-1
- Initial import

