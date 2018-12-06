# https://github.com/google/go-cmp
%global goipath         github.com/google/go-cmp
Version:                0.2.0

%global common_description %{expand:
This package is intended to be a more powerful and safer alternative
to reflect.DeepEqual for comparing whether two values are semantically
equal.}

%gometa

Name:           golang-github-google-go-cmp
Release:        4%{?dist}
Summary:        Package for comparing Go values in tests
# Detected licences
# - BSD 3-clause "New" or "Revised" License at 'LICENSE'
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTING.md


%changelog
* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-4
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Ed Marshall <esm@logic.net> - 0.2.0-1
* Update to upstream release 0.2.0.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 19 2017 Ed Marshall <esm@logic.net> - 0.1.0-1
- First package for Fedora
