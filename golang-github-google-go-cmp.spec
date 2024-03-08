# Run tests in check section
%bcond_without check

# https://github.com/google/go-cmp
%global goipath		github.com/google/go-cmp
%global forgeurl	https://github.com/google/go-cmp
Version:		0.6.0

%gometa

Summary:	Package for comparing Go values in tests
Name:		golang-github-google-go-cmp

Release:	1
Source0:	https://github.com/google/go-cmp/archive/v%{version}/go-cmp-%{version}.tar.gz
URL:		https://github.com/google/go-cmp
License:	BSD-3-Clause
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildArch:	noarch

%description
This package is intended to be a more powerful and safer
alternative to reflect.DeepEqual for comparing whether
two values are semantically equal.

The primary features of cmp are:

 *  When the default behavior of equality does not suit
    the needs of the test, custom equality functions can
    override the equality operation. For example, an equality
    function may report floats as equal so long as they are
    within some tolerance of each other.

 *  Types that have an Equal method may use that method to
    determine equality. This allows package authors to
    determine the equality operation for the types that they
    define.

 *  If no custom equality functions are used and no Equal
    method is defined, equality is determined by recursively
    comparing the primitive kinds on both values, much like
    reflect.DeepEqual. Unlike reflect.DeepEqual, unexported
    fields are not compared by default; they result in panics
    unless suppressed by using an Ignore option (see
    cmpopts.IgnoreUnexported) or explicitly compared using the
    AllowUnexported option.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n go-cmp-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

