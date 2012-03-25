Changelog
=========

0.1.13
------

- added this changelog
- git get-version fetches only when local lookup fails
- hg get-version pulls if label not found
- Popen error message incudes cwd path

0.1.12
------

- py_checker clean after all refactorings since 0.1.0

0.1.11
------

- svn and hg update without user interaction
- bugfix #30
- minor bugfixes

0.1.10
------

- minor bugs

0.1.9
-----

- safer sanitization of shell params
- git diff and stat recurse for submodules
- base class manages all calls to Popen

0.1.8
-----

- several bugfixes
- reverted using shell commands instead of bazaar API


0.1.7
-----

- reverted using shell commands instaed of pysvn and mercurial APIs
- protection against shell incection attempts

0.1.6
-----

- bugfixes to svn and bzr
- unified all calls through Popen

0.1.5
-----

- missing dependency to dateutil added

0.1.4
-----

switched shell calls to calls to python API of mercurial, bazaar, py-svn

0.1.3
-----

- fix #6

0.1.2
-----

- fix #15

0.1.1
-----

- more unit tests
- diverse bugfixes
- major change to git client behavior, based around git https://kforge.ros.org/vcstools/trac/ticket/1

0.1.0
-----

- documentation fixes

0.0.3
-----

- import from svn