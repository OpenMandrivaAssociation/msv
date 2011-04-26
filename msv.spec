# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define gcj_support 1

%define bootstrap %{?_with_bootstrap:1}%{!?_with_bootstrap:%{?_without_bootstrap:0}%{!?_without_bootstrap:%{?_bootstrap:%{_bootstrap}}%{!?_bootstrap:0}}}

%define cvsdate 20050722

Summary:        Multischema Validator
Name:           msv
Version:        1.2
Release:        %mkrel 0.1.%{cvsdate}.3.1.11
Epoch:          1
License:        BSD-Style
URL:            http://msv.dev.java.net
Group:          Development/Java
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r msv-20050722 msv ; mv msv msv-20050722 tar zcf msv-20050722.tar.gz msv-*
Source0:        %{name}-%{cvsdate}.tar.gz
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs co -r msv-20060821 msv/xsdlib/src/com/sun/msv/datatype/xsd/DateType.java
# This is needed for the package to build
Source1:        %{name}-20060821-Datatype.java
Patch0:          %{name}-build_xmls.patch
# There is a build time dependency on crimson which needs to be stripped
Patch1:         %{name}-disable-crimson.patch
# Class-Path
Patch2:         %{name}-noclasspathsinmanifests.patch
BuildRequires:  ant >= 0:1.6, java-rpmbuild >= 0:1.6
BuildRequires:  javacc
BuildRequires:  junit
%if ! %{bootstrap}
BuildRequires:  jdom
BuildRequires:  saxon
%endif

BuildRequires:  isorelax
BuildRequires:  relaxngDatatype
BuildRequires:  servlet
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildRequires:  xml-commons-resolver12
BuildRequires:  ant-trax
BuildRequires:  java-javadoc
BuildRequires:  xerces-j2-javadoc-impl
BuildRequires:  xerces-j2-javadoc-xni
BuildRequires:  xerces-j2-javadoc-apis
BuildRequires:  isorelax-javadoc
BuildRequires:  relaxngDatatype-javadoc
Requires:         jpackage-utils >= 0:1.6
Requires(postun): jpackage-utils >= 0:1.6

%if ! %{gcj_support}
BuildRequires:  java-devel
BuildArch:      noarch
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%if %{gcj_support}
BuildRequires:    java-gcj-compat-devel
%endif

%description
The Sun Multi-Schema XML Validator (MSV) is a Java 
technology tool to validate XML documents against 
several kinds of XML schemata. It supports RELAX NG, 
RELAX Namespace, RELAX Core, TREX, XML DTDs, and a 
subset of XML Schema Part 1. This latest (version 1.2) 
release includes several bug fixes and adds better 
conformance to RELAX NG/W3C XML standards and JAXP 
masquerading. 

%package        msv
Summary:        MSV proper
Group:          Development/Java
Requires:       isorelax
Requires:       relaxngDatatype
Requires:       servlet
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis
Requires:       xml-commons-resolver12
Requires:       msv-xsdlib
Requires:         jpackage-utils >= 0:1.6
Provides:       msv-strict <= %{version}-%{release}
Obsoletes:      msv-strict <= %{version}-%{release}

%description    msv
%{summary}.

%package        msv-javadoc
Summary:        Javadoc for MSV proper
Group:          Development/Java
Requires:         jpackage-utils >= 0:1.6
Provides:       msv-strict-javadoc <= %{version}-%{release}
Obsoletes:      msv-strict-javadoc <= %{version}-%{release}

%description    msv-javadoc
%{summary}.

%package        demo
Summary:        Samples for %{name}
Group:          Development/Java
Requires:       msv-msv
Requires:       msv-xsdlib
Requires:         jpackage-utils >= 0:1.6

%description    demo
%{summary}.

%package        relames
Summary:        Relames 
Group:          Development/Java
Requires:       isorelax
Requires:       relaxngDatatype
Requires:       xalan-j2
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis
Requires:       xml-commons-resolver12
Requires:       msv-msv
Requires:       msv-xsdlib
Requires:         jpackage-utils >= 0:1.6

%description    relames
%{summary}.

%package        relames-javadoc
Summary:        Javadoc for relames
Group:          Development/Java
Requires:         jpackage-utils >= 0:1.6

