Summary: 	Java API for XML Processing
Summary(pl):	API Javy do przetwarzania XML
Name:		jaxp
Version:	1.1
Release:	1
License:	Read License-* files
Group:		Development/Languages/XML/Java
Source0:	jaxp-1_1.zip
URL:		http://java.sun.com/xml/download.html
Provides:	xalan-j
Provides:	crimson
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
JAXP - Java(TM) API for XML Processing.

%description -l pl
JAXP - API Javy do przetwarzania XML.

%package doc
Summary:	JAXP documentation
Summary(pl):	Dokumentacja do JAXP
Group:		Development/Languages/XML/Java

%description doc
JAXP documentation.

%description doc -l pl
Dokumentacja do JAXP.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install *.jar $RPM_BUILD_ROOT%{_javalibdir}

gzip -9nf License-ASF *.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs examples
