Name:		python-megatools
Version:	0.0.4
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/m/megatools/megatools-%{version}.tar.gz
Summary:	Simple python Megatools wrapper
URL:		https://pypi.org/project/megatools/
License:	GPL
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch
Requires:	megatools

%description
Megatools's wrapper

%files
%{py_sitedir}/megatools
%{py_sitedir}/megatools-*.*-info
