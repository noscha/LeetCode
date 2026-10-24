class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        """
        Convert dates to absolute day, and calculate intersection
        """

        def date_to_total_day(date: str) -> int:

            MONTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            month, day = date.split("-")

            total_day = sum(
                [MONTHS[i] for i in range(len(MONTHS)) if i < int(month) - 1]
            ) + int(day)

            return total_day

        intersection_start = max(
            date_to_total_day(arriveAlice), date_to_total_day(arriveBob)
        )

        intersection_end = min(
            date_to_total_day(leaveAlice), date_to_total_day(leaveBob)
        )

        return max(intersection_end - intersection_start + 1, 0)
