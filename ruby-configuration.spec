%define pkgname configuration
Summary:	Ruby configuration for your ruby programs
Name:		ruby-%{pkgname}
Version:	1.3.4
Release:	1
License:	Ruby-alike
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	c4db42cbb3b60ca7a2c921b941ae0ce9
URL:		https://github.com/ahoward/configuration
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby configuration for your ruby programs.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/configuration.rb
%{ruby_vendorlibdir}/configuration
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
