
def overlap(tup1, tup2):
    if (tup1[0] >= tup2[0] and tup1[0] <= tup2[-1]) or (tup1[-1] >= tup2[0] and tup1[-1] < tup2[-1]):
        return (min(tup1+tup2), max(tup1+tup2))
    return (tup1, tup2)

# this compares each meetings with every other since it is unordered
# this results in O(n^2)
def merge_ranges(meetings):
    new_meetings = []
    while meetings:
        new_meeting = meetings.pop()
        indices = []
        for i in range(len(meetings)):
            if (new_meeting[0] >= meetings[i][0] and new_meeting[0] <= meetings[i][-1]) or (new_meeting[-1] >= meetings[i][0] and new_meeting[-1] < meetings[i][-1]):
                new_meeting = (min(new_meeting+meetings[i]), max(new_meeting+meetings[i]))
                indices.append(i)
        for i in indices:
            meetings.pop(i)
        new_meetings.append(new_meeting)
    return new_meetings

# if we sort the original list then any meetings that can be merged are adjacent, time complexity is O(nlogn)
# additional merging takes O(n)
# so the overall time is O(nlogn)
# this doesn't rollover, only considering pairs of times but the next one can be merged with previous result
def merge_ranges(meetings):
    meetings.sort(key = lambda x: x[0])     #sort by start times
    merged_meetings = []
    # user two pointers
    i, j = 0, 1
    while j<len(meetings):
        if (meetings[i][1] >= meetings[j][0]):
            new_meeting = (meetings[i][0], max(meetings[i][1],meetings[j][1]))
            merged_meetings.append(new_meeting)
            i += 2
            j += 2
        else:
            merged_meetings.append(meetings[i])
            i += 1
            j += 1
    return merged_meetings


# correct implementation
def merge_ranges(meetings):

    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting, use the
        # later end time of the two
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start,
                                   max(last_merged_meeting_end,
                                       current_meeting_end))
        else:
            # Add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings


# Tests

import unittest
class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)