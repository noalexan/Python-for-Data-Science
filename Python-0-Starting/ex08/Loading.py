import os
import sys
import time


def ft_tqdm(lst: range) -> None:
    start = last = time.time()

    for i in lst:
        terminal_size = os.get_terminal_size()
        width = terminal_size.columns

        ratio = (i + 1) / lst.stop
        average = round(ratio * 100)
        percentage = str(average).rjust(3) + "%"

        total_seconds_since_start = last - start
        minutes_since_start = round(total_seconds_since_start // 60)
        seconds_since_start = round(total_seconds_since_start % 60)

        resume = "{}/{} [{}:{}]".format(
            i + 1,
            lst.stop,
            str(minutes_since_start).zfill(2),
            str(seconds_since_start).zfill(2),
        )

        bar_len = width - len(percentage) - len(resume) - 3

        last = time.time()

        sys.stderr.write(
            "\r{}|{}| {}".format(
                percentage,
                ("\u2588" * int(ratio * bar_len)).ljust(bar_len),
                resume
            )
        )

        yield i

    sys.stderr.write("\n")
