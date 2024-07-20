Name:       kustomize
Version:    5.4.3
Release:    1%{?dist}
Summary:    Customization of kubernetes YAML configurations

License:    ASL 2.0
URL:        https://github.com/kubernetes-sigs/kustomize/releases
Source0:    https://github.com/kubernetes-sigs/kustomize/releases/download/%{name}%2Fv%{version}/%{name}_v%{version}_linux_amd64.tar.gz
Source1:    https://github.com/kubernetes-sigs/kustomize/releases/download/%{name}%2Fv%{version}/checksums.txt
ExclusiveArch: x86_64

BuildRequires: coreutils

%description
kustomize lets you customize raw, template-free YAML files for multiple 
purposes, leaving the original YAML untouched and usable as is.

kustomize targets kubernetes; it understands and can patch kubernetes style 
API objects. It's like make, in that what it does is declared in a file, and 
it's like sed, in that it emits edited text.

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
* Sat Jul 20 2024 Johan Kok <johan@fedoraproject.org> - 5.4.3-1
- Bumped to 5.4.3

* Mon May 06 2024 Johan Kok <johan@fedoraproject.org> - 5.4.1-1
- Bumped to 5.4.1

* Thu Dec 07 2023 Johan Kok <johan@fedoraproject.org> - 5.2.1-1
- Initial import
