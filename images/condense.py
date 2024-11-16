import re


max_delay = 2

with open("images/pipeline.cast") as f:
    with open("images/condensed.cast", "w") as fo:

        total = 0
        last_timestamp = 0

        for line in f.readlines():
            if line.startswith("["):

                match = re.search(r"\d+\.\d+", line)
                timestamp = float(match.group())
                timestamp = timestamp - total

                if timestamp - last_timestamp > max_delay:
                    correction = timestamp - (last_timestamp + max_delay)
                    total = total + correction
                    timestamp = last_timestamp + max_delay

                last_timestamp = timestamp

                new_line = re.sub(r"\d+\.\d+", f"{timestamp:.3f}", line, count=1)
                fo.write(new_line)
            else:
                fo.write(line)
