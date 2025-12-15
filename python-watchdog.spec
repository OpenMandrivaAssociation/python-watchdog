%define module watchdog

Name:		python-watchdog
Version:	6.0.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/w/%{module}/%{module}-%{version}.tar.gz
Summary:	Filesystem events monitoring
URL:		https://pypi.org/project/watchdog/
License:	Apache-2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Filesystem events monitoring

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf src/%{module}.egg-info

%files
%doc README.rst
%license LICENSE
%{_bindir}/watchmedo
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
