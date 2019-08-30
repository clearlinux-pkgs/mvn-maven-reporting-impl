#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-reporting-impl
Version  : 2.3
Release  : 3
URL      : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-impl/2.3/maven-reporting-impl-2.3.jar
Source0  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-impl/2.3/maven-reporting-impl-2.3.jar
Source1  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-impl/2.1/maven-reporting-impl-2.1.jar
Source2  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-impl/2.1/maven-reporting-impl-2.1.pom
Source3  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-impl/2.2/maven-reporting-impl-2.2.jar
Source4  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-impl/2.2/maven-reporting-impl-2.2.pom
Source5  : https://repo1.maven.org/maven2/org/apache/maven/reporting/maven-reporting-impl/2.3/maven-reporting-impl-2.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-reporting-impl-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-reporting-impl package.
Group: Data

%description data
data components for the mvn-maven-reporting-impl package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.3
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.3/maven-reporting-impl-2.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.1/maven-reporting-impl-2.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.1/maven-reporting-impl-2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.2/maven-reporting-impl-2.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.2/maven-reporting-impl-2.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.3
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.3/maven-reporting-impl-2.3.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.1/maven-reporting-impl-2.1.jar
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.1/maven-reporting-impl-2.1.pom
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.2/maven-reporting-impl-2.2.jar
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.2/maven-reporting-impl-2.2.pom
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.3/maven-reporting-impl-2.3.jar
/usr/share/java/.m2/repository/org/apache/maven/reporting/maven-reporting-impl/2.3/maven-reporting-impl-2.3.pom
