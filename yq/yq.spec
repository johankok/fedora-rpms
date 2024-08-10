Name:          yq
Version:       4.44.3
Release:       1%{?dist}
Summary:       A portable command-line YAML, JSON, XML, CSV and properties processor

License:       MIT
URL:           https://github.com/mikefarah/yq/releases
Source0:       https://github.com/mikefarah/yq/releases/download/v%{version}/yq_linux_amd64.tar.gz
ExclusiveArch: x86_64

%description
a lightweight and portable command-line YAML, JSON and XML processor. yq uses
jq like syntax but works with yaml files as well as json, xml, properties, csv
and tsv. It does not yet support everything jq does - but it does support the
most common operations and functions, and more is being added continuously.

%prep
%autosetup -c

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1/
%{__install} -m 755 yq_linux_amd64 %{buildroot}/%{_bindir}/%{name}
%{__install} -m 644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sat Aug 10 2024 Johan Kok <johan@fedoraproject.org> - 4.44.3-1
- Bumped to 4.44.3

* Sat Jul 20 2024 Johan Kok <johan@fedoraproject.org> - 4.44.2-1
- Bumped to 4.44.2

* Fri Apr 12 2024 Johan Kok <johan@fedoraproject.org> - 4.43.1-1
- Bumped to 4.43.1

* Mon Mar 18 2024 Johan Kok <johan@fedoraproject.org> - 4.40.7-1
- Bumped to 4.40.7

* Thu Jan 04 2024 Johan Kok <johan@fedoraproject.org> - 4.40.5-1
- Bumped to 4.40.5

* Sat Dec 02 2023 Johan Kok <johan@fedoraproject.org> - 4.40.3-1
- Bumped to 4.40.3

* Wed Oct 04 2023 Johan Kok <johan@fedoraproject.org> - 4.35.2-1
- Bumped to 4.35.2

* Fri Aug 11 2023 Johan Kok <johan@fedoraproject.org> - 4.35.1-1
- Bumped to 4.35.1

* Fri Jul 14 2023 Johan Kok <johan@fedoraproject.org> - 4.34.2-1
- Bumped to 4.34.2

* Wed May 24 2023 Johan Kok <johan@fedoraproject.org> - 4.34.1-1
- Bumped to 4.34.1

* Wed Apr 12 2023 Johan Kok <johan@fedoraproject.org> - 4.33.3-1
- Bumped to 4.33.3

* Fri Mar 31 2023 Johan Kok <johan@fedoraproject.org> - 4.33.2-1
- Bumped to 4.33.2

* Mon Mar 27 2023 Johan Kok <johan@fedoraproject.org> - 4.33.1-1
- Bumped to 4.33.1

* Sat Mar 18 2023 Johan Kok <johan@fedoraproject.org> - 4.32.2-1
- Bumped to 4.32.2

* Sun Mar 05 2023 Johan Kok <johan@fedoraproject.org> - 4.31.2-1
- Bumped to 4.31.2

* Mon Feb 20 2023 Johan Kok <johan@fedoraproject.org> - 4.31.1-1
- Bumped to 4.31.1

* Sat Feb 11 2023 Johan Kok <johan@fedoraproject.org> - 4.30.8-1
- Bumped to 4.30.8

* Mon Feb 06 2023 Johan Kok <johan@fedoraproject.org> - 4.30.4-2
- Update installed binaries

* Thu Nov 24 2022 Johan Kok <johan@fedoraproject.org> - 4.30.4-1
- Initial import
