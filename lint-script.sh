#!/bin/bash 
set +x
# Run linters for salt formulas
readonly basedir="$(basename $PWD)"
readonly workdir="${basedir:4}"
check_yaml() {
       # Check yaml files for errors
       printf "|yamllint|\n"
       yamllint .
}
check_salt() {
       # Check sls files for errors
       printf "|salt-lint|\n"
       find . -name "*.sls" -exec salt-lint {} \;
}
check_python() {
       # Check python test files for errors
       printf "|pylint|\n"
       pylint -d R0801 test/
}
main() {
       # exec the linters
       check_yaml
       check_salt
       check_python
}
main "$@"
# vi:tabstop=4 shiftwidth=4 noexpandtab
