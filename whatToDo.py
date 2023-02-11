def main(): 
  print('We will determine the appropriate outcome to the given situation based on your rating. This will allow you to control your negative and positive experiences.')

  name = input('What is your name? ')

  print('Hello, ', name, '! Below is how you will rate your interaction. ')

  print('1: Highly disturbed...')
  print('2: Slightly bothered.')
  print('3: Neither pleasant or upsetting.')
  print('4: Enjoyable!')
  print('5: Exceptional!!')

  rate = int(input('How would you rate this interaction based on the given rubric? '))

  whatToDo(rate)

def whatToDo(rate):
  if(rate == 1):
    print('You should immediatly remove yourself from the situation, go to a place of peace and journal.')
  elif(rate == 2):
    print('If possible, remove self from situation. If not, mentally take your mind to a place of peace and choose not to engage. Reflect later in your journal.')
  elif(rate == 3):
    print('Live journal, try to see why this experience is causing indiffernece. You should be able to find something positive about the situation and hold on to that.')
  elif(rate == 4):
    print('Awesome, try to take a look around to look to see patterns so you can continue to have enjoyable experiences. Record this experience in your night journal!')
  elif(rate == 5):
    print('Keep it up! Sounds like you had a great time. Bask in the moment but rememember to take note of what makes this experience so expentional so you can surround yourself with a continuance of exceptional experiences!')

main()
