Summary:	Java API for XML Processing
Summary(pl):	API Javy do przetwarzania XML-a
Name:		jaxp
Version:	1.1
Release:	1
License:	restricted, non-distributable (see License* files)
# base JAXP is on Sun's restricted license (internal use only),
# DOM bindings are on W3C license (distributable)
# and the rest is on Apache license (distributable)
Group:		Development/Languages/XML/Java
Source0:	%{name}-1_1.zip
URL:		http://java.sun.com/xml/download.html
NoSource:	0
Requires:	jre >= 1.1.8
Provides:	crimson
Provides:	xalan-j
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
JAXP - Java(TM) API for XML Processing.

%description -l pl
JAXP - API Javy do przetwarzania XML-a.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc License-ASF *.html
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs examples
