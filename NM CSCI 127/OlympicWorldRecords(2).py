#Saiss Cruz
#saiss.cruz10@myhunter.cuny.edu
#11/4/2021

def worldRecord(gender, eventDistance):                                                                         
  """
  Takes as two parameters: the gender and the eventDistance.
  Returns the AMNH worldRecord, as follows:
  If the eventDistance is is "100" and the gender is "men", record is 9.63 seconds.
  If the eventDistance is is "200" and the gender is  "men", record is 19.30 seconds.
  If the eventDistance is is "400" and the gender is  "men", record is 43.03 seconds.
  If the eventDistance is is "100" and the gender is "women", record is 10.62 seconds.
  If the eventDistance is is "200" and the gender is  "women", record is 21.34 seconds.
  If the eventDistance is is "400" and the gender is  "women", record is 48.25 seconds.
  """

  men = {"100":9.63, "200":19.30, "400":43.03}
  women = {"100":10.62, "200":21.34, "400":48.25}

  if gender == "men":
    return men[eventDistance]
  elif gender == "women":
    return women[eventDistance]
  else:
    print("Error Encountered")

def main():
  a = input('Enter the gender (men, women): ')
  t = input('Enter the eventDistance (100,200,400): ')
  print(f'The world record is {worldRecord(a,t)}')

#Allow script to be run directly:
if __name__ == "__main__":
  main()