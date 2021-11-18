 
file_input_ = open('06_Publications.md','r')
file_output_ = open('06_Publications_last_five_years.md', 'w')

for line_ in file_input_:
    
    if '### 2016' in line_:
        break
    else:
        file_output_.write(line_)
        
file_input_.close()
file_output_.close()
    
file_input_ = open('09_Congress.md','r')
file_output_ = open('09_Congress_last_five_years.md', 'w')

for line_ in file_input_:
    
    if '### 2016' in line_:
        break
    else:
        file_output_.write(line_)
        
file_input_.close()
file_output_.close()
