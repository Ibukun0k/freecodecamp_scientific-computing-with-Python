def add_time(start, duration, day=False):
  s = start

  duration = duration.split(":")
  n = (int((duration)[0]) * 60) + (int((duration)[1]))

  h, m = map(int, s[:-2].split(':'))
  h %= 12
  if s[-2:] == 'PM':
    h += 12
  t = h * 60 + m + n
  h, m = divmod(t, 60)
  x = h//24
  h %= 24
  suffix = ' A' if h < 12 else ' P'
  h %= 12
  if h == 0:
    h = 12

  if day:
    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days_of_the_week = [i.lower() for i in (days_of_the_week)]
    y = [y.lower() for y in day]
    today = ""
     
    for y in y:
      today += y

    newindex = (days_of_the_week).index(today) + int(x)
        
    while newindex >= 7:
      newindex = newindex - 7

    day = days_of_the_week[int(newindex)]

    theday = ""

    for i in day:
      theday += day

      day = theday.title()
    
      if x > 1:
        return("{:01d}:{:02d}{}M, {} ({} days later)").format(h, m, suffix, day, x)

      elif x == 1:
        return("{:01d}:{:02d}{}M, {} (next day)").format(h, m, suffix, day)

      elif x < 1:
        day = days_of_the_week[(days_of_the_week).index(today)]

        theday = ""

        for i in day:
          theday += day

          day = theday.title()

          return("{:01d}:{:02d}{}M, {}" ).format(h, m, suffix, day)

  else:
    if x > 1:
      return("{:01d}:{:02d}{}M ({} days later)").format(h, m, suffix, x)

    elif x == 1:
      return("{:01d}:{:02d}{}M (next day)").format(h, m, suffix)

    elif x < 1:
      return("{:01d}:{:02d}{}M" ).format(h, m, suffix)
