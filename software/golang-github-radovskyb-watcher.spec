%global goipath     github.com/radovskyb/watcher
%global tag         v1.0.7

%gometa

%global common_description %{expand:
watcher is a Go package for watching for files or directory changes without using filesystem events.}

%global golicenses    LICENSE
%global godocs        *.md

Name:       %{goname}
Version:    1.0.7
Release:    %autorelease
Summary:    watch for files or directory changes without using filesystem events
License:    BSD
URL:        %{gourl}
Source:     %{gosource}

BuildRequires: go-rpm-macros

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%check
%gocheck

%gopkgfiles

%changelog
%autochangelog
