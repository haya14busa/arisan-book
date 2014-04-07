#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FILE: 008-interval-scheduling.py
# AUTHOR: haya14busa
# License: MIT license
#
#     Permission is hereby granted, free of charge, to any person obtaining
#     a copy of this software and associated documentation files (the
#     "Software"), to deal in the Software without restriction, including
#     without limitation the rights to use, copy, modify, merge, publish,
#     distribute, sublicense, and/or sell copies of the Software, and to
#     permit persons to whom the Software is furnished to do so, subject to
#     the following conditions:
#
#     The above copyright notice and this permission notice shall be included
#     in all copies or substantial portions of the Software.
#
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#     OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#     MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#     CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#     TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#     SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#=============================================================================

def max_n_of_jobs_can_paticipate_in(n_of_jobs, start_times, end_times):
    '''
    Input:
     n = 5
     s = {1, 2, 4, 6, 8}   // start time
     t = {3, 5, 7, 9, 10}  // end time

    Expected Output:
     3 (select 1,3,5th jobs)

    Solution:
     Choose the job which ends first
    '''
    # Describe jobs as a tuple of start and end time
    # jobs[i][0] : end time
    # jobs[i][1] : start time
    jobs = []
    for i in range(n_of_jobs):
        jobs.append((end_times[i], start_times[i]))

    # Sort by END times
    jobs.sort()

    n_of_jobs_can_paticipate_in = 0
    current_time = 0 # It's same as end time of last select jobs

    for i in range(n_of_jobs):
        if current_time < jobs[i][1]:
            n_of_jobs_can_paticipate_in += 1
            current_time = jobs[i][0]

    return n_of_jobs_can_paticipate_in


def main():
    assert max_n_of_jobs_can_paticipate_in(5, [1, 2, 4, 6, 8], [3, 5, 7, 9, 10]) == 3

    print('All done!')

if __name__ == '__main__':
    main()
