#!/bin/sh
# (cp build/where /usr/local/bin/ 2>/dev/null && INSTDIR=/usr/local/bin/ && printf "\033[32mInstalled system wide in $INSTDIR\n") || (mkdir -p ~/.local/bin/; cp build/where ~/.local/bin/ && INSTDIR=~/.local/bin && printf "\033[32mInstalled user wide in ~/.local/bin/\n") && ( printf "\033[0m"; echo ${INSTDIR}; ln -s "${INSTDIR}where" "${INSTDIR}wheres" ) || printf "\033[31mFailure\n";

file=nv-dotf.py

if cp $file /usr/local/bin/ 2>/dev/null; then
	INSTDIR=/usr/local/bin/
	printf "\033[32mInstalled system wide in $INSTDIR\n"
else
	mkdir -p ~/.local/bin/
	if cp $file ~/.local/bin/; then
		INSTDIR=~/.local/bin/
		printf "\033[32mInstalled user wide in ~/.local/bin/\n"
	fi
fi
printf "\033[0m";
# echo ${INSTDIR};
: << EOF
if [ -n "$INSTDIR" ]; then
	ln -s "${INSTDIR}where" "${INSTDIR}wheres"
else
	printf "\033[31mFailure\n";
fi
EOF
