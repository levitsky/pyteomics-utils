# pyteomics-utils
Simple but handy CLI tools for everyday data analysis tasks.

The commands operate on stdin and write to stdout whenever possible.

## Supported commands (run each command with `-h` for help)

`pyteomics fasta decoy` -- generate a decoy database for one or more files.

`pyteomics fasta describe` -- check contents of a FASTA file.

`pyteomics fasta combine` -- combine multiple FASTA files, optionally adding decoys in the process.

`pyteomics pepxml info` -- list number of PSMs (with and without FDR filtering) in pepXML files.
