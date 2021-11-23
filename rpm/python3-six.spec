Name:       python3-six
Summary:    Six is a Python 2 and 3 compatibility library
Version:    1.14.0
Release:    1
License:    MIT
URL:        https://pypi.org/project/six/
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Requires:   python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Six is a Python 2 and 3 compatibility library. It provides utility
functions for smoothing over the differences between the Python
versions with the goal of writing Python code that is compatible
on both Python versions. See the documentation for more information
on what is provided.

%prep
%setup -q -n %{name}-%{version}/six

%build
%{py3_build}

%install
rm -rf %{buildroot}
%{py3_install}

%files
%defattr(-,root,root,-)
%license LICENSE
%{python3_sitelib}/six.py
%{python3_sitelib}/six-*.egg-info
%{python3_sitelib}/__pycache__/*
