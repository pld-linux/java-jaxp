Summary: 	jaxp
Name:		jaxp
Version:	1.1
Release:	1
License:	Read License-* files
Group:		Development/Languages/XML/Java
Group(de):	Entwicklung/Sprachen/XML/Java
Group(pl):	Programowanie/Jêzyki/XML/Java
Source0:	jaxp-1_1.zip
URL:		http://java.sun.com/xml/download.html
Provides:	xalan-j
Provides:	crimson
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
jaxp

%package doc
Group:		Development/Languages/XML/Java
Group(de):	Entwicklung/Sprachen/XML/Java
Group(pl):	Programowanie/Jêzyki/XML/Java
Summary:	jaxp documentation

%description doc
jaxp documentation

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_javalibdir}
cp *.jar $RPM_BUILD_ROOT/%{_javalibdir}

gzip -9nf License-ASF *.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_javalibdir}
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs examples
