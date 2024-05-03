import itertools


class Solution:
    ## TC: O(n)
    ## SC: O(1)
    ## tags: string_manipulation
    def compareVersion(self, version1: str, version2: str) -> int:
        def iter_rev(version):
            while version:
                rev, _, version = version.partition(".")
                yield int(rev)

        rev_pairs = itertools.zip_longest(
            iter_rev(version1), iter_rev(version2), fillvalue=0
        )
        for rev1, rev2 in rev_pairs:
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        return 0
