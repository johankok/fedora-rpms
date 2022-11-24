Name:       step-cli
Version:    0.23.0
Release:    1%{?dist}
Summary:    A zero trust swiss army knife for working with X509, OAuth, JWT, OATH OTP, etc. 

License:    ASL 2.0
URL:        https://github.com/smallstep/cli/releases
Source0:    https://github.com/smallstep/cli/releases/download/v%{version}/step_linux_%{version}_amd64.tar.gz

%description
step is an easy-to-use CLI tool for building, operating, and automating Public Key Infrastructure (PKI) systems and workflows. It's the client counterpart to the step-ca online Certificate Authority (CA). You can use it for many common crypto and X.509 operations—either independently, or with an online CA.

%prep
%setup -q -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Thu Nov 24 2022 Johan Kok <johan@fedoraproject.org> - 0.23.0-1
- Initial import