%description    relames-javadoc
%{summary}.

%package        rngconv
Summary:        Rngconv
Group:          Development/Java
Requires:       isorelax
Requires:       relaxngDatatype
Requires:       xerces-j2
Requires:       xml-commons-jaxp-1.3-apis
Requires:       msv-msv
Requires:       msv-xsdlib
Requires:         jpackage-utils >= 0:1.6

%description    rngconv
%{summary}.

%package        xmlgen
Summary:        XmlGen
Group:          Development/Java
Requires:       isorelax
Requires:       relaxngDatatype
Requires:       xml-commons-jaxp-1.3-apis
Requires:       xerces-j2
Requires:       msv-msv
Requires:       msv-xsdlib
Requires:         jpackage-utils >= 0:1.6

%description    xmlgen
%{summary}.

%package        xmlgen-javadoc
Summary:        Javadoc for xmlgen
Group:          Development/Java
Requires:         jpackage-utils >= 0:1.6

%description    xmlgen-javadoc
%{summary}.

%package        xsdlib
Summary:        Xsdlib
Group:          Development/Java
Requires:       relaxngDatatype
Provides:       xsdlib <= %{version}-%{release}
Obsoletes:      xsdlib <= %{version}-%{release}
Requires:         jpackage-utils >= 0:1.6

%description    xsdlib
%{summary}.

%package        xsdlib-javadoc
Summary:        Javadoc for xsdlib
Group:          Development/Java
Provides:       xsdlib-javadoc <= %{version}-%{release}
Obsoletes:      xsdlib-javadoc <= %{version}-%{release}
Requires:         jpackage-utils >= 0:1.6

%description    xsdlib-javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Java
Requires:         jpackage-utils >= 0:1.6

%description    manual
%{summary}.

%prep
%setup -q -n %{name}-%{cvsdate}
cp %{SOURCE1} xsdlib/src/com/sun/msv/datatype/xsd/DateType.java
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
# delete Class-Path: from manifests
for m in $(find . -name MANIFEST.MF); do
sed -e '/^Class-path:/d' $m > tempf
cp tempf $m
done
rm tempf

%patch0 -p0 -b .sav
%patch1 -p0 -b .sav2
%patch2 -p0

%{__perl} -pi -e 's/1\.[23]/1.4/g' `find . -type f -name build.xml`

%build
pushd shared/lib
ln -sf $(build-classpath ant) ant.jar
#ln -sf $(build-classpath crimson) crimson.jar
#ln -sf $(build-classpath dom4j) dom4j.jar
ln -sf $(build-classpath isorelax) isorelax.jar
ln -sf $(build-classpath junit) junit.jar
ln -sf $(build-classpath relaxngDatatype) relaxngDatatype.jar
ln -sf $(build-classpath xml-commons-resolver12) resolver.jar
%if ! %{bootstrap}
ln -sf $(build-classpath jdom) jdom.jar
ln -sf $(build-classpath saxon) saxon.jar
%endif
ln -sf $(build-classpath servlet) servlet.jar
ln -sf $(build-classpath xalan-j2) xalan.jar
ln -sf $(build-classpath xerces-j2) xercesImpl.jar
ln -sf $(build-classpath xml-commons-jaxp-1.3-apis) xmlParserAPIs.jar
popd

%{ant} -Dant.build.javac.source=1.4 release

