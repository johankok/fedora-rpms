Name:          step-cli
Version:       0.27.4
Release:       1%{?dist}
Summary:       A zero trust swiss army knife for working with X509, OAuth, JWT, OATH OTP, etc

License:       ASL 2.0
URL:           https://github.com/smallstep/cli/releases
Source0:       https://github.com/smallstep/cli/releases/download/v%{version}/step_linux_%{version}_amd64.tar.gz
ExclusiveArch: x86_64

%description
step is an easy-to-use CLI tool for building, operating, and automating Public
Key Infrastructure (PKI) systems and workflows. It's the client counterpart to
the step-ca online Certificate Authority (CA). You can use it for many common
crypto and X.509 operations—either independently, or with an online CA.

%prep
%autosetup -n step_%{version}

%install
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 bin/step %{buildroot}/%{_bindir}/step

%files
%{_bindir}/step
%license LICENSE
%doc README.md

%changelog
* Sun Sep 15 2024 Johan Kok <johan@fedoraproject.org> - 0.27.4-1
- Bumped to 0.27.4

* Sat Jul 20 2024 Johan Kok <johan@fedoraproject.org> - 0.27.2-1
- Bumped to 0.27.2

* Mon May 06 2024 Johan Kok <johan@fedoraproject.org> - 0.26.1-1
- Bumped to 0.26.1

* Fri Apr 12 2024 Johan Kok <johan@fedoraproject.org> - 0.26.0-1
- Bumped to 0.26.0

* Sat Jan 20 2024 Johan Kok <johan@fedoraproject.org> - 0.25.2-1
- Bumped to 0.25.2

* Sat Dec 02 2023 Johan Kok <johan@fedoraproject.org> - 0.25.1-1
- Bumped to 0.25.1

* Wed Oct 04 2023 Johan Kok <johan@fedoraproject.org> - 0.25.0-1
- Bumped to 0.25.0

* Sun May 14 2023 Johan Kok <johan@fedoraproject.org> - 0.24.4-1
- Bumped to 0.24.4

* Sat Apr 15 2023 Johan Kok <johan@fedoraproject.org> - 0.24.3-1
- Bumped to 0.24.3

* Fri Mar 10 2023 Johan Kok <johan@fedoraproject.org> - 0.23.4-1
- Bumped to 0.23.4

* Sun Mar 05 2023 Johan Kok <johan@fedoraproject.org> - 0.23.3-1
- Bumped to 0.23.3

* Sat Feb 11 2023 Johan Kok <johan@fedoraproject.org> - 0.23.2-1
- Bumped to 0.23.2

* Thu Nov 24 2022 Johan Kok <johan@fedoraproject.org> - 0.23.0-1
- Initial import

