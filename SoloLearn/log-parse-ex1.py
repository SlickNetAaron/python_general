import re
def show_time_of_pid(line):
  pattern = r'(^.*\d{2}:\d{2}:\d{2}).*\[(\d+)\]'
  result = re.search(pattern, line)
  return f"{result.group(1)} pid:{result.group(2)}"

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187
