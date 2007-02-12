# NOTE: this spec is obsolete: jre 1.4 contains jaxp 1.2.6, jre 1.5 contains 1.3
Summary:	Java API for XML Processing
Summary(pl.UTF-8):   API Javy do przetwarzania XML-a
Name:		jaxp
Version:	1.2.0
Release:	1
License:	SCSL
# base JAXP is on Sun's restricted license (internal use only),
# DOM bindings are on W3C license (distributable)
# and the rest is on Apache license (distributable)
Group:		Development/Languages/XML/Java
# download from http://www.sun.com/software/communitysource/jaxp/download.html
# (after registering etc.; note that sources distribution is restricted, see
#  also http://www.sun.com/software/communitysource/countries.html )
Source0:	%{name}-1_2_0-scsl.zip
# NoSource0-md5:	6424d0dc065b63506c9873e78a18869e
URL:		http://java.sun.com/xml/download.html
NoSource:	0
BuildRequires:	unzip
Requires:	jre >= 1.1.8
Provides:	crimson
Provides:	xalan-j
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
JAXP - Java(TM) API for XML Processing.

%description -l pl.UTF-8
JAXP - API Javy do przetwarzania XML-a.

%package doc
Summary:	JAXP documentation
Summary(pl.UTF-8):   Dokumentacja do JAXP
Group:		Development/Languages/XML/Java

%description doc
JAXP documentation.

%description doc -l pl.UTF-8
Dokumentacja do JAXP.

%prep
%setup -c

%build
ant jars

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
install dist/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/License-ASF docs/*.html
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs samples
