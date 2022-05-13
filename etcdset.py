#!/bin/bash

usage() {
cat <<EOF 
Usage:
    -s: Standard ETCD Set
    -c: Custom ETCD Set

note: Machines must be created first
EOF

exit 1
}

custom() {
	read -p "Enter name of machine: " machine
	read -p "Enter key: " key
	read -p "Enter Value: " value

	salt "$(hostname)" etcd.set /store/$machine/$key $value
	
	exit 0
}

standard() {
	read -p "Enter number of machines you are setting: " num
	read -p "Enter contact email: " email 
	read -p "Enter senv: " senv
	read -p "Enter role: " role

	for i in $(seq 1 $num); do
		read -p "Enter name of machine: " machine
		salt "$(hostname)" etcd.set /store/$machine/contact $email	
		salt "$(hostname)" etcd.set /store/$machine/senv $senv
		salt "$(hostname)" etcd.set /store/$machine/role $role
	done
	
	exit 0
}

main() {
	# Parse CLI Args	
	while getopts ":sc" o; do
		case "${o}" in 
			s)	standard;;
			c) 	custom;;
			*)  	usage;;
		esac
	done

	usage	
}

main "$@"
