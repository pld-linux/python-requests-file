# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		requests-file
Summary:	File transport adapter for Requests
Name:		python-%{module}
Version:	1.5.1
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/requests-file/
Source0:	https://files.pythonhosted.org/packages/source/r/requests-file/%{module}-%{version}.tar.gz
# Source0-md5:	c96daf6b0c56687556e8a52748fd896c
URL:		http://github.com/dashea/requests-file
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File transport adapter for Requests.

%package -n python3-%{module}
Summary:	File transport adapter for Requests
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
File transport adapter for Requests.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/requests_file.py[co]
%{py_sitescriptdir}/requests_file-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/requests_file.py
%{py3_sitescriptdir}/__pycache__/*.py[co]
%{py3_sitescriptdir}/requests_file-%{version}-py*.egg-info
%endif
