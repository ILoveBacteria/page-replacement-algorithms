# Page Replacement Algorithms

[![License: MIT](https://img.shields.io/github/license/ILoveBacteria/page_replacement_algorithms)](https://github.com/ILoveBacteria/page_replacement_algorithms/blob/master/LICENSE)
[![Issues](https://img.shields.io/github/issues/ILoveBacteria/page_replacement_algorithms)](https://github.com/ILoveBacteria/page_replacement_algorithms/issues)
[![Forks](https://img.shields.io/github/forks/ILoveBacteria/page_replacement_algorithms)](https://github.com/ILoveBacteria/page_replacement_algorithms/network/members)
[![Stars](https://img.shields.io/github/stars/ILoveBacteria/page_replacement_algorithms)]()
[![Watchers](https://img.shields.io/github/watchers/ILoveBacteria/page_replacement_algorithms)]()
[![Last commit](https://img.shields.io/github/last-commit/ILoveBacteria/page_replacement_algorithms)](https://github.com/ILoveBacteria/page_replacement_algorithms/commits/master)
[![Workflow](https://img.shields.io/github/actions/workflow/status/ILoveBacteria/page_replacement_algorithms/test.yml?label=test)](https://img.shields.io/github/actions/workflow/status/ILoveBacteria/page_replacement_algorithms/test.yml?label=test)
[![Workflow](https://img.shields.io/github/pipenv/locked/python-version/ILoveBacteria/page_replacement_algorithms)](https://img.shields.io/github/pipenv/locked/python-version/ILoveBacteria/page_replacement_algorithms)

## Description

This is my OS course project.

This repository contains an implementation of three popular page replacement algorithms: **First-In-First-Out (FIFO)**, 
**Least Recently Used (LRU)**, and **Second Chance**. These algorithms are commonly used in operating systems to manage 
memory allocation and ensure that the most frequently accessed pages are kept in memory, while less frequently 
used pages are swapped out to disk.

The code is written in a modular and extensible way, allowing for easy integration into existing systems or for 
use as a standalone library. Each algorithm is implemented as a separate class, with a consistent interface that 
allows for easy swapping between them.

The FIFO algorithm simply replaces the oldest page in memory when a new page needs to be loaded. LRU keeps track 
of the least recently used pages and replaces the one that has not been accessed for the longest time. Second Chance 
is similar to FIFO, but gives each page a "second chance" before being replaced if it has been accessed recently.