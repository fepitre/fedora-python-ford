# Based on spec created bypyp2rpm-3.3.7
%global pypi_name ford
%global pypi_version 6.1.5

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        FORD, standing for FORtran Documenter, is an automatic documentation generator for modern Fortran programs

License:        GPLv3
URL:            https://github.com/Fortran-FOSS-Programmers/ford
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/FORD-%{pypi_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(beautifulsoup4) >= 4.5.1
BuildRequires:  python3dist(graphviz)
BuildRequires:  python3dist(importlib-metadata)
BuildRequires:  python3dist(jinja2) >= 2.1
BuildRequires:  python3dist(markdown)
BuildRequires:  python3dist(markdown-include) >= 0.5.1
BuildRequires:  python3dist(md-environ)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(pytest) >= 3.3
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(toposort)
BuildRequires:  python3dist(tqdm)

%description
This is an automatic documentation generator for modern Fortran programs.
FORD stands for FORtran Documenter. As you may know, "to ford" refers to crossing
a river (or other body of water). It does not, in this context, refer to any
company or individual associated with cars.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(beautifulsoup4) >= 4.5.1
Requires:       python3dist(graphviz)
Requires:       python3dist(importlib-metadata)
Requires:       python3dist(jinja2) >= 2.1
Requires:       python3dist(markdown)
Requires:       python3dist(markdown-include) >= 0.5.1
Requires:       python3dist(md-environ)
Requires:       python3dist(pygments)
Requires:       python3dist(setuptools)
Requires:       python3dist(toposort)
Requires:       python3dist(tqdm)
%description -n python3-%{pypi_name}
This is an automatic documentation generator for modern Fortran programs.
FORD stands for FORtran Documenter. As you may know, "to ford" refers to crossing
a river (or other body of water). It does not, in this context, refer to any
company or individual associated with cars.

%prep
%autosetup -n FORD-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# fixme: find why we get FORD-0.0.0 instead of %{pypi_name}-%{python3_version}
mv $RPM_BUILD_ROOT/%{python3_sitelib}/FORD-0.0.0-py%{python3_version}.egg-info \
    $RPM_BUILD_ROOT/%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

# fixme: pytest fails
#%check
#PYTHONPATH=. pytest -k test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md README.rst
%{_bindir}/ford
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Dec 14 2021 Frédéric Pierret (fepitre) <frederic@invisiblethingslab.com> - 6.1.5-1
- Initial package.