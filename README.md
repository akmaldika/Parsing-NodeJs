# Parsing-NodeJs
> Tugas Besar IF 2124 Teori Bahasa Formal dan Otomata aplikasi CFG dan CNF pada Parsing NodeJS Semester 3 Tahun 2022/2023

## Table of Contents
* [General Information](#General-Information)
* [Technologies Used](#Technologies-Used)
* [Setup](#setup)
* [Example Program Test](#Example-Program-Test)
* [Contributors](#contributors)
<!-- * [Acknowledgements](#acknowledgements) -->

<!-- Adreas Bara Timur -->
## General Information
- The goal of this project is to create parsing for node js using grammar and parse algorithm.
- This project is using CFG (Context-Free Grammar) for grammar and using CYK (Cocke-Younger-Kasami) for parse algorithm.
- Students were asked to implement what they got in class by making their own code.

## Technologies Used
- Python 3

## Setup
### Prerequisite
- [Python 3](https://www.python.org/downloads//)
### Instalation
1. Clone the repo

```PowerShell
git clone https://github.com/akmaldika/Parsing-NodeJs.git
```
2. Make sure directory on terminal is in '..\Parsing-NodeJs\\' 

3. Run the program

```PowerShell
python main.py <path-of-test-file.js>
```

## Example Program Test
- Example of Accepted
```C
// File : Accepted.js
function foo(arg) {
    if (arg > 100) {
        return 'Greater'
    }
    else {
        return 'Lower'
    }
}
```

- output :

```PowerShell
File accepted
Relative length :  32
RunTime: 0.7610864639282227
```

- Example of rejected
```C
// File : recj.js
function foo(arg) {
    if (arg > 100) 
        return 'Greater'
    }
    else {
        return 'Lower'
    }
}
```

output :

```PowerShell
Syntax Error (CYK)
Relative length :  31
RunTime: 0.7130420207977295
```

## Contributors
- 13521050 [Akmal Mahardika Nurwahyu Pratama](https://github.com/akmaldika)
- 13521087 [Razzan Daksana Yoni](https://github.com/razzanYoni)
- 13521095 [Muhamad Aji Wibisono](https://github.com/MuhamadAjiW)
