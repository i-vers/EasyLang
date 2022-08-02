filename = open('code.el', 'r')

for line, command in enumerate(filename, 1):
     command = command.strip()

     # Comments 
     if command.startswith('-') or not command.strip():
          pass

     elif command.casefold().startswith('var '):
          command = command[4:]
          print(command)

     elif command.casefold().startswith('say '):
          print(command[4:].encode('raw_unicode_escape').decode('unicode_escape'))
  
   
     else:
          if command.casefold() == 'say':
               print('There\'s nothing to say! If you want to make a new line use the "\\n" method.')

          else:
               print(f'On line {line}, command was not recognised')
