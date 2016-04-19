#
# Conditional build:
%bcond_without	tests		# build without tests

%define pkgname configuration
Summary:	Pure Ruby scoped configuration files
Name:		ruby-%{pkgname}
Version:	1.3.2
Release:	1
License:	Ruby or BSD
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	f8ab1405e68849f007d2b9ea2e54449d
URL:		http://codeforpeople.com/lib/ruby/configuration/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby configuration gem provides a mechanism for configuring Ruby
programs with Ruby configuration files.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%if %{with tests}
# Only one and failing test in upstream
# https://github.com/ahoward/configuration/pull/5
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc LICENSE
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
