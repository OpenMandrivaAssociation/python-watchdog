Name:		python-watchdog
Version:	6.0.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/w/watchdog/watchdog-%{version}.tar.gz
Summary:	Filesystem events monitoring
URL:		https://pypi.org/project/watchdog/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Filesystem events monitoring

%files
%{_bindir}/watchmedo
%{py_sitedir}/watchdog
%{py_sitedir}/watchdog-*.*-info