%install
rm -rf $RPM_BUILD_ROOT

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 package/msv.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-msv-%{version}.jar
install -m 644 package/relames.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-relames-%{version}.jar
install -m 644 package/rngconv.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-rngconv-%{version}.jar
install -m 644 package/xmlgen.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-xmlgen-%{version}.jar
install -m 644 package/xsdlib.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-xsdlib-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} 
ln -sf msv-msv.jar msv-strict.jar
ln -sf msv-xsdlib.jar xsdlib.jar
)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}/msv
cp -pr msv/dist/javadoc/* \
                $RPM_BUILD_ROOT%{_javadocdir}/%{name}/msv
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}/relames
cp -pr relames/dist/javadoc/* \
                $RPM_BUILD_ROOT%{_javadocdir}/%{name}/relames
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}/xmlgen
cp -pr generator/dist/javadoc/* \
                $RPM_BUILD_ROOT%{_javadocdir}/%{name}/xmlgen
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}/xsdlib
cp -pr xsdlib/dist/javadoc/* \
                $RPM_BUILD_ROOT%{_javadocdir}/%{name}/xsdlib

# docs
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}/msv
install -m 644 msv/doc/* \
                  $RPM_BUILD_ROOT%{_docdir}/%{name}/msv
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/msv/Apache-LICENSE-1.1.txt
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}/relames
install -m 644 relames/doc/* \
                  $RPM_BUILD_ROOT%{_docdir}/%{name}/relames
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/relames/Apache-LICENSE-1.1.txt
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}/rngconv
install -m 644 rngconverter/doc/* \
                  $RPM_BUILD_ROOT%{_docdir}/%{name}/rngconv
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/rngconv/Apache-LICENSE-1.1.txt
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}/xmlgen
install -m 644 generator/doc/* \
                  $RPM_BUILD_ROOT%{_docdir}/%{name}/xmlgen
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/xmlgen/Apache-LICENSE-1.1.txt
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}/xsdlib
install -m 644 xsdlib/doc/* \
                  $RPM_BUILD_ROOT%{_docdir}/%{name}/xsdlib
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/xsdlib/Apache-LICENSE-1.1.txt

#examples
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/msv
cp -pr msv/dist/examples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/msv
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/xsdlib
cp -pr xsdlib/dist/examples/* $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}/xsdlib

%if %{gcj_support}
#export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm --exclude usr/share/%{name}-%{version}/%{name}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{gcj_support}
%post
%{update_gcjdb}

%postun
%{clean_gcjdb}
%endif

%files msv
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-msv-%{version}.jar
%{_javadir}/%{name}-msv.jar
%{_javadir}/msv-strict.jar
%doc %{_docdir}/%{name}/msv/license.txt
%doc %{_docdir}/%{name}/msv/copyright.txt
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-msv*
%endif

%files msv-javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}/msv

%files demo
%defattr(0644,root,root,0755)
%{_datadir}/%{name}-%{version}/msv
%{_datadir}/%{name}-%{version}/xsdlib

%files relames
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-relames-%{version}.jar
%{_javadir}/%{name}-relames.jar
#%{_docdir}/%{name}/relames/license.txt
%doc %{_docdir}/%{name}/relames/copyright.txt
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-relames*
%endif

%files relames-javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}/relames

%files rngconv
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-rngconv-%{version}.jar
%{_javadir}/%{name}-rngconv.jar
%doc %{_docdir}/%{name}/rngconv/license.txt
%doc %{_docdir}/%{name}/rngconv/copyright.txt
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-rngconv*
%endif

%files xmlgen
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-xmlgen-%{version}.jar
%{_javadir}/%{name}-xmlgen.jar
%doc %{_docdir}/%{name}/xmlgen/license.txt
%doc %{_docdir}/%{name}/xmlgen/copyright.txt
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-xmlgen*
%endif

%files xmlgen-javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}/xmlgen

%files xsdlib
%defattr(0644,root,root,0755)
%{_javadir}/%{name}-xsdlib-%{version}.jar
%{_javadir}/%{name}-xsdlib.jar
%{_javadir}/xsdlib.jar
%doc %{_docdir}/%{name}/xsdlib/license.txt
%doc %{_docdir}/%{name}/xsdlib/copyright.txt
%if %{gcj_support}
%attr(-,root,root) %{_libdir}/gcj/%{name}/%{name}-xsdlib*
%endif

%files xsdlib-javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}/xsdlib

%files manual
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}/msv/ChangeLog.txt
%doc %{_docdir}/%{name}/msv/*.html
%doc %{_docdir}/%{name}/msv/*.gif
%doc %{_docdir}/%{name}/msv/README.txt
%doc %{_docdir}/%{name}/relames/README.txt
%doc %{_docdir}/%{name}/rngconv/README.txt
%doc %{_docdir}/%{name}/xmlgen/*.html
%doc %{_docdir}/%{name}/xmlgen/README.txt
%doc %{_docdir}/%{name}/xsdlib/*.html
%doc %{_docdir}/%{name}/xsdlib/README.txt
