class Colours: 
  reset='\033[0m'
  underline='\033[04m' 
  bold = '\033[1m'

  class fg: 
    red  ='\033[31m'
    orange ='\033[33m'
    yellow ='\033[93m'
    green ='\033[32m'
    lightgreen ='\033[92m'
    blue ='\033[34m'
    lightblue='\033[94m'
    cyan ='\033[36m'
    purple ='\033[35m'
    pink ='\033[95m'

  class bg: 
    red ='\033[41m'
    orange ='\033[43m'
    green ='\033[42m'
    blue ='\033[44m'
    cyan ='\033[46m'
    purple ='\033[45m'
    lightgrey ='\033[47m'
    black ='\033[40m'

  input_colour = fg.orange
  equipment_colour = fg.lightblue
  attribute_colour = fg.lightblue
  enemy_colour = fg.red + bold
  tag_colour = fg.green + underline
  

  tag = lambda string: f"{Colours.tag_colour}[{string}]{Colours.reset}"