# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/davecgh/go-spew
%global goipath         github.com/davecgh/go-spew
Version:                1.1.1

%gometa

%global common_description %{expand:
Implements a deep pretty printer for Go data structures to aid in debugging.}

%global golicenses      LICENSE
%global godocs          README.md test_coverage.txt

Name:           %{goname}
Release:        %autorelease
Summary:        Implements a deep pretty printer for Go data structures to aid in debugging

License:        ISC
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
