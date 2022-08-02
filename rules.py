filename = open('code.el', 'r')

variables = {}

for line, command in enumerate(filename, 1):
     command = command.strip()

     # Comments 
     if command.startswith('-') or not command.strip():
          pass

     elif command.casefold().startswith('var '):
          command = command[4:]
          variable_name, variable_value = command.replace(" ", "").split("=")
          variables[variable_name.strip()] = variable_value.strip()

     elif command.casefold().startswith('say '):
          if command[:4].strip() not in variables.keys():
               print(command[4:].encode('raw_unicode_escape').decode('unicode_escape'))
          else:
               print(variables[command[:4].strip()])
     else:
          if command.casefold() == 'say':
               print('There\'s nothing to say! If you want to make a new line use the "\\n" method.')
          else:
               print(f'On line {line}, command was not recognised')
