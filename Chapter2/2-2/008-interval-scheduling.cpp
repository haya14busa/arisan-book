#include <cstdio>
#include <iostream>
#include <assert.h>
#include <algorithm>

const int MAX_N = 10000;

int max_n_of_jobs_can_be_paticipating(int n_of_jobs, int start_t[], int end_t[]) {
    /*
     * Input:
     *  n = 5
     *  s = {1, 2, 4, 6, 8}   // start time
     *  t = {3, 5, 7, 9, 10}  // end time
     *
     * Expected Output:
     *  3 (select 1,3,5th jobs)
     *
     * Solution:
     *  Choose the job which ends first
     *
     */
    // Describe jobs as a pair of start and end time
    std::pair<int, int> jobs[MAX_N];

    for (int i = 0; i < n_of_jobs; i++) {
        // We want to sort by *END* time later, so insert END time to first
        jobs[i].first = end_t[i];
        jobs[i].second = start_t[i];
    }
    std::sort(jobs, jobs + n_of_jobs);

    int n_of_jobs_paticipated_in = 0;
    int current_time = 0; // Equals to last choosed jobs of END time
    for (int i = 0; i < n_of_jobs; i++) {
        if (current_time < jobs[i].second) {
            n_of_jobs_paticipated_in++;
            current_time = jobs[i].first;
        }
    }

    return n_of_jobs_paticipated_in;
}

int main() {
    int n1 = 5;
    int s1[] = {1, 2, 4, 6, 8};
    int t1[] = {3, 5, 7, 9, 10};
    assert(max_n_of_jobs_can_be_paticipating(n1, s1, t1) == 3);

    puts("All done!");
}
