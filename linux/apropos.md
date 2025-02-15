# apropos

Search the manual page names and descriptions, whatis database.

## Syntax

apropos keyword

apropos [-dalv?V] --exact [-s list] [-m system[,...]] [-M path] [-L locale] [-C file] keyword ...

apropos [-dalv?V] --regex [-s list] [-m system[,...]] [-M path] [-L locale] [-C file] regex ...

apropos [-dalv?V] --wildcard [-s list] [-m system[,...]] [-M path] [-L locale] [-C file] keyword ...

Options (not all distributions support these options, run apropos -?)

   -a, --and
            Only display items that match all the supplied keywords.
            The default is to display items that match any keyword.

   -C file, --config-file=file
            Use this user configuration file rather than the default of ~/.manpath.

   -d, --debug
            Print debugging information.

   -e, --exact
            Each keyword will be exactly matched against the page names and the descriptions.

   -r, --regex
            Interpret each keyword as a regular expression.  This is the default
            behaviour.  Each keyword will be matched against the page names and
            the descriptions independently.
            It can match any part of either. The match is not limited to word boundaries.

   -w, --wildcard
            Interpret each keyword as a pattern containing shell style wildcards.
            Each keyword will be matched against the page names and the descriptions
            independently.  If --exact is also used, a match will only be found if an
            expanded keyword matches an entire description or page name.
            Otherwise the keyword is also allowed to match on word boundaries in the description.

   -l, --long
            Do not trim output to the terminal width.  Normally, output will be
            truncated to the terminal width to avoid ugly results from poorly-written NAME sections.


   -m system[,...], --systems=system[,...]
            If this system has access to other Operating System’s manual page
            descriptions, they can be searched using this option.
            To search NewOS’s manual page descriptions, use the option -m NewOS.

            The system specified can be a combination of comma-delimited Operating System names.
            To include a search of the native Operating System’s whatis descriptions, include
            the system name man in the argument string.
            This option will override the $SYSTEM environment variable.

   -M path, --manpath=path
            Specify an alternate set of colon-delimited manual page hierarchies to search.
            By default, apropos uses the $MANPATH environment variable, unless it is empty or
            unset, in which case it will determine an appropriate manpath based on your
            $PATH environment variable.  This option overrides the contents of $MANPATH.

   -L locale, --locale=locale
            apropos will normally determine your current locale by a call to the C function
            setlocale(3) which interrogates various environment variables, possibly including
            $LC_MESSAGES and $LANG.  To temporarily override the determined value, use this
            option to supply a locale string directly to apropos.  Note that it will not take
            effect until the search for pages actually begins. Output such as the help message
            will always be displayed in the initially determined locale.

   -s list, --sections=list, --section=list
            Search only the given manual sections.
            list is a colon- or comma-separated list of sections.
            If an entry in list is a simple section, for example "3",
            then the displayed list of descriptions will include pages in sections "3",
            "3perl", "3x", and so on; while if an entry in list has an extension,
            for example "3perl", then the list will only include pages in that exact part
            of the manual section.

   -?, --help
            Print a help message and exit.

       --usage
            Print a short usage message and exit.

   -V, --version
            Display version information.

   -v, --verbose
            Print verbose warning messages.

Each manual page has a short description available within it. apropos searches the descriptions for instances of keyword.

keyword is usually a regular expression, as if (-r) was used, or may contain wildcards (-w), or match the exact keyword (-e). Using these options, it may be necessary to quote the keyword or escape (\) the special characters to stop the shell from interpreting them.

The standard matching rules allow matches to be made against the page name and word boundaries in the description.

The database searched by apropos is updated by the mandb program. Depending on your installation, this may be run by a periodic cron job, or may need to be run manually after new manual pages have been installed.

## Example commands

1. Search for a keyword in manual page descriptions

```sh
apropos network
```

Finds manual pages related to “network”.

2. Search for multiple keywords (matches any by default)

```sh
apropos network security
```

Finds manual pages related to “network” or “security”.

### Using Options

1. Search for pages that match all keywords

```sh
apropos -a network security
```

Finds manual pages that contain both “network” and “security”.

2. Search for an exact match

```sh
apropos --exact ls
```

Finds manual pages where “ls” appears exactly as a command or in descriptions.

3. Use a regular expression to match pages

```sh
apropos --regex '^net'
```

Finds manual pages whose names or descriptions start with “net”.

4. Use wildcard matching

```sh
apropos --wildcard 'net*'
```

Finds manual pages with words that start with “net” (e.g., “network”, “netstat”).

### Filtering by Section

1. Search only within a specific manual section (e.g., section 2)

```sh
apropos -s 2 open
```

Finds system calls (section 2) related to “open”.

2. Search multiple manual sections (e.g., 2 and 3)

```sh
apropos -s 2,3 open
```

Finds results in both sections 2 and 3.

### Other Useful Options

1. Show results without truncation

```sh
apropos --long network
```

Prevents output from being cut off at terminal width.

2. Debugging mode (useful for troubleshooting)

```sh
apropos --debug network
```

Shows debugging information about the search.

3. Use a custom man path

```sh
apropos -M /usr/local/man network
```

Searches manual pages from /usr/local/man instead of the default path.

4. Check the apropos version

```sh
apropos --version
```
