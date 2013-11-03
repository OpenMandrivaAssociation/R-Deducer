%global packname  Deducer
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.7.6.1
Release:          1
Summary:          Deducer
Group:            Sciences/Mathematics
License:          GPLv2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-6.1.tar.gz
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava R-ggplot2 R-scales R-JGR R-car R-multcomp R-effects R-foreign R-plyr R-e1071 R-MASS 

Requires:         R-lawstat R-Hmisc 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-rJava R-ggplot2 R-scales R-JGR R-car R-multcomp R-effects R-foreign R-plyr R-e1071 R-MASS

BuildRequires:   R-lawstat R-Hmisc 
%description
An intuitive, cross-platform graphical data analysis system. It uses menus
and dialogs to guide the user efficiently through the data manipulation
and analysis process, and has an excel like spreadsheet for easy data
frame visualization and editing. Deducer works best when used with the
Java based R GUI JGR, but the dialogs can be called from the command line.
Dialogs have also been integrated into the Windows Rgui.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
