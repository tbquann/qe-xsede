Results for benchmarking Quantum ESPRESSO 6.3 on Bridges are archived in this repo. Last updated: October 14 2018.

Hardware:

<center>

|System|CPU|MEM|
|:---:|:---:|:--:|
|Regular memory| Intel(R) Xeon(R) CPU E5-2695 v3 @ 2.30GHz|128 GB|
|Large memory| Intel(R) Xeon(R) CPU E7-8860/8870 v3/4 @ 2.1-3.2 GHz|3TB|

</center>

For detailed description of system configurations, see [XSEDE's official website](https://www.psc.edu/bridges/user-guide/system-configuration) 

Compilers:

<center>

|Cases| Compilers|
|:-:|:-|
|1| Intel Compiler v2017.4.196 + Intel MPI|
|2| Intel Compiler v2017.4.196 + MPICH2 v2.3|
|3| GCC v4.8.5 + Intel MPI|
|4| GCC v4.8.5 + MPICH v2.3|
|5| GCC v4.8.5 + OPENMPI v2.1.2|

</center>


Makefile and make.inc file can be found under install folder.





Acknowledgment: XSEDE startup allocation.

