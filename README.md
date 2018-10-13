Results for benchmarking Quantum ESPRESSO 6.3 are archived in this repo. Latest update: October 2018.

Benchmark work was carried out on two types of compute nodes (regular and large memory) on Pittsburgh's Bridges cluster.

Hardware:

|Hardware|CPU|MEM|
|:---:|:---:|--|
|Regular memory| Intel(R) Xeon(R) CPU E5-2695 v3 @ 2.30GHz|128 GB|
|Large memory| ||

Compilers:

The following compilers combinations are used in the benchmarking:

|||
|-|-|
|1| Intel Compiler v2017.4.196 + Intel MPI|
|2| Intel COmpiler v2017.4.196 + MPICH2 v2.3|
|3| GCC v4.8.5 + Intel MPI|
|4| GCC v4.8.5 + MPICH v2.3|
|5| GCC v4.8.5 + OPENMPI v2.1.2|

Makefile and make.inc file can be found under install folder.

Compiling QE for Bridges regular memory nodes
In this 


Benchmarking QE on Bridges regular memory nodes



Acknowledgment: XSEDE startup allocation.

References:
